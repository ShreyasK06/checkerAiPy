import asyncio

import pygame

from CheckersAI.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from CheckersAI.game import Game
from CheckersAI.minimax.algorithm import minimax

FPS = 60

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
depth = 3


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def draw_result(win, text):
    font = pygame.font.SysFont(None, 56)
    small = pygame.font.SysFont(None, 28)
    band = pygame.Surface((WIDTH, 120), pygame.SRCALPHA)
    band.fill((0, 0, 0, 190))
    win.blit(band, (0, HEIGHT // 2 - 60))
    title = font.render(text, True, (255, 255, 255))
    hint = small.render('Click anywhere to play again', True, (200, 200, 200))
    win.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 12)))
    win.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 28)))
    pygame.display.update()


# The loop yields to the browser every frame (await asyncio.sleep(0)) so the
# same file runs natively and when compiled to WebAssembly with pygbag.
async def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    result = None

    while run:
        clock.tick(FPS)

        if result is None and game.turn == WHITE:
            value, new_board = minimax(game.get_board(), depth, WHITE, game)
            game.ai_move(new_board)

        if result is None and game.winner() is not None:
            result = 'You lost' if game.winner() == WHITE else 'You beat the AI'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if result is not None:
                    game.reset()
                    result = None
                else:
                    row, col = get_row_col_from_mouse(pygame.mouse.get_pos())
                    game.select(row, col)

        game.update()
        if result is not None:
            draw_result(WIN, result)
        await asyncio.sleep(0)

    pygame.quit()


asyncio.run(main())
