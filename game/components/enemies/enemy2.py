import pygame
from game.components.enemies.enemy import Enemy
from  game.utils.constants import ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH, BULLET_ENEMY_TYPE

class EnemyTwo(Enemy):
    WIDTH = 40
    HEIGHT = 60
    SPEED_X = 10 
    SPEED_Y = 10
    SHOOTING_TIME = 15

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.is_alive = True
        self.shooting_time = 0

    def update(self, bullet_handler):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        elif self.rect.x >= SCREEN_WIDTH:
            self.is_alive = False
        self.shooting_time += 1
        self.move()
        self.shoot(bullet_handler)
    
    def move(self):
        self.rect.y += self.SPEED_Y
        self.rect.x -= self.SPEED_X

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
         bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)