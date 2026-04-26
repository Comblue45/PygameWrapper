from .entity import Entity
import pygame

class Game:

    def __init__(self,
                 size: tuple[int, int] = (500, 500),
                 title: str = "PygameHelper",
                 first_scene: list[Entity]|None = None,
                 background_color: str = "black",
                 FPS: int = 60):
        self.change_current_scene(first_scene if first_scene else [])
        self.background_color = background_color
        self.FPS = FPS

        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.dt = 0.0
        self.running = False

        self.pressed_keys = pygame.key.get_pressed()
        self.pressed_mouse = pygame.mouse.get_pressed()

        self.just_pressed_keys = {}
        self.just_pressed_mouse = {key: False for key in range(0,3)}

    def start(self) -> None:
        self.running = True

        while self.running:
            self.pressed_keys = pygame.key.get_pressed()
            self.pressed_mouse = pygame.mouse.get_pressed()

            for key in self.just_pressed_keys.keys():
                self.just_pressed_keys[key] = False
            for key in self.just_pressed_mouse.keys():
                self.just_pressed_mouse[key] = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    self.just_pressed_keys[event.key] = True
            

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.just_pressed_mouse[0] = True
                    elif event.button == 2:
                        self.just_pressed_mouse[1] = True
                    elif event.button == 3:
                        self.just_pressed_mouse[2] = True

            self.screen.fill("black")
            for entity in self.current_scene:
                entity.update(self.dt)
                if entity.graphical:
                    self.screen.blit(entity.graphical, entity.physical)
            pygame.display.flip()

            self.dt = self.clock.tick(self.FPS) / 1000

    def change_current_scene(self, new_scene) -> None:
        self.current_scene = new_scene
        for entity in self.current_scene:
            entity.ready(self)
    
    def add_pressed_key(self, key: int) -> None:
        self.just_pressed_keys[key] = False