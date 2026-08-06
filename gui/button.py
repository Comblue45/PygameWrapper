from ..core import Entity
from .text import Text
import pygame

class Button(Entity):

    def __init__(self, color: tuple[int, int, int]|str, size: tuple[int, int], text: Text, *args, **kwargs) -> None:
        super().__init__()
        self.text: Text = text
        self.text.set_parent(self)
        self.text.rect.center = (self.rect.center[0], self.rect.center[1])

        surface = pygame.Surface(size)
        surface.fill(color)
        super().__init__(image=surface, *args, **kwargs)

        # Add text getting added to the scene and also deleted when the button is deleted
    
    def ready(self) -> None:
        super().ready()
        self.game.add_entity(self.text)

    def update(self, dt: float) -> None:
        super().update(dt)
        if self.was_just_pressed():
            self.on_just_pressed()
        if self.is_pressed():
            self.on_press()

        # self.text.rect.bottomleft = ((self.image.get_width() - self.text.image.get_width()) / 2, 
        #                              (self.image.get_height() - self.text.image.get_height()) - self.image.get_height() / 5)
        self.text.rect.center = (self.image.get_width() / 2, self.image.get_height() / 2)

    def on_press(self) -> None:
        pass
    def on_just_pressed(self) -> None:
        pass