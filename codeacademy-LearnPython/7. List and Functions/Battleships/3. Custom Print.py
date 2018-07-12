#THE second for loop in the print_board function iteerates through
#each row in board and print it to the screen
board = []
for i in range(5):
  board.append(['O'] * 5)
def print_board(board_in):
  for row in board:
    print (row)
 
print_board(board)

  
