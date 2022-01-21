import pygame
#generic bad guy class to be inherited from for various badguys
class Baddie():
    def __init__(self, screen, asteroids, player):
        self.screen = screen
        self.asteroids = asteroids
        self.player = player
        self.rect
