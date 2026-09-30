# 8-Queens Problem using Backtracking

def is_safe(board, row, col):
    # Check all previously placed queens
    for i in range(row):

        # Check same column
        if board[i] == col:
            return False

        # Check diagonal
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row, n):
    # All queens are successfully placed
    if row == n:
        return True

    # Try each column
    for col in range(n):

        if is_safe(board, row, col):

            # Place queen
            board[row] = col

            # Move to next row
            if solve(board, row + 1, n):
                return True

            # Backtrack
            board[row] = -1

    return False


def display_board(board, n):
    print("\nSolution:")
    
    for row in range(n):
        for col in range(n):

            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


# Main Program
n = int(input("Enter number of queens: "))

board = [-1] * n

if solve(board, 0, n):
    display_board(board, n)
else:
    print("No solution exists.")

