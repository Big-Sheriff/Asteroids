import pygame
import random

from logger import log_event
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # Move the asteroid based on its velocity
        self.position += self.velocity * dt
    
    def split(self) -> list["Asteroid"]:
        self.kill()  # Remove the current asteroid from all sprite groups
        # Split the asteroid into two smaller asteroids if it's large enough
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        else:
            log_event("asteroid_split")
            new_angle =  random.uniform(20, 50)
            new_vector1 = self.velocity.rotate(new_angle)
            new_vector2 = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroit2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = new_vector1 * 1.2
            asteroit2.velocity = new_vector2 * 1.2
