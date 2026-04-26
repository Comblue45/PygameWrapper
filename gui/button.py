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

        self.is_pressed = False
        self.just_pressed = False
    
    def ready(self, game):
        super().ready(game)
        self.game.current_scene.append(self.text)

    def update(self, dt):
        super().update(dt)
        if self.is_on_point(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.is_pressed = True
            else:
                self.is_pressed = False
            if self.game.pressed_mouse[0]:
                self.just_pressed = True
            else:
                self.just_pressed = False

    def delete(self) -> None:
        self.game.current_scene.remove(self.text)
        self.game.current_scene.remove(self)
    
    def update_button(self) -> None:
        self.graphical = pygame.Surface(self.size)
        self.graphical.fill(self.color)
        self.physical = self.graphical.get_rect()