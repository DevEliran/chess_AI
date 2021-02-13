import pygame

BOARD_LENGTH = 8
SQUARE_SIZE = 80
DISPLAY_SIZE = (800, 600)
SURFACE_SIZE = (SQUARE_SIZE * BOARD_LENGTH, SQUARE_SIZE * BOARD_LENGTH)
P1_COLOR = (255, 255, 255)
P2_COLOR = (0, 0, 0)
BOARD_TITLE = 'Chess'


class Board(object):
    def __init__(self):
        self.colors = {0: P1_COLOR, 1: P2_COLOR}
        self._exit = False
        pygame.init()

        self.display = pygame.display.set_mode(SURFACE_SIZE)
        self.board = pygame.Surface(SURFACE_SIZE)
        pygame.display.set_caption(BOARD_TITLE)

        self.board.fill(P1_COLOR)

        while not self._exit:
            self.display.blit(self.board, self.board.get_rect())
            self.draw_board()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(True)

    def draw_board(self):
        for file in range(0, BOARD_LENGTH):
            for rank in range(0, BOARD_LENGTH):
                color = self.colors[(file+rank) % 2]
                pygame.draw.rect(self.board, color,
                                 (file * SQUARE_SIZE, rank * SQUARE_SIZE,
                                  SQUARE_SIZE, SQUARE_SIZE))

    @property
    def exit(self):
        return self._exit

    @exit.setter
    def exit(self, exit):
        self._exit = exit


