from game.components.enemies.ship import Ship
from game.components.enemies.go_all_over import GoAllOver
from game.components.enemies.burguer import Burguer
from game.components.enemies.ovni import Ovni
from game.components.enemies.final_boss import FinalBoss

class EnemyHandler():
    def __init__(self):  
        self.enemies = []
        self.number_enemies_destroyed = 0
        self.score = 0

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if enemy.is_destroyed:
                self.number_enemies_destroyed += 1
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 2:
           self.enemies.append(Ship())
           self.enemies.append(GoAllOver())
           self.enemies.append(Burguer())
           self.enemies.append(Ovni())
        if self.score >= 10:
            self.enemies.append(FinalBoss())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def reset(self):
        self.enemies = []
        self.number_enemies_destroyed = 0