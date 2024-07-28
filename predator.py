import pygame
import math
from settings import *
from boid import Boid
import random

class Predator(Boid):
    SEPARATION_FACTOR = 3.5
    ALIGNMENT_FACTOR = 0.5
    COHESION_FACTOR = 0.2

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = BOID_SIZE * 1.5  # Larger size for predator

    def update(self, predators, obstacles):
        self.flock(predators)
        
        avoid_obstacles = self.avoid_obstacles(obstacles) * 2.0
        self.apply_force(avoid_obstacles)

        self.velocity += self.acceleration
        if self.velocity.length() > MAX_SPEED:
            self.velocity.scale_to_length(MAX_SPEED)
        self.position += self.velocity
        self.acceleration *= 0

        # Bounce off edges
        if self.position.x < 0 or self.position.x > WIDTH:
            self.velocity.x *= -1
        if self.position.y < 0 or self.position.y > HEIGHT:
            self.velocity.y *= -1

        self.position.x = max(0, min(self.position.x, WIDTH))
        self.position.y = max(0, min(self.position.y, HEIGHT))



    def flock(self, boids):
        separation = self.separate(boids) * self.SEPARATION_FACTOR
        alignment = self.align(boids) * self.ALIGNMENT_FACTOR
        cohesion = self.cohere(boids) * self.COHESION_FACTOR

        self.acceleration += separation + alignment + cohesion

    def draw(self, screen):
        radius = PREDATOR_SIZE
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), radius)
