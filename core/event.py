from dataclasses import dataclass
from .entity import Entity

@dataclass(slots=True, frozen=True)
class Event:
    author: Entity
    target: Entity