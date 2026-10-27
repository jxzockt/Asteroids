from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import pygame
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius<= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random1=random.uniform(20,50)
            asteroid1=self.velocity.rotate(random1)
            asteroid2=self.velocity.rotate(random1*-1)
            radius_n=self.radius-ASTEROID_MIN_RADIUS
            new_asteroid1=Asteroid(self.position.x,self.position.y,radius_n)
            new_asteroid1.velocity=asteroid1*1.2
            new_asteroid2=Asteroid(self.position.x,self.position.y,radius_n)
            new_asteroid2.velocity=asteroid2*1.2
