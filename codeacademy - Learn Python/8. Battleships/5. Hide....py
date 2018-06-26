from random import randint 

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

def random_row(board_in):
  row = randint(0, len(board_in) - 1)
  return row
random_row(board)
def random_col(board_in):
  col = randint(0, len(board_in) - 1)
  return col
random_col(board)
