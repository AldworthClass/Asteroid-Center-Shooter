import Asteroid
import Player
import Bullet
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class HUD():
    def __init__(self, screen,  ship, asteroids, bullets):
        self.ship = ship
        self.asteroids = asteroids
        self.bullets = bullets
        self.color = WHITE
        self.screen = screen
        self.rect = [0, 500, 700, 200]

    def update(self, time):
        #White HUD region
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.draw_shields()
        self.draw_timer(time)
        self.draw_points()

    def draw_timer(self, time):
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Time: " + str(time), True, BLACK)
        self.screen.blit(text, [575, 510])


    #Draws shield indicator
    def draw_shields(self):
        # Add shield bar here
        pygame.draw.rect(self.screen, RED,[5, 505, 100, 33])
        if self.ship.shields > 0:
            pygame.draw.rect(self.screen, GREEN, [5, 505, self.ship.shields, 33])
        pygame.draw.rect(self.screen, BLACK, [5, 505, 100, 33], 1)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Shields", True, BLACK)
        self.screen.blit(text, [17, 510])

    def draw_points(self):
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Points:", self.ship.score, True, BLACK)
        self.screen.blit(text, [15, 555])
