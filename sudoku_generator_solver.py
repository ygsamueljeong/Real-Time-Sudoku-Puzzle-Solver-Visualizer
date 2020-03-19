import random

def create_board():
    board = []
    # Create 1 Root Row
    new_row = random.sample(range(1, 10), 9)
    board.append(new_row)
    while board:
        # Next Row = Shift 3 Spaces of the 1st Row
        new_row = new_row[3:] + new_row[:3]
        board.append(new_row)
        # Next Row = Shift 3 Spaces of the 2nd Row
        new_row = new_row[3:] + new_row[:3]
        board.append(new_row)
        # Break When 9 Rows are Filled in 'board'
        if len(board) == 9:
            break
        # Next Row = Shift 1 Space of the 3rd Row
        new_row = new_row[1:] + new_row[:1]
        board.append(new_row)
    return board

def erase_cells(board):
    # Erase 54 Cells to Create Puzzle
    empty_num = 0
    while empty_num < 54:
        row = random.randint(0, 8)
        column = random.randint(0, 8)
        if board[row][column] != ' ':
            board[row][column] = ' '
            empty_num += 1
    return board

def check_guess(guess, row_index, col_index, board):
    # Row & Column Check
    row = board[row_index]
    column = list(board[i][col_index] for i in range(0, 9))
    if guess in row or guess in column:
        return False
    # Block Check (Specifically Designed for 9 x 9 Sudo
    block_row = (row_index // 3) * 3
    block_col = (col_index // 3) * 3
    for row in range(block_row, block_row + 3):
        for column in range(block_col, block_col + 3):
            if board[row][column] == guess:
                return False
    return True

def solve_sudoku(puzzle):
    # Searching for Empty Cells
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
