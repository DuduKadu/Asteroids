import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_random = random.uniform(20,50)
        asteroid_pos1 = self.velocity.rotate(split_random)
        asteroid_pos2 = self.velocity.rotate(-split_random)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        First = Asteroid(self.position.x, self.position.y, new_radius)
        Second = Asteroid(self.position.x, self.position.y, new_radius)

        First.velocity += asteroid_pos1 * 1.2
        Second.velocity += asteroid_pos2 * 1.2

