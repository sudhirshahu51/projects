'''To find the solution of an unsolved sudoku puzzle'''


# Program to print the grid
def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=' ')
        print()


# Program to find the empty position and also to keep track of the increments
def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                l[0], l[1] = row, col
                return True
    return False


# To find if the number is used in that row
def used_in_row(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False


# To find if the number is used in that col
def used_in_col(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False


# To find the the number is used in that box
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[row + i][col + j] == num:
                return True
    return False


# To find if all the conditions for sudoku satisfies
def check_location_is_safe(arr, row, col, num):
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) \
           and not used_in_box(arr, row - row % 3, col - col % 3, num)


# Program to find the solution of sudoku using backtracking and iteration
def solve_soduku(arr):
    l = [0, 0]
    if not find_empty_location(arr, l):
        return True
    row = l[0]
    col = l[1]
    for num in range(1, 10):
        # If the position looks promising
        if check_location_is_safe(arr, row, col, num):
            arr[row][col] = num
            # If the solution is correct return true
            if solve_soduku(arr):
                return True
            # Unmark it and try again
            arr[row][col] = 0
    return False

# Main function
if __name__ == "__main__":
    grid = [[0, 0, 0, 5, 0, 0, 4, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [0, 0, 0, 0, 0, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 0, 0, 0],
            [1, 3, 0, 0, 0, 0, 0, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 0, 2, 0, 0, 0, 0, 0]]
    if solve_soduku(grid):
        print_grid(grid)
    else:
        print('Sorry, No Solution')