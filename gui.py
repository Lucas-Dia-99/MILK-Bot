import pygame
import chess


class Gui():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([400, 400])
        self.pieces = {'p': pygame.transform.scale(pygame.image.load('pieces/black-pawn.png').convert_alpha(), (50, 50)),
                       'n': pygame.transform.scale(pygame.image.load('pieces/black-knight.png').convert_alpha(), (50, 50)),
                       'b': pygame.transform.scale(pygame.image.load('pieces/black-bishop.png').convert_alpha(), (50, 50)),
                       'r': pygame.transform.scale(pygame.image.load('pieces/black-rook.png').convert_alpha(), (50, 50)),
                       'q': pygame.transform.scale(pygame.image.load('pieces/black-queen.png').convert_alpha(), (50, 50)),
                       'k': pygame.transform.scale(pygame.image.load('pieces/black-king.png').convert_alpha(), (50, 50)),
                       'P': pygame.transform.scale(pygame.image.load('pieces/white-pawn.png').convert_alpha(), (50, 50)),
                       'N': pygame.transform.scale(pygame.image.load('pieces/white-knight.png').convert_alpha(), (50, 50)),
                       'B': pygame.transform.scale(pygame.image.load('pieces/white-bishop.png').convert_alpha(), (50, 50)),
                       'R': pygame.transform.scale(pygame.image.load('pieces/white-rook.png').convert_alpha(), (50, 50)),
                       'Q': pygame.transform.scale(pygame.image.load('pieces/white-queen.png').convert_alpha(), (50, 50)),
                       'K': pygame.transform.scale(pygame.image.load('pieces/white-king.png').convert_alpha(), (50, 50)),
                       }

    def create_board(self):
        colors = ["white", "saddlebrown"]
        for r in range(8):
            for c in range(8):
                x1 = r * 50
                y1 = c * 50
                x2 = x1 + 50
                y2 = x2 + 50
                rect = pygame.Rect(x1, y1, x2, y2)
                pygame.draw.rect(self.screen, colors[(r+c) % 2], rect)

    def load_position(self, board: chess.Board):
        self.create_board()
        for i in range(64):
            piece = board.piece_at(i)
            if piece != None:
                self.screen.blit(
                    self.pieces[str(piece)], ((i % 8)*50, 350-(i//8)*50))
        pygame.display.flip()
                    

    def run(self):
        self.create_board()
        board = chess.Board(chess.STARTING_FEN)
        self.load_position(board)
        pygame.display.flip()

