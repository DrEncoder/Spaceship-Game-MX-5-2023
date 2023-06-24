import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
BURGUER_BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_4.png"))
BULLET_FINAL_BOSS = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_5.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
BURGUER = pygame.image.load(os.path.join(IMG_DIR, "Enemy/burguer.png"))
OVNI = pygame.image.load(os.path.join(IMG_DIR, "Enemy/ovni.png"))
FINAL_BOSS = pygame.image.load(os.path.join(IMG_DIR, "Enemy/final_boss.png"))

ASTEROID = pygame.image.load(os.path.join(IMG_DIR, "Asteroid/asteroid.png"))

LOGO = pygame.image.load(os.path.join(IMG_DIR, "Other/logo.png"))

FONT_STYLE = 'freesansbold.ttf'

BULLET_ENEMY_TYPE = 'enemy'
BULLET_PLAYER_TYPE = 'player'
BULLET_BURGUER_TYPE = 'burguer'
BULLET_FINAL_BOSS_TYPE = 'boss'

LEFT = 'left'
RIGHT = 'right'
DOWN = 'down'

BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
RED_COLOR = (239, 9, 9)
