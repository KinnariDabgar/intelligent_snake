import pygame
pygame.init()
clock = pygame.time.Clock()
# display_surface
gd = pygame.display.set_mode((400, 500))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
light_green = (0, 200, 0)
blue = (0, 0, 255)
mint = (102, 255, 204)
t = (0, 51, 153)

background = pygame.image.load("ui_bg.png")


def Message(size, mess, x_pos, y_pos):
    font = pygame.font.SysFont("jokerman", size)
    render = font.render(mess, True, black)
    gd.blit(render, (x_pos, y_pos))


Message(100, "START", 150, 100)
clock.tick(1)


def button(x_button, y_button, mess_b):
   # pygame.draw.rect(gd, t, [x_button, y_button, 80, 30])
    Message(30, mess_b, x_button, y_button)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_button < mouse[0] < x_button+100 and y_button < mouse[1] < y_button+30:
        pygame.draw.rect(gd, white, [x_button, y_button, 66, 38])
        Message(30, mess_b, x_button, y_button)
        if click == (1, 0, 0) and mess_b == "Play":
            import intel_snake
        elif click == (1, 0, 0) and mess_b == "Best":
            import choose_bw_two
        elif click == (1, 0, 0) and mess_b == "Quit":
            pygame.quit()
            quit()


def game_intro():
    intro = False
    while intro == False:
        gd.fill(light_green)
        gd.blit(background, (0, 0))
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
