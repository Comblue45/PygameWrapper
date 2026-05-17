from pygame import font
from ..core import Entity

class Text(Entity):

    def __init__(self, text: str = "", color: str = "black", size: int = 50) -> None:
        self.text = text
        self.color = color
        self.size = size
        self.font = font.Font(None, self.size)
        super().__init__(image=self.font.render(self.text, None, self.color))
    
    def update_text(self) -> None:
        self.font = font.Font(None, self.size)
        self.image = self.font.render(self.text, None, self.color)
        self.update_auto_rect()