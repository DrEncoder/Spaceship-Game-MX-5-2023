import pygame
import os
import csv

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE_COLOR, RED_COLOR, LOGO
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components.asteroids.asteroid_handler import AsteroidHandler
from game.components.power_ups.power_up_handler import PowerUpHandler
from game.utils import text_utils


class Game:

    STATS_FILE = 'statistics.csv'

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()
        self.asteorid_handler = AsteroidHandler()
        self.power_up_handler = PowerUpHandler()
        self.number_death = 0
        self.score = 0
        self.game_over = False
        self.menu_selection = 0
        self.statistics = self.load_statistics()
        

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                if self.playing:
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                else:
                    if event.key == pygame.K_UP:
                        self.menu_selection -= 1
                        if self.menu_selection < 0:
                            self.menu_selection = 2
                    elif event.key == pygame.K_DOWN:
                        self.menu_selection += 1
                        if self.menu_selection > 2:
                            self.menu_selection = 0
                    elif event.key == pygame.K_RETURN:
                        if self.menu_selection == 0:
                            self.playing = True
                            self.reset()
                        elif self.menu_selection == 1:
                            self.show_high_scores()
                        elif self.menu_selection == 2:
                            self.show_statistics()
                        elif self.menu_selection == 3:
                            self.running = False

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input, self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler)
            self.bullet_handler.update(self.player, self.enemy_handler.enemies)
            self.asteorid_handler.update()
            self.power_up_handler.update(self.player)
            self.score = self.enemy_handler.number_enemies_destroyed
            if not self.player.is_alive:
                pygame.time.delay(500)
                self.playing = False
                self.number_death += 1
                self.game_over = True
                self.save_statistics()
                self.score = self.enemy_handler.number_enemies_destroyed


    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.asteorid_handler.draw(self.screen)
            self.power_up_handler.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    
    WIDTH=350
    HEIGHT=350

    def draw_menu(self):
        menu_options = ['Start Game', 'High Scores', 'Statistics', 'Exit']
        menu_color = [WHITE_COLOR] * 4
        menu_color[self.menu_selection] = RED_COLOR

        menu_image = LOGO
        menu_image = pygame.transform.scale(menu_image, (self.WIDTH, self.HEIGHT))
        menu_image_rect = menu_image.get_rect()
        menu_image_rect.center = (550, 150)
        self.screen.blit(menu_image, menu_image_rect)

        for index, option in enumerate(menu_options):
            text, text_rect = text_utils.get_message(option, 30, menu_color[index], height=SCREEN_HEIGHT // 1.3 - 100 + index * 40)
            self.screen.blit(text, text_rect)

        if self.game_over:
            score_text, score_rect = text_utils.get_message(f'Your score was: {self.score}', 20, RED_COLOR, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 250)
            self.screen.blit(score_text, score_rect)

        if self.menu_selection == 2:
            self.show_statistics()

           
    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 20, WHITE_COLOR, 1000, 40)
        self.screen.blit(score, score_rect)

    def save_statistics(self):
        with open(Game.STATS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Number of Deaths', 'Total Ships Destroyed'])
            writer.writerow([self.number_death, self.enemy_handler.number_enemies_destroyed])

    def load_statistics(self):
        if not os.path.isfile(Game.STATS_FILE):
            return {'Number of Deaths': 0, 'Total Ships Destroyed': 0}

        with open(Game.STATS_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            try:
                row = next(reader)
                return {'Number of Deaths': int(row[0]), 'Total Ships Destroyed': int(row[1])}
            except (csv.Error, IndexError):
                return {'Number of Deaths': 0, 'Total Ships Destroyed': 0}

    def show_statistics(self):
        statistics = {
            'Number of Deaths': self.number_death,
            'Total Ships Destroyed': self.enemy_handler.number_enemies_destroyed
        }

        self.statistics.update(statistics)
        self.save_statistics()

        stat_text = ""
        for stat_name, stat_value in self.statistics.items():
            stat_text += f'{stat_name}: {stat_value}\n'

        stat_message, stat_rect = text_utils.get_message(stat_text, 20, WHITE_COLOR, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.screen.blit(stat_message, stat_rect)

    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.asteorid_handler.reset()
        self.power_up_handler.reset()
