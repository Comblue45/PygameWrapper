import pygame
from .entity import Entity
from .rendering_task import RenderingTask

class Game:

    def __init__(self, title: str = "PygameWrapper", background_color: str = "black", size: tuple[int, int] = (500, 500), scene: list[Entity]|None = None, FPS: int = 60) -> None:
        self.background_color = background_color
        self.scene = scene if scene else []
        self.FPS = FPS

        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.dt = 0.0
        self.running = False
        self._rendering_tasks: list[RenderingTask] = []

        self.just_pressed = {}
        self.just_pressed_mouse = {k: False for k in range(0,4)}
        print(self.just_pressed_mouse)

        self.setup_scene()

    def run(self) -> None:
        self.running = True

        while self.running:
            self._update()

    def _update(self) -> None:
        self._input()
        self._handle_entities()
        self._render()
        self._time()
        self._prepare_next_frame()

    def _input(self) -> None:
        self.just_pressed = {key: False for key in self.just_pressed.keys()}
        self.just_pressed_mouse = {key: False for key in self.just_pressed_mouse.keys()}
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.just_pressed[event.key] = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.just_pressed_mouse[0] = True
                if event.button == 2:
                    self.just_pressed_mouse[1] = True
                if event.button == 3:
                    self.just_pressed_mouse[2] = True

    def _handle_entities(self) -> None:
        for entity in self.scene:
            self._update_entity(entity)
            self._prepare_entity_rendering(entity)
    def _update_entity(self, entity: Entity) -> None:
        entity.before_update()
        entity.update(self.dt)
        entity.after_update()
    def _prepare_entity_rendering(self, entity: Entity) -> None:
        if entity.image and entity.visible:
            self._rendering_tasks.append(RenderingTask(entity.world_position(),
                                                       entity.image))

    def _render(self) -> None:
        self.screen.fill(self.background_color)
        for rendering_task in self._rendering_tasks:
            self.screen.blit(rendering_task.surface, rendering_task.position)
        pygame.display.flip()

    def _time(self) -> None:
        self.dt = self.clock.tick(self.FPS) / 1000

    def _prepare_next_frame(self) -> None:
        self._rendering_tasks.clear()

    def setup_scene(self) -> None:
        for entity in self.scene:
            entity.setup(self)
            entity.ready()

    def add_entity(self, entity: Entity) -> None:
        self.scene.append(entity)
        entity.setup(self)
        entity.ready()
    def remove_entity(self, entity: Entity) -> None:
        self.scene.remove(entity)
        entity.removed_from_scene()
        entity.remove_parent()
        for child in list(entity.childern):
            entity.remove_child(child)
    
    def add_just_pressed_key(self, key: int) -> None:
        self.just_pressed[key] = False