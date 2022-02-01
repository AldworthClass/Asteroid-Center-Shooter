import pygame
from Player import Player
from Asteroid import Asteroid
from Bullet import Bullet
from HUD import HUD
import MyFunctions
import random


# Define some colors, you may want to add more
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (250, 250, 0)

def end_game_screen(screen, clock, ship):
    done = False
    pos = [0, 0]
    while not done:
        # --- Main event loop

        # --- All events are detected here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

        if pygame.Rect([50, 50, 200, 100]).collidepoint(pos):
            return True
            #reset or quit

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, [50, 50, 200, 100])
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("GAME OVER", True, BLACK)
        screen.blit(text, [55, 50])



        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)


pygame.init()


# Set the width and height of the screen [width, height]
size = (700, 500)


screen = pygame.display.set_mode((size[0], size[1]+100))

asteroid_image = pygame.image.load("asteroid.png").convert_alpha()
background_image = pygame.image.load("space_background.png").convert()
mass_relay_image = pygame.image.load("mass_relay.png").convert_alpha()
mass_relay_image = pygame.transform.scale(mass_relay_image, (100, 51))

num_baddies = 2
baddies = []

bullets = []

num_asteroids = 10
asteroids = []

ship = Player(screen, [350, 15], size, bullets, asteroids)
stats_display = HUD(screen, ship, asteroids, bullets)
pygame.display.set_caption("My Game")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------

#Create obstacles
for i in range (num_asteroids):
    asteroids.append(Asteroid([random.randrange(5, size[0] - 5),random.randrange(5, size[1]) - 10], screen, size, asteroid_image))

time = 0
seconds = 0

while not done:
    # --- Main event loop

    # --- All events are detected here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so adjust speed
            if event.key == pygame.K_LEFT:
                ship.x_speed += -2
            elif event.key == pygame.K_RIGHT:
                ship.x_speed += 2
            elif event.key == pygame.K_UP:
                ship.y_speed += -2
            elif event.key == pygame.K_DOWN:
                ship.y_speed += 2
            elif event.key == pygame.K_SPACE:
                ship.shoot()

            # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT:
                ship.x_speed += 2
            elif event.key == pygame.K_RIGHT:
                ship.x_speed -= 2
            elif event.key == pygame.K_UP:
                ship.y_speed += 2
            elif event.key == pygame.K_DOWN:
                ship.y_speed -= 2

    # --- Game logic should go here
    time += 1
    if time == 60:
        time = 0
        seconds += 1

    if ship.move():     #Moves ship, which also handles all projectiles
        done = end_game_screen(screen, clock, ship)


    # --- Screen-clearing code goes here
    #  Here, we clear the screen to white.
    #screen.fill(BLACK)
    screen.blit(background_image, [0, 0])
    

    # --- Drawing code should go here
    #center portal
    screen.blit(mass_relay_image, [292, 217])
    #pygame.draw.circle(screen, YELLOW, [int(size[0]/2), int(size[1]/2)], 5)

    #ship and ships bullets are drawn
    ship.draw()

    #Draws and Moves asteroids
    for asteroid in asteroids:
        asteroid.move()
        asteroid.draw()

    stats_display.update(seconds)

    if len(asteroids) == 0:
        done = end_game_screen(screen, clock, ship)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
