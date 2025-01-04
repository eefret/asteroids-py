import pygame

import random

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
        
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        a = Asteroid(self.position.x, self.position.y, new_radius)
        a.velocity = v1 * 1.2
        b = Asteroid(self.position.x, self.position.y, new_radius)
        b.velocity = v2 * 1.2
