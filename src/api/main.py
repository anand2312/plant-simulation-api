import simpy
from loguru import logger
from fastapi import FastAPI
from sim import simulation, builder

from .models import PlantConfiguration
import logging


logging.basicConfig(level=logging.DEBUG)

app = FastAPI(
    title="Warehouse Plant Simulation API",
    description="REST API for warehouse plant simulation using SimPy",
    version="0.1.0"
)


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint providing API information."""
    return {
        "message": "Warehouse Plant Simulation API",
        "version": "0.1.0",
        "docs": "/docs"
    }


@app.post("/run")
async def run_simulation(obj: PlantConfiguration, until: int) -> dict[str, simulation.ComponentStats]:
    logger.info(f"Starting simulation run with obj = {obj}")
    env = simpy.Environment()
    components = builder.PlantBuilder(env).build_from_dict(obj.model_dump())
    sim = simulation.Simulation(env, components)
    sim.run(until)
    logger.info(f"Results for {obj}: {sim.get_results()}")
    return sim.get_results()
