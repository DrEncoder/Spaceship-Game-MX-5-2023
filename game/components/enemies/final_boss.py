import math
import pygame
from game.utils.constants import BULLET_ENEMY_TYPE, FINAL_BOSS, SCREEN_HEIGHT, SCREEN_WIDTH

class FinalBoss(pygame.sprite.Sprite):

    WIDTH = 1000
    HEIGHT = 500
    SPEED = 1
    X_POS = -500
    Y_POS = -500

    def __init__(self):
        super().__init__()
        self.image = FINAL_BOSS
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.health = 1000
        self.shoot_delay = 2000
        self.last_shot = pygame.time.get_ticks()
        self.is_destroyed = False
        self.is_alive = True
        self.shooting_time = 0
        self.path = [(50, -50), (50,50)]
        self.current_point_index = 0
        self.target_point = self.path[self.current_point_index]
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, bullet_handler):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        elif self.rect.x >= SCREEN_WIDTH:
            self.is_alive = False
        self.shooting_time += 1
        self.move()
        if self.health <= 0:
            self.kill()

        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            self.shoot(bullet_handler)

    def move(self):
        dx = self.target_point[0] - self.rect.x
        dy = self.target_point[1] - self.rect.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance <= self.SPEED:
            self.rect.x = self.target_point[0]
            self.rect.y = self.target_point[1]
            self.current_point_index += 1
            if self.current_point_index >= len(self.path):
                self.current_point_index = 0
            self.target_point = self.path[self.current_point_index]
        else:
            direction_x = dx / distance
            direction_y = dy / distance
            self.rect.x += direction_x * self.SPEED
            self.rect.y += direction_y * self.SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.midtop)
        bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.midbottom)
        bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.midleft)
        bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.midright)