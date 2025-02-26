import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LEFT, RIGHT, BULLET_ENEMY_TYPE


class Enemy():
    X_POS_LIST = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]
    Y_POS = -50
    SPEED_X = 5  
    SPEED_Y = 2
    MOV_X = [LEFT, RIGHT]
    INTERVAL = 100
    SHOOTING_TIME = 60
    

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOV_X)
        self.is_alive = True
        self.is_destroyed = False
        self.index = 0
        self.shooting_time = 0

    def update(self, bullet_handler):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        self.shooting_time += 1
        self.move()
        self.shoot(bullet_handler)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.SPEED_Y
        if self.mov_x == LEFT:
            self.rect.x -= self.SPEED_X
            if self.index > self.INTERVAL or self.rect.left <= 0:
                self.mov_x = RIGHT
                self.index = 0
        else:
            self.rect.x += self.SPEED_X
            if self.index > self.INTERVAL or self.rect.right >= SCREEN_WIDTH:
                self.mov_x = LEFT
                self.index = 0
        self.index += 1

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
         bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)



