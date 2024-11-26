import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.move(self.velocity * dt)
        
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = vector2 * 1.2