import pygame
import pygame_menu

pygame.init()

# Set default width and height for display
default_w = 800
default_h = 800

# Set display to fullscreen
screen = pygame.display.set_mode(
    (default_w, default_h), 
    pygame.FULLSCREEN)

# Center coordinates for player x,y
screen_x_mid, screen_y_mid = screen.get_rect().center

clock = pygame.time.Clock()

# Use Factory Method for future race selection
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

display_menu = False

def set_move_up_true():
    global move_up
    move_up = True

def set_move_down_true():
    global move_down
    move_down = True

def set_move_right_true():
    global move_right
    move_right = True

def set_move_left_true():
    global move_left
    move_left = True

key_map_keydown = {
    "w" : set_move_up_true,
    "s" : set_move_down_true,
    "a" : set_move_left_true,
    "d" : set_move_right_true
}

def set_move_up_false():
    global move_up
    move_up = False

def set_move_down_false():
    global move_down
    move_down = False

def set_move_right_false():
    global move_right
    move_right = False

def set_move_left_false():
    global move_left
    move_left = False

key_map_keyup = {
    "w" : set_move_up_false,
    "s" : set_move_down_false,
    "a" : set_move_left_false,
    "d" : set_move_right_false
}

background = pygame.image.load("grid.png")
menu = pygame_menu.Menu(
    "Test", 400, 300, theme=pygame_menu.themes.THEME_BLUE,)

menu.add.button("Quit", pygame_menu.events.EXIT)
menu.mainloop(screen)

# menu.add.text_input('Name :', default='John Doe')
# menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
# menu.add.button('Play', start_the_game)
# menu.add.button('Quit', pygame_menu.events.EXIT)

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

        # Player key down
        if event.type == pygame.KEYDOWN:

            # If player presses the ESCAPE key
            if event.key == pygame.K_ESCAPE:
                # menu.close()
                pass

            key_unicode = event.unicode
            if key_unicode in key_map_keydown:
                key_map_keydown[key_unicode]()

        # Player key up
        if event.type == pygame.KEYUP:
            key_unicode = event.unicode
            if key_unicode in key_map_keyup:
                key_map_keyup[key_unicode]()

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