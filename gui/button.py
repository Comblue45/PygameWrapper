from ..core import Entity
from .text import Text
import pygame

class Button(Entity):

    def __init__(self, size: tuple[int,int] = (100,100), color: str = "red", text: Text|None = None):
        self.size = size
        self.color = color
        self.text = text if text else Text("Button")

        final_suface = pygame.Surface(size=self.size)
        final_suface.fill(self.color)
        super().__init__(final_suface)

    def ready(self, game):
        super().ready(game)
        self.game.current_scene.append(self.text)

    def delete(self) -> None:
        self.game.current_scene.remove(self.text)
        self.game.current_scene.remove(self)
    
    def update_button(self) -> None:
        self.graphical = pygame.Surface(self.size)
        self.graphical.fill(self.color)
        self.physical = self.graphical.get_rect()