def print_grid(grid):
    """utility function to print the sudoku grid in a readable formate"""
    for row in grid:
        print(" ".join(str(num) for num in row))

def find_empty_location(grid,l):
    """find the next empty location in the grid"""
    for row in range(9):
        for col in range(9):
            if grid[row][col]==0:
                l[0]=row
                l[1]=col
                return True
        
        return False

def used_in_row(grid,row,num):
    """check if the number is already present in the current row"""
    return any(grid[row][col] == num for col in range(9))

def used_in_col(grid,col,num):
    """check if the number is already present in the current column"""
    return any(grid[col][row] == num for row in range(9))

def used_in_box(grid, row, col, num):
    """check if number is already present in the 3x3 sub grid"""
    box_row= row - row % 3
    box_col= col - col % 3
    return any(grid[i][j] == num for i in range(box_row, box_row+3) for j in range(box_col, box_col+3))

def check_location_is_safe(grid, row, col, num):
    """check if it is safe to place a number in a given cell"""
    return (not used_in_row(grid,row,num) and not used_in_col(grid,col,num) and not used_in_box(grid,row,col,num))

def solve_sudoku(grid):
    """main function that uses backtracking to solve the sudoku"""
    l=[0,0]
    if not find_empty_location(grid,l):
        return True
    
    row,col=l

    for num in range(1,10):
        if check_location_is_safe(grid, row, col, num):
            grid[row][col]=num

            if solve_sudoku(grid):
                return True
            
            grid[row][col]=0
        
    return False


if __name__ == '__main__':
    grid=[
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    print('Initial sudoku grid')
    print_grid(grid)

    if solve_sudoku(grid):
        print("\nSudoku grid solved successfully")
        print_grid(grid)

    else:
        print("No solution exists")