from game.utils.constants import BULLET_ENEMY_TYPE
from game.utils.constants import BULLET_PLAYER_TYPE
from game.utils.constants import BULLET_BURGUER_TYPE
from game.utils.constants import BULLET_FINAL_BOSS_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.spaceship_bullet import SpaceshipBullet
from game.components.bullets.burguer_bullet import BurguerBullet
from game.components.bullets.bullet_final_boss import BulletFinalBoss

class BulletHandler:
    def __init__(self):
        self.bullets = []

    def update(self, player, enemies):
        for bullet in self.bullets:
            if type(bullet) is BulletEnemy: 
                bullet.update(player)
            if type(bullet) is BurguerBullet: 
                bullet.update(player)
            if type(bullet) is BulletFinalBoss: 
                bullet.update(player)
            elif type(bullet) is SpaceshipBullet:
                for enemy in enemies:
                    bullet.update(enemy)
            if not bullet.is_alive:
                self.remove_bullet(bullet)
        

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
           self.bullets.append(BulletEnemy(center))

        elif type == BULLET_PLAYER_TYPE:
           self.bullets.append(SpaceshipBullet(center))

        elif type == BULLET_BURGUER_TYPE:
           self.bullets.append(BurguerBullet(center))
        
        elif type == BULLET_FINAL_BOSS_TYPE:
           self.bullets.append(BurguerBullet(center))

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)

    def reset(self):
        self.bullets = []