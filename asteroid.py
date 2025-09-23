import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self, self.containers)
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(surface=screen,center=self.position, radius=self.radius, width=2, color="white")

    def update(self, dt):
        self.position += (self.velocity * dt)