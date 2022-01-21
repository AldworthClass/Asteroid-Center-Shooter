import pygame
import math
import MyFunctions

# Define some colors, you may want to add more
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Bullet():
    def __init__(self, start, dest):
        self.dest = dest
        self.color = BLUE
        self.upgraded = False
        self.radius = 2
        # Starts projectile in centre of ship
        self.loc = start
        #Screen size do determine if bullet should be removed
        self.screen_width = 2 * self.dest[0]
        self.scree_height = 2 * self.dest[1]

        self.speed_multiplier = 3

        # Determine appropriate speed to move projectiles based on slope and distance

        # Change in x between ship centre and mouse location
        self.run = self.dest[0] - self.loc[0]
        # Change in y between ship centre and mouse location
        self.rise = self.dest[1] - self.loc[1]
        if self.rise == 0:
            self.rise = -0.01
        distance = math.sqrt(self.run * self.run + self.rise * self.rise)
        # Normalizes speed by dividing out distance from rise and run and uses multiplyer to set speed
        self.x_speed = self.run / distance * self.speed_multiplier
        self.y_speed = self.rise / distance * self.speed_multiplier

        self.loc = MyFunctions.get_point_circle(15, self.loc, self.dest)

    def move(self):
        self.loc[0] += self.x_speed
        self.loc[1] += self.y_speed
        if math.sqrt((self.loc[0] - self.dest[0])**2 + (self.loc[1] - self.dest[1])**2) <= 2:
            self.upgrade()
        if self.loc[0] < 0 or self.loc[0] > self.screen_width or self.loc[1] < 0 or self.loc[1] > self.scree_height:
                return False

        return True

    def check_asteroid_hit(self, asteroids):
        for asteroid in asteroids:
            if (MyFunctions.distance(self.loc, asteroid.location) < self.radius + asteroid.size): #bullet and asteroid collide
                asteroid.weak_hit()
                if  self.upgraded or asteroid.size <= 5:
                    asteroids.remove(asteroid)
                return True
        return False

    def upgrade(self):
        self.color = RED
        self.upgraded = True
        self.radius = 4
        self.x_speed *= 2
        self.y_speed *= 2


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [int(self.loc[0]), int(self.loc[1])], self.radius)
