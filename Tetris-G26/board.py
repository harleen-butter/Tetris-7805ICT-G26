import pygame

pygame.font.init()

TITLE_FONT = pygame.font.Font('fonts/CHABUL.ttf', 65)
SCORE_FONT = pygame.font.Font('fonts/LeagueMono-Bold.ttf', 23)

BACKGROUND_COLOR = (132, 149, 117)
FRAME_COLOR = (19, 21, 17)
TEXT_COLOR = (19, 21, 17)


class Board:
    def __init__(self, width, height, block_size, box_width, box_height):
        self.screen_width = width
        self.screen_height = height
        self.block_size = block_size
        self.box_width = box_width
        self.box_height = box_height
        self.start_x = (width - box_width) // 2
        self.start_y = (height - box_height) - 30

    def draw_window(self, surface, grid, draw_grid):
        surface.fill(BACKGROUND_COLOR)

        # draw title over the box
        title = SCORE_FONT.render('TETRIS - Group 26', True, TEXT_COLOR)
        surface.blit(title, (
        self.start_x + self.box_width / 2 - (title.get_width() / 2), self.start_y / 2 - title.get_height() / 2))

        # draw each brick
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(surface, grid[i][j],
                                 (self.start_x + j * self.block_size, self.start_y + i * self.block_size,
                                  self.block_size, self.block_size), 0)

        # draw border of box
        pygame.draw.rect(surface, FRAME_COLOR, (self.start_x, self.start_y, self.box_width, self.box_height), 5)

        draw_grid(surface, grid, self.start_x, self.start_y, self.block_size, self.box_width, self.box_height)

    def draw_next_shape(self, shape, surface, score, get_max_score, format_timer, speed_level, level, max_combo):
        # draw preview next block
        text = SCORE_FONT.render('Next Block', True, TEXT_COLOR)

        preview_x = self.start_x + self.box_width + 50
        preview_y = self.start_y + self.box_height / 2 - 100
        surface.blit(text, (preview_x + 4 * self.block_size - text.get_width() / 2, preview_y - 80 - self.block_size))
        formatted = shape.shape[shape.rotation % len(shape.shape)]

        # draw score
        label = SCORE_FONT.render(f'SCORE: {score}', True, TEXT_COLOR)
        surface.blit(label, (self.start_x / 2 - label.get_width() / 2, preview_y - 80 - self.block_size))

        # draw speed value
        label = SCORE_FONT.render(f'MODE: Player', True, TEXT_COLOR)
        surface.blit(label, (self.start_x / 2 - label.get_width() / 2, preview_y + 30))

        # draw combo
        label = SCORE_FONT.render(f'LEVEL: {1}', True, TEXT_COLOR)
        surface.blit(label, (self.start_x / 2 - label.get_width() / 2, preview_y + 170))

        # max combo
        label = SCORE_FONT.render(f'GAME: Normal', True, TEXT_COLOR)
        surface.blit(label, (self.start_x / 2 - label.get_width() / 2, preview_y + 100))

        for i, row in enumerate(formatted):
            for j, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(surface, shape.color,
                                     (preview_x + (j + 1.5) * self.block_size, preview_y + (i - 1) * self.block_size,
                                      self.block_size, self.block_size), 0)
        # draw horizontal borders
        pygame.draw.line(surface, FRAME_COLOR, (preview_x + 1.5 * self.block_size, preview_y - 2 * self.block_size),
                         (preview_x + 6.5 * self.block_size, preview_y - 2 * self.block_size), width=3)
        pygame.draw.line(surface, FRAME_COLOR, (preview_x + 1.5 * self.block_size, preview_y + 4 * self.block_size),
                         (preview_x + 6.5 * self.block_size, preview_y + 4 * self.block_size), width=3)
        # draw vertical borders
        pygame.draw.line(surface, FRAME_COLOR, (preview_x + 1.5 * self.block_size, preview_y - 2 * self.block_size),
                         (preview_x + 1.5 * self.block_size, preview_y + 4 * self.block_size), width=3)
        pygame.draw.line(surface, FRAME_COLOR, (preview_x + 6.5 * self.block_size, preview_y - 2 * self.block_size),
                         (preview_x + 6.5 * self.block_size, preview_y + 4 * self.block_size), width=3)
