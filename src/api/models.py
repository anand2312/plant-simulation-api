from enum import Enum
from typing import Generic, TypeVar, Literal

from pydantic import BaseModel, Field


ParamsT = TypeVar("ParamsT", bound=BaseModel)

ComponentType = Literal["Source", "Drain", "Conveyor", "Station"]


class RoutingLogic(str, Enum):
    """Valid routing logic options for Router components."""
    ROUND_ROBIN = "round_robin"
    RANDOM = "random"


class SourceParams(BaseModel):
    """Parameters for Source components."""
    interval: float = Field(default=1.0, gt=0, description="Time between part generations")
    limit: int | None = Field(default=None, ge=1, description="Maximum parts to generate")
    start_immediately: bool = Field(default=True, description="Start generating at t=0")
    routing_strategy: RoutingLogic = Field(default=RoutingLogic.ROUND_ROBIN)


class ConveyorParams(BaseModel):
    """Parameters for Conveyor components."""
    travel_time: float = Field(default=1.0, gt=0, description="Time to travel across conveyor")
    capacity: int = Field(default=1, ge=1, description="Number of parts transported simultaneously")
    routing_strategy: RoutingLogic = Field(default=RoutingLogic.ROUND_ROBIN)



class StationParams(BaseModel):
    """Parameters for Station components."""
    processing_time: float = Field(default=1.0, gt=0, description="Time to process one part")
    capacity: int = Field(default=1, ge=1, description="Number of parts processed simultaneously")
    routing_strategy: RoutingLogic = Field(default=RoutingLogic.ROUND_ROBIN)


class DrainParams(BaseModel):
    capacity: int = Field(default=1, ge=1, description="Number of parts processed simultaneously")
    drain_time: float = Field(default=1.0, description="Time to process one part")


class Component(BaseModel, Generic[ParamsT]):
    """A component in the plant configuration."""
    name: str = Field(..., min_length=1, description="Unique identifier for this component")
    type: ComponentType = Field(..., description="Type of the component")
    params: ParamsT | dict = Field(default={}, description="Component-specific parameters")
    outputs: list[str] = Field(default=[], description="Downstream component name(s)")


class PlantConfiguration(BaseModel):
    """Top-level plant configuration specification."""
    components: list[Component[SourceParams | StationParams | ConveyorParams | DrainParams]] = Field(..., description="List of plant components")