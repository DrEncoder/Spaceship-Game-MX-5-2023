from game.utils.constants import SCREEN_HEIGHT


class Bullet:
    def __init__(self, image, center):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.is_alive = True

    def update(self, object):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        if self.rect.colliderect(object.rect):
            object.is_alive = False
            self.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)