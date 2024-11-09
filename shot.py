import pygame
from circleshape import CircleShape
class Shot(CircleShape):
    SHOT_RADIUS = 5
    
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.SHOT_RADIUS, 2)
        
    def update(self, dt):
        self.move(self.velocity * dt)