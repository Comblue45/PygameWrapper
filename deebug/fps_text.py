from __future__ import annotations

from ..gui.text import Text


class FPSText(Text):
    def __init__(self, color: str = "white", size: int = 24) -> None:
        super().__init__(text="FPS: 0", color=color, size=size)

    def update(self, dt: float) -> None:
        fps = self.game.get_fps()
        self.text = f"FPS: {fps}"
        self.update_text()
        self.rect.topleft = (0, 0)