import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BURGUER_BULLET


class BurguerBullet(Bullet):
    WIDTH = 9
    HEIGHT = 32
    SPEED = 20


    def __init__(self, center):
        self.image = BURGUER_BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center)

    def update(self, player):
        self.rect.y += self.SPEED
        super().update(player)