from typing import Any
from loguru import logger
from fastapi import FastAPI
import simpy
from sim import simulation, builder

app = FastAPI(
    title="Warehouse Plant Simulation API",
    description="REST API for warehouse plant simulation using SimPy",
    version="0.1.0"
)


@app.get("/")
async def root():
    """Root endpoint providing API information."""
    return {
        "message": "Warehouse Plant Simulation API",
        "version": "0.1.0",
        "docs": "/docs"
    }


@app.get("/run")
async def run_simulation(obj: dict[str, Any], until: int) -> dict[str, simulation.DrainResults]:
    logger.info(f"Starting simulation run with obj = {obj}")
    env = simpy.Environment()
    components = builder.PlantBuilder(env).build_from_dict(obj)
    sim = simulation.Simulation(env, components)
    sim.run(until)
    logger.info(f"Results for {obj}: {sim.get_results()}")
    return sim.get_results()
