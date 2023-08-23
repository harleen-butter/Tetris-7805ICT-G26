import pygame
import csv
import sys
from board import TITLE_FONT, SCORE_FONT, BACKGROUND_COLOR, TEXT_COLOR
from menu import ACTIVE_COLOR


def draw_configure(win, leaderboard, width, height):
    menu_text = TITLE_FONT.render('CONFIGURE', True, TEXT_COLOR)
    win.blit(menu_text, (width / 2 - menu_text.get_width() / 2, height / 2 - 350))

    width_btn = -450
    height_btn = -100
    for i, v in enumerate(leaderboard):
        for index, j in enumerate(v):
            # draw title row
            if i == 0:
                label = SCORE_FONT.render(j, True, ACTIVE_COLOR)
                button_x = width / 2 - label.get_width() / 2
                win.blit(label, (button_x + width_btn, height / 3 - 100))
            else:
                # draw score and time
                label = SCORE_FONT.render(j, True, TEXT_COLOR)
                button_x = width / 2 - label.get_width() / 2
                win.blit(label, (button_x + width_btn, height / 3 + height_btn))
            width_btn += 150
        width_btn = -300
        height_btn += 50


def get_configure(win, width, height):
    rows = [['', 'SETTINGS']]
    with open('configure.csv') as f:
        f.seek(0)
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            rows.append(row)
    try:
        leaderboard = [rows[0]] + sorted(rows[1:], key=lambda x: str(x[1]))
    except:
        leaderboard = [rows[0]]

    high_scores = True

    while high_scores:
        win.fill(BACKGROUND_COLOR)
        draw_configure(win, leaderboard, width, height)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    high_scores = False
