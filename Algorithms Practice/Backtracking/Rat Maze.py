# Level: Medium 
# Given N*N maze, a rat starts at maze[0][0] and need to go to maze[N-1][N-1].
# The rat can move only in two directions: forward and down. 
# In the maze matrix, 0 means a dead end, and 1 means the block can be used in the path. 

N = 4 

def printSol(sol): 
    """This function prints the output maze to the screen."""
    for i in sol: 
        for j in i: 
            print('{:6}'.format(j), end = '')
        print()


def isSafe(maze, x, y): 
    """This function checks if maze[x][y] is a valid move."""
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1: 
        return True 

    return False 


def solveMaze(maze, N):
    """..."""
    # Create a N * N maze solution
    sol = [[0 for j in range(N)] for i in range(N)]
    
    if recurMaze(maze, 0, 0, sol) == False: 
        print('Solution doesnt exist.')
    else: 
        print('Solution exists:')
        printSol(sol)


def recurMaze(maze, x, y, sol): 
    """This is the recursion and backtracking function."""
    # Degenerate case: 
    if x == N - 1 and y == N - 1 and maze[x][y] == 1:   # if (x, y) is the destination cell
        sol[x][y] = 1
        return True 

    # Check if maze[x][y] is a valid move
    if isSafe(maze, x, y) == True: 
        if sol[x][y] == 1:   # check if the current cell is already in solution path.
            return False 
    
        # Mark x, y as part of solution path
        sol[x][y] = 1

        # Move forward in x direction 
        if recurMaze(maze, x + 1, y, sol) == True: 
            return True

        # If moving in x direction doesnt give a solution,
        # then move down in y direction 
        if recurMaze(maze, x, y + 1, sol) == True: 
            return True 

        # If none of the above movements work, then 
        # BACKTRACK: unmark x, y as part of the solution path 
        sol[x][y] = 0 
        return False   # this means the move (x, y) doesnt have a path.


if __name__=='__main__': 
    maze = [[1, 0, 0, 0], 
            [1, 1, 0, 1], 
            [0, 1, 0, 0], 
            [1, 1, 1, 1]]

    print('Maze:')
    for i in range(N): 
        for j in range(N): 
            print('{:6}'.format(maze[i][j]), end = '')
        print()

    solveMaze(maze, N)

    

# Algorithm:  

# 1. Create a solution matrix, initially filled with 0’s.
# 2. Create a recursive function, which takes initial matrix, output matrix and position 
# of rat (i, j).
# 3. if the position is out of the matrix or the position is not valid then return.
# 4. Mark the position output[i][j] as 1 and check if the current position is destination or not. If destination is reached print the output matrix and return.
# 5. Recursively call for position (i+1, j) and (i, j+1).
# 6. Unmark position (i, j), i.e output[i][j] = 0.





