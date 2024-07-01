import pygame as pg
from pygame.locals import *
from random import randint
from time import sleep

pg.init()
pg.font.init()

SCREEN_WIDTH: int = 640
SCREEN_HEIGHT: int = 480

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Pongo!")

text_font = pg.font.SysFont('Comic Sans MS', 15)
winner_font = pg.font.SysFont('Comic Sans MS', 40)

x: int = int(SCREEN_WIDTH / 2)
y: int = int(SCREEN_HEIGHT / 2)

is_collided: bool = False

# == Player configs. ==
# Player 1
x_player1: int = SCREEN_WIDTH - 40
y_player1: int = int(SCREEN_HEIGHT / 2) - 30

# Player 2
x_player2: int = 40
y_player2: int = int(SCREEN_HEIGHT / 2) - 30

MOVEMENT_VALUE = 10
ball_velocity = 3
player_have_ball = 1

player1_points: int = 0
player2_points: int = 0

running: bool = True

cock = pg.time.Clock()
fps = 120

while running:
    #pg.time.delay(5)
    cock.tick(fps)

    screen.fill((0, 0, 0))

    pg.draw.rect(screen, (255, 255, 255), [0, 0, SCREEN_WIDTH, 30])
    pg.draw.rect(screen, (255, 255, 255), [0, SCREEN_HEIGHT - 30, SCREEN_WIDTH, SCREEN_HEIGHT])

    for i in range(16):
        pg.draw.rect(screen, (255, 255, 255), [int(SCREEN_WIDTH / 2) - 10, 40 + (i * 25), 7, 15])

    #pg.draw.rect(screen, (255, 255, 255), [int(SCREEN_WIDTH / 2) - 10, 50, 20, 20])

    solo_pongo_text = text_font.render("P O N G O", False, (0, 0, 0))
    player1_points_text = text_font.render(f"Points: {player1_points}", False, (0, 0, 0))
    player2_points_text = text_font.render(f"Points: {player2_points}", False, (0, 0, 0))

    screen.blit(player1_points_text, (SCREEN_WIDTH - 90, 5))
    screen.blit(player2_points_text, (30, 5))
    screen.blit(solo_pongo_text, (SCREEN_WIDTH - 360, 5))

    for event in pg.event.get():
        keys = pg.key.get_pressed()

        # Player 1 Controls
        if keys[pg.K_u] and y_player1 != 30:
            y_player1 -= MOVEMENT_VALUE
        if keys[pg.K_j] and y_player1 != SCREEN_HEIGHT - 110:
            y_player1 += MOVEMENT_VALUE

        # Player 2 Controls
        if keys[pg.K_w] and y_player2 != 30:
            y_player2 -= MOVEMENT_VALUE
        if keys[pg.K_s] and y_player2 != SCREEN_HEIGHT - 110:
            y_player2 += MOVEMENT_VALUE

        if event.type == QUIT:
            running = False

    player1 = pg.Rect(x_player1, y_player1, 15, 80)
    player2 = pg.Rect(x_player2, y_player2, 15, 80)
    ball = pg.Rect(x, y, 25, 25)

    pg.draw.rect(screen, (255, 255, 255), player1)
    pg.draw.rect(screen, (255, 255, 255), player2)
    pg.draw.rect(screen, (255, 255, 255), ball)
    
    # Ball collision
    if SCREEN_WIDTH <= x >= SCREEN_WIDTH + 40:
        x = int(SCREEN_WIDTH / 2)
        y = int(SCREEN_HEIGHT / 2)

        player2_points += 1

        is_collided = False

        winner_text = winner_font.render(f"PLAYER {player_have_ball} WINS!", False, (255, 255, 255))
        screen.blit(winner_text, (int(SCREEN_WIDTH / 2) - 150, int(SCREEN_HEIGHT / 2) - 30))
        pg.display.update()

        player_have_ball = 1

        sleep(5)

        y_player1 = int(SCREEN_HEIGHT / 2) - 30
        y_player2 = int(SCREEN_HEIGHT / 2) - 30
    
    if x == -40:
        x = int(SCREEN_WIDTH / 2)
        y = int(SCREEN_HEIGHT / 2)

        player1_points += 1

        is_collided = False

        winner_text = winner_font.render(f"PLAYER {player_have_ball} WINS!", False, (255, 255, 255))
        screen.blit(winner_text, (int(SCREEN_WIDTH / 2) - 150, int(SCREEN_HEIGHT / 2) - 30))
        pg.display.update()

        player_have_ball = 1

        sleep(5)

        y_player1 = int(SCREEN_HEIGHT / 2) - 30
        y_player2 = int(SCREEN_HEIGHT / 2) - 30

    if player_have_ball == 1:
        x += ball_velocity
    else:
        x -= ball_velocity

    if player1.colliderect(ball) and not is_collided:
        is_collided = True
        player_have_ball = 2
        y = randint(60, SCREEN_HEIGHT - 60)

    elif player2.colliderect(ball) and is_collided:
        is_collided = False
        player_have_ball = 1
        y = randint(60, SCREEN_HEIGHT - 60)

    pg.display.update()

pg.quit()