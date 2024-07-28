import pygame
from settings import *

class Obstacle:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
    
    def draw(self, screen):
        rect = pygame.Rect(self.position.x - OBSTACLE_SIZE // 2, self.position.y - OBSTACLE_SIZE // 2, OBSTACLE_SIZE, OBSTACLE_SIZE)
        pygame.draw.rect(screen, OBSTACLE_COLOR, rect)
