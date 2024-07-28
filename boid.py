import pygame
import random
import math
from settings import *

class Boid:
    SEPARATION_FACTOR = 1.5
    ALIGNMENT_FACTOR = 1.0
    COHESION_FACTOR = 1.0
    NEIGHBOR_RADIUS = 50
    AVOID_OBST_FACTOR = 2.0
    AVOID_PRED_FACTOR = 3.0
    MAX_SPEED = 4
    MAX_FORCE = 0.1

    separation_enabled = True
    alignment_enabled = True
    cohesion_enabled = True

    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.acceleration = pygame.Vector2(0, 0)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def update(self, boids, obstacles, predators):
        self.flock(boids)

        avoid_obstacles = self.avoid_obstacles(obstacles) * self.AVOID_OBST_FACTOR
        self.apply_force(avoid_obstacles)
        
        avoid_predators = self.avoid_predators(predators) * self.AVOID_PRED_FACTOR
        self.apply_force(avoid_predators)

        self.velocity += self.acceleration
        if self.velocity.length() > self.MAX_SPEED:
            self.velocity.scale_to_length(self.MAX_SPEED)
        self.position += self.velocity
        self.acceleration *= 0

        # Bounce off edges
        if self.position.x < 0 or self.position.x > WIDTH:
            self.velocity.x *= -1
        if self.position.y < 0 or self.position.y > HEIGHT:
            self.velocity.y *= -1

        self.position.x = max(0, min(self.position.x, WIDTH))
        self.position.y = max(0, min(self.position.y, HEIGHT))

    def apply_force(self, force):
        self.acceleration += force

    def flock(self, boids):
        if Boid.separation_enabled:
            separation = self.separate(boids) * Boid.SEPARATION_FACTOR
            self.apply_force(separation)
        if Boid.alignment_enabled:
            alignment = self.align(boids) * Boid.ALIGNMENT_FACTOR
            self.apply_force(alignment)
        if Boid.cohesion_enabled:
            cohesion = self.cohere(boids) * Boid.COHESION_FACTOR
            self.apply_force(cohesion)
        
        

    def separate(self, boids):
        steer = pygame.Vector2(0, 0)
        count = 0
        for other in boids:
            distance = self.position.distance_to(other.position)
            if 0 < distance < BOID_SIZE * 2:
                diff = self.position - other.position
                diff /= distance
                steer += diff
                count += 1
        if count > 0:
            steer /= count
        if steer.length() > 0:
            steer.scale_to_length(self.MAX_SPEED)
            steer -= self.velocity
            if steer.length() > self.MAX_FORCE:
                steer.scale_to_length(self.MAX_FORCE)
        return steer

    def align(self, boids):
        sum_velocity = pygame.Vector2(0, 0)
        count = 0
        for other in boids:
            if self.position.distance_to(other.position) < Boid.NEIGHBOR_RADIUS:
                sum_velocity += other.velocity
                count += 1
        if count > 0:
            sum_velocity /= count
            sum_velocity.scale_to_length(self.MAX_SPEED)
            steer = sum_velocity - self.velocity
            if steer.length() > self.MAX_FORCE:
                steer.scale_to_length(self.MAX_FORCE)
            return steer
        return pygame.Vector2(0, 0)

    def cohere(self, boids):
        sum_position = pygame.Vector2(0, 0)
        count = 0
        for other in boids:
            if self.position.distance_to(other.position) < Boid.NEIGHBOR_RADIUS:
                sum_position += other.position
                count += 1
        if count > 0:
            sum_position /= count
            return self.seek(sum_position)
        return pygame.Vector2(0, 0)

    def seek(self, target):
        desired = target - self.position
        if desired.length() == 0:
            return pygame.Vector2(0, 0)
        desired.scale_to_length(self.MAX_SPEED)
        steer = desired - self.velocity
        if steer.length() > self.MAX_FORCE:
            steer.scale_to_length(self.MAX_FORCE)
        return steer

    def avoid_obstacles(self, obstacles):
        steer = pygame.Vector2(0, 0)
        for obstacle in obstacles:
            distance = self.position.distance_to(obstacle.position)
            if distance < OBSTACLE_SIZE * 2:
                diff = self.position - obstacle.position
                diff /= distance
                steer += diff
        if steer.length() > 0:
            steer.scale_to_length(self.MAX_SPEED)
            steer -= self.velocity
            if steer.length() > self.MAX_FORCE:
                steer.scale_to_length(self.MAX_FORCE)
        return steer

    def avoid_predators(self, predators):
        steer = pygame.Vector2(0, 0)
        for predator in predators:
            distance = self.position.distance_to(predator.position)
            if distance < PREDATOR_AVOIDANCE_RADIUS:
                diff = self.position - predator.position
                diff /= distance
                steer += diff
        if steer.length() > 0:
            steer.scale_to_length(self.MAX_SPEED)
            steer -= self.velocity
            if steer.length() > self.MAX_FORCE:
                steer.scale_to_length(self.MAX_FORCE)
        return steer

    def draw(self, screen):
        angle = math.atan2(self.velocity.y, self.velocity.x)
        points = [
            (self.position.x + BOID_SIZE * math.cos(angle), self.position.y + BOID_SIZE * math.sin(angle)),
            (self.position.x + BOID_SIZE * math.cos(angle + 2.5), self.position.y + BOID_SIZE * math.sin(angle + 2.5)),
            (self.position.x + BOID_SIZE * math.cos(angle - 2.5), self.position.y + BOID_SIZE * math.sin(angle - 2.5))
        ]
        pygame.draw.polygon(screen, self.color, points)

