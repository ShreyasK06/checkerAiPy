import pygame
import asyncio
from CheckersAI.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from CheckersAI.game import Game
from CheckersAI.minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
depth = 3


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


async def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), depth, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            if game.winner() == (255, 255, 255):
                print("OH NO YOU LOST")
                run = False
            else:
                print('GOOD JOB YOU HAVE BEAT THE AI')
                run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    await asyncio.sleep(0)
    pygame.quit()


asyncio.run(main())
