import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode(
    (screen_width, screen_height), 
    pygame.FULLSCREEN)

clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.posx = 500
        self.posy = 200
        self.color = (255, 255, 0)

my_player = Player()

running = True
while running:

    for event in pygame.event.get():

        # Check for player quitting game, break out of game loop
        if event.type == pygame.QUIT:
            running = False

        # Check for player mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            my_player.posx, my_player.posy = pygame.mouse.get_pos()

            screen.fill((0,0,0))

            circle = pygame.draw.circle(
                screen, my_player.color, 
                (my_player.posx, my_player.posy), 
                30)
            
            pygame.display.flip()
            
    clock.tick(60)

pygame.quit()