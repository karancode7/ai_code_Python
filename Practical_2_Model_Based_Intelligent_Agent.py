
from collections import deque

# ---------------- Display Grid ----------------
def display_grid(grid):
    print("\nGrid Environment:")
    for row in grid:
        print(" ".join(row))

# ---------------- Model-Based Intelligent Agent ----------------
def model_based_agent(grid):

    rows = len(grid)
    cols = len(grid[0])

    start = None
    goal = None

    # Find Start and Goal
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "G":
                goal = (i, j)

    if start is None or goal is None:
        print("\nStart (S) or Goal (G) not found!")
        return

    queue = deque([(start, [start])])
    visited = {start}

    # Up, Down, Left, Right
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:

        current, path = queue.popleft()

        print("Current Position :", current)

        if current == goal:
            print("\nGoal Reached Successfully!")
            print("\nShortest Path :")
            for p in path:
                print(p, end=" ")
            print()
            return

        x, y = current

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if (0 <= nx < rows and
                0 <= ny < cols and
                grid[nx][ny] != "X" and
                (nx, ny) not in visited):

                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    print("\nNo Path Found!")

# ---------------- Main Menu ----------------
while True:

    print("\n========== MODEL-BASED INTELLIGENT AGENT ==========")
    print("1. Run Demo (Automatic Output)")
    print("2. Run with User Input")
    print("3. Exit")

    choice = input("\nEnter Your Choice : ")

    # -------- Demo Mode --------
    if choice == "1":

        grid = [
            ["S", "0", "0", "X", "0"],
            ["X", "X", "0", "X", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "X", "X", "X", "0"],
            ["0", "0", "0", "G", "0"]
        ]

        print("\nDemo Grid Loaded Successfully!")

        display_grid(grid)
        model_based_agent(grid)

    # -------- User Input Mode --------
    elif choice == "2":

        rows = int(input("\nEnter Number of Rows : "))
        cols = int(input("Enter Number of Columns : "))

        print("\nEnter Grid")
        print("S = Start")
        print("G = Goal")
        print("X = Obstacle")
        print("0 = Free Cell\n")

        grid = []

        for i in range(rows):

            row = input(f"Enter Row {i+1} : ").split()

            while len(row) != cols:
                print(f"Please enter exactly {cols} values.")
                row = input(f"Enter Row {i+1} : ").split()

            grid.append(row)

        display_grid(grid)
        model_based_agent(grid)

    # -------- Exit --------
    elif choice == "3":
        print("\nThank You!")
        print("Program Closed Successfully.")
        break

    else:
        print("\nInvalid Choice! Please Enter 1, 2 or 3.")