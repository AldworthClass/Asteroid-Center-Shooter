import pygame
import random
import math

BROWN = (168, 96, 50)

class Asteroid():
    def __init__(self, location, screen, screen_size):
        self.location = location
        self.color = BROWN
        self.size = random.randint(8,14)
        self.x_speed = random.randint(-2, 2)
        self.y_speed = random.randint(-2, 2)
        self.screen = screen
        self.screen_size = screen_size


    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.location, self.size)

    def weak_hit(self):
        self.size -= 1

    def move(self):
        self.location[0] += self.x_speed
        self.location[1] += self.y_speed
        #hit left/right side
        if self.location[0] - self.size <= 0 or self.location[0] + self.size >= self.screen_size[0]:
            self.x_speed *= -1
        #hit top/bottom
        if self.location[1] - self.size <= 0 or self.location[1] + self.size >= self.screen_size[1]:
            self.y_speed *= -1
