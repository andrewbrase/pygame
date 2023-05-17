import pygame

pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
running = True

while running:

    # Check for player quitting game, break out of game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    clock.tick(60)

pygame.quit()