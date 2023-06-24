import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_FINAL_BOSS


class BulletFinalBoss(Bullet):
    WIDTH = 15
    HEIGHT = 40
    SPEED = 21


    def __init__(self, center):
        self.image = BULLET_FINAL_BOSS
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center)

    def update(self, player):
        self.rect.y += self.SPEED
        if not player.has_shield:
             super().update(player) 