import math
import pygame
from game.components.enemies.enemy import Enemy
from  game.utils.constants import ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH, BULLET_ENEMY_TYPE

class GoAllOver(Enemy):
    WIDTH = 40
    HEIGHT = 60
    SPEED = 7
    SHOOTING_TIME = 60

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.is_alive = True
        self.shooting_time = 0
        self.path = [(50, -50), (50, 50), (1000, 50), (1000, 150), (50, 150), (50, 250), (1000, 250),
                      (1000, 350), (50, 350), (50, 450), (1000, 450), (1000, 550), (50, 550), (50, 650)]
        self.current_point_index = 0
        self.target_point = self.path[self.current_point_index]

    def update(self, bullet_handler):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        elif self.rect.x >= SCREEN_WIDTH:
            self.is_alive = False
        self.shooting_time += 1
        self.move()
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

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
         bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)