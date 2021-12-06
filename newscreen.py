import pygame
pygame.init()
#clock = pygame.time.Clock()
screen_height = 500
screen_width = 400
# display_surface
screen = pygame.display.set_mode((screen_width, screen_height))
white = (255, 255, 255)
black = (0, 0, 0)


background = pygame.image.load("ui_bg.png")

# display text on user_interface


def Message(size, mess, x_pos, y_pos):
    font = pygame.font.SysFont("jokerman", size)
    render = font.render(mess, True, black)
    screen.blit(render, (x_pos, y_pos))

# actions of button


def button(x_button, y_button, mess_b):
    Message(30, mess_b, x_button, y_button)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_button < mouse[0] < x_button+100 and y_button < mouse[1] < y_button+30:
        pygame.draw.rect(screen, white, [x_button, y_button, 66, 38])
        Message(30, mess_b, x_button, y_button)
        if click == (1, 0, 0) and mess_b == "Play":
            import intel_snake
        elif click == (1, 0, 0) and mess_b == "Best":
            import choose_bw_two
        elif click == (1, 0, 0) and mess_b == "Quit":
            pygame.quit()
            quit()

# main_function


def game_intro():
    intro = True
    while intro == True:
        screen.blit(background, (0, 0))
        button(170, 330, "Play")
        button(170, 380, "Best")
        button(170, 430, "Quit")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


game_intro()
pygame.quit()
quit()
