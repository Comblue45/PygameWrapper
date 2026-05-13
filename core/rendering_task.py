from dataclasses import dataclass
from pygame import Surface

@dataclass(slots=True, frozen=True)
class RenderingTask:
    position: tuple[int, int]
    surface: Surface