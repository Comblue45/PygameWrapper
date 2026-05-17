from dataclasses import dataclass
from .entity import Entity

@dataclass(slots=True)
class Event:
    author: Entity
    target: Entity