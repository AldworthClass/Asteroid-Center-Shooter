import pygame
from Bullet import Bullet
import MyFunctions

# Define some colors, you may want to add more
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Player():
    def __init__(self, screen, location, size, bullets, asteroids):
        self.location = location
        self.health = 5
        self.shields = 100
        self.x_speed = 0
        self.y_speed = 0
        self.screen = screen
        self.mid = [size[0]/2, size[1]/2]
        self.bullets = bullets
        self.asteroids = asteroids
        self.score = 0
        self.color = BLUE
        self.shield_color = GREEN
        self.radius = 15

    def move(self):

        # move ship, must stay on screen
        self.location[0] += self.x_speed
        self.location[1] += self.y_speed
        #if ship goes off screen, put it back in place
        if self.location[0] < 0 + self.radius or self.location[0] + self.radius > self.mid[0]*2:
            self.location[0] -= self.x_speed
        if self.location[1] < 0 + self.radius or self.location[1] + self.radius > self.mid[1]*2:
            self.location[1] -= self.y_speed
        if self.check_hit():# player hit asteroid
            return True #Ends here if ship is dead
        #moves projectile
        for bullet in self.bullets:
            if not bullet.move():#Removes bullets if they are off the screen
                self.bullets.remove(bullet)
            else:
                if bullet.check_asteroid_hit(self.asteroids):#Checks for a collision with an asteroid
                    self.bullets.remove(bullet)
                    print("asteroid destroyed")
                    self.score += 5
        return False



    #adding collision
    def check_hit(self):

        for asteroid in self.asteroids:
            if MyFunctions.distance(asteroid.location, self.location) < asteroid.size + 15:
                self.shields -= 1
                if self.shields < 40:
                    self.shield_color = RED

        #shields instantly destroyed when centerpoint hit
        if(MyFunctions.distance(self.location, self.mid) < self.radius + 5):
            self.shields = 0
        #If ship is dead
        if self.shields == 0:
            return True
        #If ship is not dead
        return False

    def draw(self):
        # draws ship
        pygame.draw.circle(self.screen, self.color, self.location, 10)
        if self.shields > 0:
            pygame.draw.circle(self.screen, self.shield_color, self.location, self.radius, 2)

        #draws turret
        pygame.draw.line(self.screen, WHITE, self.location, MyFunctions.get_point_circle(self.radius, self.location, self.mid), 3)

        #draws bullets
        for bullet in self.bullets:
            bullet.draw(self.screen)


    def shoot(self):
        #copy list b/c bullet only needs the points, not a reference to the list
        self.bullets.append(Bullet(self.location.copy(), self.mid ))
