from sudoku_generator_solver import *
import pygame

# RGB Colors Highlighting Cell Being Calculated
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Sudoku:
    def __init__(self, screen):
        self.row = 9
        self.col = 9
        self.dimension = 500
        self.screen = screen
        self.control = erase_cells(create_board())
        self.puzzle = [[self.control[row][col] for row in range(self.row)] for col in range(self.col)]
        self.practice_sheet = [[self.control[row][col] for row in range(self.row)] for col in range(self.col)]

    def visualize_board(self):
        # Refreshing the Screen
        screen.fill(WHITE)
        screen.blit(background, (0, 0))
        screen.blit(title_text, ((70, 20), (500, 20)))
        screen.blit(sub_text, ((660, 570), (660, 570)))

        # Drawing Borders
        for index in range(0, 10):
            if index % 3 == 0:
                thick = 3
            else:
                thick = 1
            pygame.draw.line(self.screen, WHITE, (150, 80 + index * 55.56), (150 + self.dimension, 80 + index * 55.56), thick)
            pygame.draw.line(self.screen, WHITE, (150 + index * 55.56, 80), (150 + index * 55.56, 80 + self.dimension), thick)

        # Drawing Cell Values
        font = pygame.font.SysFont("Papyrus", 30, bold=True)
        for row in range(self.row):
            for col in range(self.col):
                if self.puzzle[row][col] == ' ':
                    color = GREEN
                else:
                    color = WHITE
                text = font.render(str(self.practice_sheet[row][col]), 1, color)
                screen.blit(text, ((170 + row * 55.56, 85 + col * 55.56), (170 + row * 55.56, 85 + col * 55.56)))
        return

    def redraw_cell(self, value, row, col, color):
        # Redrawing Incorrect Guess Values with new Guesses
        font = pygame.font.SysFont("Papyrus", 30, bold=True)
        text = font.render(str(value), 1, color)
        screen.blit(text, ((170 + row * 55.56, 85 + col * 55.56), (170 + row * 55.56, 85 + col * 55.56)))
        return

    def visualize_solving(self):
        # Exact Same Algo as 'solve_sudoku()' with Pygame Visualization Function
        for row in range(len(self.practice_sheet)):
            for column in range(len(self.practice_sheet)):
                if self.practice_sheet[row][column] == ' ':
                    for guess in range(1, 10):
                        if check_guess(guess, row, column, self.practice_sheet):
                            # Refreshing Screen to Prevent Overlap-Printing
                            self.visualize_board()
                            pygame.draw.rect(self.screen, RED, (150 + row * 55.56, 80 + column * 55.56, 55.56, 55.56), 5)
                            pygame.display.update()
                            pygame.time.delay(50)
                            # Visualizing Guess
                            self.practice_sheet[row][column] = guess
                            self.redraw_cell(guess, row, column, GREEN)
                            pygame.display.update()
                            pygame.time.delay(50)
                            # Backtracking Recursion Implementation
                            if self.visualize_solving():
                                return True
                            self.practice_sheet[row][column] = ' '
                            # Visualizing Backtracking Recursion
                            self.visualize_board()
                            pygame.draw.rect(self.screen, RED, (150 + row * 55.56, 80 + column * 55.56, 55.56, 55.56), 5)
                            pygame.display.update()
                            pygame.time.delay(50)
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
    my_board = Sudoku(screen)
    running = True
    while running:
        screen.fill(WHITE)
        screen.blit(background, (0, 0))
        # Title
        font = pygame.font.SysFont("Papyrus", 35)
        title_text = font.render(str('Sudoku Backtracking Algorithm Visualizer'), 1, WHITE)
        screen.blit(title_text, ((70, 20), (500, 20)))
        # Instruction Print
        font = pygame.font.SysFont("comicsans", 18)
        sub_text = font.render(str('Press SPACE to Solve!'), 1, WHITE)
        screen.blit(sub_text, ((655, 570), (655, 570)))
        # Board Print
        my_board.visualize_board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                # Press SPACE to Solve Sudoku
                if event.key == pygame.K_SPACE:
                    my_board.visualize_solving()
        pygame.display.update()

