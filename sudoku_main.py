from sudoku_generator_solver import *
import pygame

# RGB Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Sudoku:
    def __init__(self, row, col, dimension, screen):
        self.row = row
        self.col = col
        self.dimension = dimension
        self.screen = screen
        self.board = erase_cells(create_board())
        self.puzzle = [[self.board[i][j] for i in range(self.row)] for j in range(self.col)]
        self.practice_sheet = [[self.board[i][j] for i in range(self.row)] for j in range(self.col)]

    def visualize_puzzle(self):
        # Visualizing the Board
        for pos in range(0, 10):
            if pos % 3 == 0:
                thick = 3
            else:
                thick = 1
            pygame.draw.line(self.screen, WHITE, (150, pos*55.56+80), (self.dimension+150, pos*55.56+80), thick)
            pygame.draw.line(self.screen, WHITE, (pos*55.56+150, 80), (pos*55.56+150, self.dimension+80), thick)
        # Visualizing Cell Values
        font = pygame.font.SysFont("Papyrus", 30, bold=True)
        for row in range(0, self.row):
            for col in range(0, self.col):
                if self.puzzle[row][col] == ' ':
                    color = GREEN
                else:
                    color = WHITE
                text = font.render(str(self.practice_sheet[row][col]), 1, color)
                screen.blit(text, ((170+row*55, col*55.56+85), (170+row*55.56, col*55.56+85)))
        return

    def redraw_cell(self, value, row, col, color):
        font = pygame.font.SysFont("Papyrus", 30, bold=True)
        text = font.render(str(value), 1, color)
        screen.blit(text, ((170 + row * 55, col * 55.56 + 85), (170 + row * 55, col * 55.56 + 85)))
        return

    def visualize_solve_sudoku(self):
        for row in range(len(self.practice_sheet)):
            for column in range(len(self.practice_sheet)):
                if self.practice_sheet[row][column] == ' ':
                    for guess in range(1, 10):
                        if check_guess(guess, row, column, self.practice_sheet):
                            self.practice_sheet[row][column] = guess
                            self.redraw_cell(guess, row, column, GREEN)
                            pygame.display.update()
                            pygame.time.delay(120)
                            if self.visualize_solve_sudoku():
                                return True
                            self.practice_sheet[row][column] = ' '
                            # Refreshing Screen to Prevent Overlap Printing
                            screen.fill(WHITE)
                            screen.blit(background, (0, 0))
                            screen.blit(title_text, ((70, 20), (500, 20)))
                            screen.blit(sub_text, ((660, 570), (660, 570)))
                            self.visualize_puzzle()
                            pygame.display.update()
                            pygame.time.delay(120)
                    return False
        return True

# Main Function
if __name__ == '__main__':
    # Initialize
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Sudoku Game')
    background = pygame.image.load('sudoku_background.png')
    icon = pygame.image.load('sudoku_icon.png')
    pygame.display.set_icon(icon)

    # Run Visualizer
    board = Sudoku(9, 9, 500, screen)
    running = True
    while running:
        screen.fill(WHITE)
        screen.blit(background, (0, 0))
        # Title Print
        font = pygame.font.SysFont("Papyrus", 35)
        title_text = font.render(str('Sudoku Backtracking Algorithm Visualizer'), 1, WHITE)
        screen.blit(title_text, ((70, 20), (500, 20)))
        # Instruction Print
        font = pygame.font.SysFont("comicsans", 18)
        sub_text = font.render(str('Press SPACE to Solve!'), 1, WHITE)
        screen.blit(sub_text, ((655, 570), (655, 570)))
        # Board Print
        board.visualize_puzzle()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    board.visualize_solve_sudoku()
        pygame.display.update()

