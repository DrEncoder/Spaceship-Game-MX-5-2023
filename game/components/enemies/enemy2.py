import pygame
from game.components.enemies.enemy import Enemy
from  game.utils.constants import ENEMY_2, LEFT, SCREEN_HEIGHT, SCREEN_WIDTH

class EnemyTwo(Enemy):
    WIDTH = 40
    HEIGHT = 60
    MOV_X = LEFT
    INTERVAL = 1
    SPEED_X = 15  
    SPEED_Y = 15

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.mov_x = LEFT
        self.is_alive = True

    def update(self):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        elif self.rect.x >= SCREEN_WIDTH:
            self.is_alive = False
        self.move()
    
    def move(self):
        self.rect.y += self.SPEED_Y
        if self.index > self.INTERVAL:
            self.index = 0
            self.mov_x == LEFT
            self.rect.x -= self.SPEED_X
            if self.index > self.INTERVAL:
                self.index = 0  
        self.index += 1