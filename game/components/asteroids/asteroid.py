import random
import pygame
from  game.utils.constants import ASTEROID, SCREEN_HEIGHT, SCREEN_WIDTH

class Asteroid():
    X_POS_LIST = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050]
    Y_POS = -200
    WIDTH = 200
    HEIGHT = 200
    SPEED_X = 15 
    SPEED_Y = 15
    is_alive = True
    is_destroyed = False

    def __init__(self):
        self.image = ASTEROID
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__()
        self.is_alive = True
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS

    def update(self):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        elif self.rect.x >= SCREEN_WIDTH:
            self.is_alive = False
        self.move()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def move(self):
        self.rect.y += self.SPEED_Y
        self.rect.x -= self.SPEED_X