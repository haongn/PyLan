# Bai toan ma di tuan. Ma di het ban co. In ra cac nuoc di do. 

# Backtracking works in an incremental way to attack problems. 

# Chu y: doc ky outline cua TT o cuoi file. Y tuong o het day. Rat de hieu. 

# chessboard size 
n = 8

def isSafe(x, y, board): 
    """This function checks if x, y are valid indexes for N * N chessboard."""
    if (x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):    # this cell is empty
        return True 
    
    return False 

def printSol(n, board): 
    """This function prints chessboard of a solution."""
    for i in range(n): 
        for j in range(n): 
            print('{:6}'.format(board[i][j]), end = '')
        print()

def solveKT(n): 
    """This is the main function."""
    # Initialization of chessboard
    board = [[-1 for i in range(n)] for j in range(n)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # The Knight is initially at the first block
    board[0][0] = 0    # first step   
    pos = 1            # step counter for knight's position

    # Check if solution exists or not: 
    if not recurKT(n, board, 0, 0, move_x, move_y, pos): 
        print('Solution does not exist.')
    else: 
        printSol(n, board)

def recurKT(n, board, curr_x, curr_y, move_x, move_y, pos): 
    """...."""
    # Degenerate case: if the chessboard is all covered
    if pos == n*n: 
        return True 
    
    # a) Try all next moves from the current cordinate x, y     
    for i in range(n): 
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]

        # check if new move is a valid move: 
        if isSafe(new_x, new_y, board):      
            board[new_x][new_y] = pos       # indicate the order of this move

            # recursive step: 
            if recurKT(n, board, new_x, new_y, move_x, move_y, pos + 1): 
                return True      # this will return True only in the degenerate case and propagate to outer functions
                                 # if this happens, the below step will not be executed 
            
            # Backtracking step: this will happen if the above step is False 
            # b) 
            board[new_x][new_y] = -1

    # if all moves tried above dont work, then return False
    # c) If none of the alternatives work then return false 
    return False       



if __name__=='__main__': 
    solveKT(n)

# If all squares are visited 
#     print the solution
# Else
#    a) Add one of the next moves to solution vector and recursively 
#    check if this move leads to a solution. (A Knight can make maximum 
#    eight moves. We choose one of the 8 moves in this step).
#    b) If the move chosen in the above step doesn't lead to a solution
#    then remove this move from the solution vector and try other 
#    alternative moves.
#    c) If none of the alternatives work then return false (Returning false 
#    will remove the previously added item in recursion and if false is 
#    returned by the initial call of recursion then "no solution exists" )