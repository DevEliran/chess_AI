import pygame
import os
from Pieces import *
BOARD_LENGTH = 8
SQUARE_SIZE = 80
DISPLAY_SIZE = (800, 600)
SURFACE_SIZE = (SQUARE_SIZE * BOARD_LENGTH, SQUARE_SIZE * BOARD_LENGTH)
P1_COLOR = (232, 235, 239)
P2_COLOR = (125, 135, 150)
BOARD_TITLE = 'Chess'
STARTING_POSITION = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                     ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
                     ['-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-'],
                     ['-', '-', '-', '-', '-', '-', '-', '-'],
                     ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
                     ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]


class Board(object):
    def __init__(self):
        self.black_pieces = []
        self.white_pieces = []
        self.images = {}
        self.colors = {0: P1_COLOR, 1: P2_COLOR}
        self._exit = False
        pygame.init()

        self.display = pygame.display.set_mode(SURFACE_SIZE)
        self.board = pygame.Surface(SURFACE_SIZE)
        pygame.display.set_caption(BOARD_TITLE)

        self.board.fill(P1_COLOR)
        self.load_pieces()

        while not self._exit:
            self.display.blit(self.board, self.board.get_rect())
            self.draw_board()
            self.draw_pieces()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(True)

    def load_pieces(self):
        curr_path = os.path.dirname('Board.py')
        image_path = os.path.join(curr_path, 'assets')
        pieces = [file.split('.')[0] for file in os.listdir('./assets')]
        for piece in pieces:
            image = os.path.join(image_path, piece + '.png')
            self.images[piece] = pygame.transform.scale(pygame.image.load(image),
                                                        (SQUARE_SIZE,
                                                         SQUARE_SIZE))

    def draw_board(self):
        for file in range(BOARD_LENGTH):
            for rank in range(BOARD_LENGTH):
                color = self.colors[(file+rank) % 2]
                pygame.draw.rect(self.board, color,
                                 (file * SQUARE_SIZE, rank * SQUARE_SIZE,
                                  SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self):
        for file in range(BOARD_LENGTH):
            for rank in range(BOARD_LENGTH):
                piece = STARTING_POSITION[rank][file]
                if piece != '-':
                    self.board.blit(self.images[piece],
                                    pygame.Rect(file * SQUARE_SIZE,
                                                rank * SQUARE_SIZE, SQUARE_SIZE,
                                                SQUARE_SIZE))

    @property
    def exit(self):
        return self._exit

    @exit.setter
    def exit(self, exit):
        self._exit = exit


