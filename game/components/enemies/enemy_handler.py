from game.components.enemies.ship import Ship
from game.components.enemies.diagonal_enemy_right import EnemyThree
from game.components.enemies.diagonal_enemyl_left import EnemyTwo

class EnemyHandler():
    def __init__(self):  
        self.enemies = []
        self.number_enemies_destroyed = 0

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
        if len(self.enemies) < 3:
           self.enemies.append(Ship())
           self.enemies.append(EnemyTwo())
           self.enemies.append(EnemyThree())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def reset(self):
        self.enemies = []
        self.number_enemies_destroyed = 0