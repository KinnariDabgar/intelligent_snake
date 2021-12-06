import pygame
import math
import button
import time

screen_height = 500
screen_width = 625
END = (380, 300)
score = 0
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont("comicsansms", 26)
score_X = 480
score_Y = 445
DIRECTIONS = [[10, 0], [0, 10], [-10, 0],  [0, -10]]
BLOCKED_CELLS = [  # first block
    (60, 50), (50, 50), (40, 50), (30, 50), (20, 50), (70, 50),
    (80, 50), (90, 50), (100, 50), (100, 50), (100, 50), (100, 60),
    (100, 70), (100, 80), (100, 90), (100, 100), (100, 110), (100, 120),
    (60, 250), (50, 250), (40, 250), (30, 250), (20, 250), (10, 250),
    # Second Block
    (0, 250), (70, 250), (80, 250), (90, 250), (100,
                                                250), (110, 250), (120, 250), (130, 250),
    (140, 250), (150, 250), (160, 250), (170, 250), (180,
                                                     250), (190, 250), (200, 250), (210, 250),
    # Vertical Line
    (210, 230), (210, 240),
    # Third Block
    (420, 40), (420, 50), (420, 60), (420, 70), (420, 80), (420, 90),
    (420, 100), (420, 110), (420, 120), (420, 130), (420, 140), (420, 150),
    (420, 160), (420, 170), (420, 180), (420, 190), (420, 200),
    (420, 210), (420, 220), (420, 230), (420, 240), (420, 250),
    # Horizontal Line
    (300, 140), (310, 140), (320, 140), (330, 140),
    (340, 140), (350, 140), (360, 140), (370, 140),
    (380, 140), (390, 140), (400, 140), (410, 140), (420, 140),
    # last block
    (260, 340), (270, 340), (280, 340), (290, 340), (300, 340),
    (310, 340), (320, 340), (330, 340), (340,
                                         340), (350, 340), (360, 340), (370, 340),
    (380, 340), (390, 340), (400, 340), (410,
                                         340), (420, 340), (430, 340), (440, 340),
    (450, 340), (460, 340), (470, 340), (480,
                                         340), (490, 340), (500, 340), (510, 340),
    (520, 340), (530, 340), (540, 340), (550,
                                         340), (560, 340), (570, 340), (580, 340),
    (590, 340), (600, 340), (610, 340), (620, 340), (625, 340)]
snake = [(0, 0), (10, 0), (20, 0), (30, 0)]
START = snake[3]
snake_w = 10
snake_h = 10
direction = ''
fps = 10
snake_move = False
step = 0
dest = False

background = pygame.image.load("game_bg.jpeg")
exit_img = pygame.image.load('exit.png').convert_alpha()

exit_button = button.Button(270, 450, exit_img, 0.5)


def nearest(num):
    if abs(math.floor(num / 10) - num / 10) < abs(math.ceil(num / 10) - num / 10):
        return math.floor(num / 10) * 10
    else:
        return math.ceil(num / 10) * 10


class Node:

    def __init__(self, current_pos, previous_pos, g, h):
        self.current_pos = current_pos
        self.previous_pos = previous_pos
        self.h = h
        self.g = g

    def f(self):
        return self.h + self.g


def heuristic_cost(node_pos):
    cost = abs(node_pos[0] - END[0]) + abs(node_pos[1] - END[1])
    return (cost / 10)


def get_best_node(open_set):
    firstEnter = True

    for node in open_set.values():
        if firstEnter or node.f() < bestF:
            firstEnter = False
            bestNode = node
            bestF = bestNode.f()
    return bestNode


def get_adjacent_node(node):
    list_of_node = []

    for dir in DIRECTIONS:
        new_pos = (node.current_pos[0] + dir[0], node.current_pos[1] + dir[1])
        if 0 <= new_pos[0] <= 621 and 0 <= new_pos[1] <= 499:
            list_of_node.append(
                Node(new_pos, node.current_pos, node.g + 1, heuristic_cost(new_pos)))

    return list_of_node


def min_path(closed_set):
    path = []
    node = closed_set[str(END)]
    while node.current_pos != START:
        path.insert(0, node.current_pos)
        node = closed_set[str(node.previous_pos)]
    return path


def is_blocked(node):
    blocked = False
    if node.current_pos in BLOCKED_CELLS:
        blocked = True
    return blocked


def show_score(x, y):
    score_value = font.render("Score : " + str(score),
                              True, (128, 0, 0))
    screen.blit(score_value, (x, y))


def gameover():

    # creating font object my_font
    my_font = pygame.font.SysFont('jokerman', 40)
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render('Game Over', True, (128, 0, 0))
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
    # setting position of the text
    game_over_rect.midtop = (screen_width/2, screen_height/2.5)
    # blit wil draw the text on screen
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


def main(start_pos):
    open_set = {str(start_pos): Node(
        start_pos, start_pos, 0, heuristic_cost(start_pos))}
    closed_set = {}

    while True:
        test_node = get_best_node(open_set)
        closed_set[str(test_node.current_pos)] = test_node

        if test_node.current_pos == END:
            return min_path(closed_set)

        adj_node = get_adjacent_node(test_node)

        for node in adj_node:
            if is_blocked(node) or str(node.current_pos) in closed_set.keys() or str(
                node.current_pos) in open_set.keys() and open_set[
                    str(node.current_pos)].f() < node.f():
                continue
            open_set[str(node.current_pos)] = node
        del open_set[str(test_node.current_pos)]


# initiate pygame module--- required
pygame.init()

# screen
pygame.display.set_caption('Intelligent Snake')
running = True

# clock
clock = pygame.time.Clock()

# main loop
while running:
    # key event
    for event in pygame.event.get():
        # closing events
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = event.pos
                new_pos_x = nearest(pos[0])
                new_pos_y = nearest(pos[1])
                if (new_pos_x, new_pos_y) not in BLOCKED_CELLS:
                    if(new_pos_x, new_pos_y) in snake:
                        gameover()
                    snake_move = True
                    END = (new_pos_x, new_pos_y)
                    START = snake[3]
                    path = main(START)
                    step = 0
                    dest = True

    if snake_move:
        snake.append(path[step])
        snake.pop(0)
        if snake[3] != END:
            step += 1
        else:
            snake_move = False
            score += 1
            print("Score:", score)

    screen.blit(background, (0, 0))
    if exit_button.draw(screen):
        print("exit")
        pygame.quit()
        quit()

        # create a text surface object,
        # on which text is drawn on it.
    if dest:
        screen.blit(pygame.image.load('apple.png'),
                    [END[0], END[1], 10, 10])
    # blocked draw
    for b in BLOCKED_CELLS:
        pygame.draw.rect(screen, (0, 0, 0), [b[0], b[1], 10, 10])

    # rectangle draw
    for pos in range(len(snake)):
        if pos < 3:
            pygame.draw.rect(screen, (0, 0, 255), [
                             snake[pos][0], snake[pos][1], snake_w, snake_h])
        else:
            pygame.draw.rect(screen, (255, 0, 255), [
                             snake[pos][0], snake[pos][1], snake_w, snake_h])

    show_score(score_X, score_Y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()
