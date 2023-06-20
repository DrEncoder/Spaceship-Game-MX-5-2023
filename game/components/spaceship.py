import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_ENEMY_TYPE

class Spaceship:
     WIDTH = 40
     HEIGHT = 60
     X_POS = (SCREEN_WIDTH // 2) - WIDTH
     Y_POS = 500

     def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.shooting_time = 0

     def update(self, user_input, object):
        if user_input[pygame.K_LEFT]:
           self.move_left()

        elif user_input[pygame.K_RIGHT]:
            self.move_right()

        elif user_input[pygame.K_UP]:
            self.move_up()

        elif user_input[pygame.K_DOWN]:
            self.move_down()

            self.move()
     
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        if self.rect.colliderect(object.rect):
            object.is_alive = False
            self.is_alive = False
     
     


     def draw(self, screen):
        screen.blit(self.image, self.rect)

     def move_left(self):
        if self.rect.left > 0:
              self.rect.x -= 10
     
     def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10  

     def move_up(self):
         if self.rect.top > (SCREEN_HEIGHT // 2):
            self.rect.y -= 10      

     def move_down(self):
         if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10    
      
     def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
         bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)

     
