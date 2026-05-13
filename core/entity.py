from __future__ import annotations
from typing import TYPE_CHECKING
from pygame import Surface, Rect

if TYPE_CHECKING:
    from .game import Game

class Entity:
    
    def __init__(self, 
                 image: Surface|None = None, 
                 rect: Rect|None = None,
                 parent: Entity|None = None,
                 tags: set[str]|None = None,
                 auto_rect: bool = True) -> None:
        self.image = image
        if rect:
            self.rect = rect
        elif auto_rect and image:
            self.rect = self.image.get_rect()
        else:
            self.rect = Rect(0,0,0,0)

        self.parent = None
        self.set_parent(parent) if parent else None
        self.childern = []
        self.tags = tags if tags else set()
        self.game = None
        self.visible = True

    def set_parent(self, parent: Entity) -> None:
        self.parent = parent
        parent.childern.append(self)
    def remove_parent(self) -> None:
        self.parent.childern.remove(self)
        self.parent = None
    def add_child(self, child: Entity) -> None:
        child.parent = self
        self.childern.append(child)
    def remove_child(self, child: Entity) -> None:
        child.parent = None
        self.childern.remove(child)

    def setup(self, game: Game) -> None:
        self.game = game
    def ready(self) -> None:
        pass
    def removed_from_scene(self) -> None:
        pass
    def destroy(self) -> None:
        self.game.remove_entity(self)

    def before_update(self) -> None:
        pass
    def update(self, dt: float) -> None:
        pass
    def after_update(self) -> None:
        pass

    @property
    def x(self) -> int:
        return self.rect.topleft[0]
    @x.setter
    def x(self, new_value: int) -> None:
        self.rect.topleft = (new_value,
                             self.rect.topleft[1])
    @property
    def y(self) -> int:
        return self.rect.topleft[1]
    @y.setter
    def y(self, new_value: int) -> None:
        self.rect.topleft = (self.rect.topleft[0],
                             new_value)

    def world_position(self) -> tuple[int, int]:
        if not self.parent:
            return self.rect.topleft
        px, py = self.parent.world_position()
        return (self.x + px, self.y + py)