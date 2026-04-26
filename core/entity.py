import pygame

class Entity:

    def __init__(self, 
                 surface: pygame.Surface|None = None, 
                 physical: pygame.Rect|None = None):
        self.graphical = surface
        self.physical = physical if physical else surface.get_rect() if surface else None

    def ready(self, game) -> None:
        self.game = game

    def update(self, dt: float) -> None:
        pass
    
    def is_colliding(self, other_entity) -> bool:
        if self.physical.colliderect(other_entity.physical):
            return True
        return False

    def is_on_point(self, point: tuple[int,int]) -> bool:
        if self.physical.collidepoint(point):
            return True
        return False

    def is_clicked(self) -> bool:
        if self.is_on_point(pygame.mouse.get_pos()):
            if self.game.pressed_mouse[0]:
                return True
        return False

    def was_clicked(self) -> bool:
        if self.is_on_point(pygame.mouse.get_pos()):
            if self.game.just_pressed_mouse[0]:
                return True
        return False