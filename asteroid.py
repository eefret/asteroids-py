import pygame

from circleshape import CircleShape
import constants


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = "gray"

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
