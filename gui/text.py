from ..core.entity import Entity
import pygame

class Text(Entity):

    def __init__(self, text: str = "", color: str = "white", size: int = 50, font_path: None|str = None):
        self.size = size
        self.font_path = font_path

        self.text = text
        self.color = color

        self.update_font()
        self.update_text()

        super().__init__(self.graphical, None)

    def update_font(self) -> None:
        self.font = pygame.font.Font(self.font_path, self.size)

    def update_text(self) -> None:
        self.graphical = self.font.render(self.text, False, self.color)
    
    def update_physical(self) -> None:
        self.physical = self.graphical.get_rect()