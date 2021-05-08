# Sudoku-Generator-Solver-Backtracking-Algo-Visualizer
Coding project with a unique backtracking algorithm visualizer

Objective: 
Practicing fundamental python development skills, mathematical sequence implementations, and Python GUI.

Mechanics: 
--> Create sudoku puzzles and avoid brute force methods
--> Implement backtracking algorithm to solve the puzzle which significantly reduces computation time and required power
--> Visualize the backtracking algorithm with Pygames

a.) sudoku_generator_solver.py -- generate a Sudoku Puzzle and backtracking algorithm solver
  
  1. def create_board(id1, id2) 
      --> Create a sudoku board by randomly creating a row of unique numbers between 1 and 9
      --> Repeat the Process Below Until 9 Rows are Created:
        Step 1: Shift 3 spaces of the row above and append
        Step 2: Again, shift 3 spaces of the row above and append
        Step 3: Shift 1 space of the row above and append and repeat back from Step 1
      --> This mathematical solution above avoids "brute force" coding
  
  2. def erase_cells(board) 
      --> Randomly erases 54 cells from the created_board by utilizing random.randint to choose indexes
      
  3. def check_guess(guess, row_index, col_index, board):
      --> Check the guess if the located row or col contains the same value
      --> Check the guess if the located sub-block contains the same value
      Click link below for basic Sudoku rules
      https://www.nikoli.co.jp/iphone/en/sd_tutorial.html
      
  4. def solve_sudoku(puzzle) -- Backtracking Algorithm
      --> Reads through every cell of the puzzle and identifies empty cells
      --> Test every number between 1 and 9 (included) and check the guess with created function above
      --> Implement recursion using if/else/return method of python definition function
          Step 1- Generate an acceptable guess and permanantly write the guess on the puzzle. Thus a new                     
                  puzzle is created with 1 less empty space than its predecessor.
          Step 2- Re-run solve_sudoku() to solve the "new" puzzle
          Step 3- If all number between 1 and 9 do not pass the check_guess() function, return to the       
                  previous puzzle and test for another guess
          Step 4- Run this algorithm on loop until all cells are correctly filled.
          
    Searching for Empty Cells
    for row in range(len(puzzle)):
        for column in range(len(puzzle)):
            if puzzle[row][column] == ' ':
                # Guessing with Every Possible Digit: 1 to 9
                for guess in range(1, 10):
                    # Eliminate Possibilities with Row/Column/Block Check
                    if check_guess(guess, row, column, puzzle):
                        puzzle[row][column] = guess
                        # Implement Recursion: Backtracking Algorithm
                        if solve_sudoku(puzzle):
                            return True
                        # Undoing Incorrect Guess Placements
                        puzzle[row][column] = ' '
                # If All Guesses Fail = Previous Cell Contains Wrong Guess Value
                return False
    # Ending When Cell or Puzzle Board Completes
    return True
         
c.) sudoku_main.py -- Visualizing
   
   1. Class Sudoku:
      --> Initialize and establish number of rows, cols, and dimension for pygames
      --> self.control = original puzzle that is only used for answer comparision and index matching
      --> self.puzzle = final solution board which the function returns to visualize
      --> self.practice_sheet = puzzle board where the algorithm tests out guesses
      *** 3 boards were created in purpose of avoiding errors during pygame visualization
          
   2. def visualize_board() -- pygames
      --> Visualizing the board, drawing lines, boards, and adjusting details of thickness, window dimension, and colors
   
   3. def redraw_cell() -- pygames
      --> Write a conditionally acceptable guess on an empty cell and on a refreshed window
      --> Designed to write over incorrect guesses 

   4. visualize_solving() -- pygames
      --> Same exact algorithm as solve_sudoku.py
      --> Refreshes pygame screen when a new guess is made or erased
      --> Highlights (red) the cell in which the program tests on 
      --> Delayed the displaying time because the algorithm solves too quickly
   
   5. if __name__ == '__main__':
      --> Press Space to Start Algorithm Visualization
   
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
        # Title Print
        screen.fill(WHITE)
        screen.blit(background, (0, 0))
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

d.) sudoku_background.png -- legally free background picture downloaded for pygames screen
e.) sudoku_icon.png -- legally free icon downloaded for pygames screen tab
      
      
      
