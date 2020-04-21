# Sudoku-Generator-Solver-Backtracking-Algo-Visualizer
Coding project with a unique backtracking algorithm visualizer

Objective: 
Practicing fundamental python development skills and mathematical implementations.

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
          Step 1: Generate an acceptable guess and permanantly write the guess on the puzzle. Thus a new                     puzzle is created with 1 less empty space than its predecessor.
          Step 2: Re-run solve_sudoku() to solve the "new" puzzle
          Step 3: If all number between 1 and 9 do not pass the check_guess() function, return to the       
                  previous puzzle and test for another guess
          Step 4: Run this algorithm on loop until all cells are correctly filled.
          
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
         
c.) sudoku_main.py -- Visualizing
   
   1. def buy()
      --> Executes created functions in forecast_library.py in the following order:
      *** def importing_twitdata(id1, id2) 
      *** def twit_sentiment_analyzer(raw_data)
      *** For each candidate stock, the bot avoids buying stocks already in position, calculates number of shares to buy
      *** qty_desired = round(((target_price - current_price) / current_price) * buying_power)
      *** Checks if the portfolio can afford to make an order
      *** Store buy history and target prices in a text file.
          
   2. def sell()
       --> If position has more than -7.5% loss or Unrealized Gain > Target Price, the bot orders an immediate sell order on market price
       --> Else, the bot pushes stop/limit order: 
           limit order = newly updated target price  
           stop limit = -7.5% of purchased price

    3. if __name__ == '__main__':
    # Account Status Review
    alpaca_api = tradeapi.REST(base_url=ALPACA_BASE_URL,
                        key_id=ALPACA_API_KEY,
                        secret_key=ALPACA_SECRET_KEY
                        )
    # Liquidity
    buying_power = float(alpaca_api.get_account().buying_power)

    # Current Holding Positions
    open_positions = alpaca_api.list_positions()
    my_positions = set(map(lambda index: open_positions[index].symbol, range(len(open_positions))))

    # Open Orders
    open_orders = alpaca_api.list_orders(status='open')
    my_orders = set(map(lambda index: open_orders[index].symbol, range(len(open_orders))))

    # Executing Sell & Buy Orders
    sell()
    buy()
    sys.exit()
