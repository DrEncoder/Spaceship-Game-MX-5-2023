from game.components.asteroids.asteroid import Asteroid


class AsteroidHandler():
    def __init__(self):  
        self.asteroids = []
        self.number_asteroids_destroyed = 0

    def update(self):
        self.add_enemy()
        for asteroid in self.asteroids:
            asteroid.update()
            if asteroid.is_destroyed:
                self.number_asteroids_destroyed += 1
            if not asteroid.is_alive:
                self.remove_asteroid(asteroid)

    def draw(self, screen):
        for asteroid in self.asteroids:
            asteroid.draw(screen)

    def add_enemy(self):
        if len(self.asteroids) < 1:
           self.asteroids.append(Asteroid())

    def remove_asteroid(self, asteroid):
        self.asteroids.remove(asteroid)

    def reset(self):
        self.asteroids = []