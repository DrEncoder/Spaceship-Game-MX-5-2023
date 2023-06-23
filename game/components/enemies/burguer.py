import pygame
from game.components.enemies.enemy import Enemy
from  game.utils.constants import BURGUER, BULLET_BURGUER_TYPE

class Burguer(Enemy):
    WIDTH = 60
    HEIGHT = 60
    SPEED_Y = 40
    SHOOTING_TIME = 15

    def __init__(self):
        self.image = BURGUER
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)

    def move(self):
        self.rect.y += self.SPEED_Y

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
         bullet_handler.add_bullet(BULLET_BURGUER_TYPE, self.rect.center)