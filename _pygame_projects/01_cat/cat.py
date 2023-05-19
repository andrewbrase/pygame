import pygame

pygame.init()

# Set default width and height
default_w = 800
default_h = 800

# Set fullscreen
screen = pygame.display.set_mode(
    (default_w, default_h), 
    pygame.FULLSCREEN)

# Center coordinates
screen_x_mid, screen_y_mid = screen.get_rect().center

clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.posx = screen_x_mid
        self.posy = screen_y_mid
        self.color = (0, 0, 255)

player = Player()

click_pos = None
back_x = 0
back_y = 0

move_up = False
move_down = False
move_left = False
move_right = False

background = pygame.image.load("grid.png")

running = True
while running:
    screen.blit(background, (back_x, back_y))

    for event in pygame.event.get():

        # Check for player quitting game, break out of game loop
        if event.type == pygame.QUIT:
            running = False

        # Check for player mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                move_down = True
            elif event.key == pygame.K_w:
                move_up = True
            elif event.key == pygame.K_d:
                move_right = True
            elif event.key == pygame.K_a:
                move_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                move_down = False
            elif event.key == pygame.K_w:
                move_up = False
            elif event.key == pygame.K_d:
                move_right = False
            elif event.key == pygame.K_a:
                move_left = False

    if move_up:
        back_y += 5
    if move_down:
        back_y -= 5
    if move_left:
        back_x += 5
    if move_right:
        back_x -= 5
            
    player_mod = pygame.draw.rect(
        screen, player.color, 
        pygame.Rect(screen_x_mid, screen_y_mid, 60, 60)
        )
    
    if click_pos is not None:
        circle = pygame.draw.circle(
            screen, (255, 255, 0), 
            click_pos, 30)
    
    pygame.display.flip()
            
    clock.tick(60)

pygame.quit()