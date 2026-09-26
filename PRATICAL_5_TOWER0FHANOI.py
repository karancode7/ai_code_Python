from collections import deque


def get_next_states(state):
    next_states = []

    # Three rods: A, B, C
    for source in range(3):

        # If source rod is empty, no move is possible
        if len(state[source]) == 0:
            continue

        disk = state[source][-1]

        for destination in range(3):

            if source == destination:
                continue

            # Legal move
            if len(state[destination]) == 0 or state[destination][-1] > disk:

                new_state = [list(rod) for rod in state]

                # Move disk
                new_state[source].pop()
                new_state[destination].append(disk)

                new_state = tuple(tuple(rod) for rod in new_state)

                next_states.append(
                    (new_state, source, destination, disk)
                )

    return next_states


def display_state(state):
    rods = ['A', 'B', 'C']

    for i in range(3):
        print(rods[i], ":", list(state[i]))


def tower_of_hanoi(n, source_rod, goal_rod):

    rods = ['A', 'B', 'C']

    source = rods.index(source_rod)
    goal = rods.index(goal_rod)

    # Initial state
    disks = tuple(range(n, 0, -1))

    initial = [(), (), ()]
    initial[source] = disks
    initial = tuple(initial)

    # Goal state
    goal_state = [(), (), ()]
    goal_state[goal] = disks
    goal_state = tuple(goal_state)

    # BFS Queue
    queue = deque([initial])

    # Visited states
    visited = {initial}

    # Parent information
    parent = {initial: None}

    # Move information
    move = {}

    while queue:

        current = queue.popleft()

        # Goal reached
        if current == goal_state:
            break

        # Generate next states
        for next_state, s, d, disk in get_next_states(current):

            if next_state not in visited:

                visited.add(next_state)
                queue.append(next_state)

                parent[next_state] = current
                move[next_state] = (s, d, disk)

    # Construct solution path
    path = []
    current = goal_state

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path, move


# ---------------- MAIN PROGRAM ----------------

print("TOWER OF HANOI - STATE SPACE SEARCH")

n = int(input("Enter number of disks: "))

source_rod = input("Enter source rod (A/B/C): ").upper()
goal_rod = input("Enter goal rod (A/B/C): ").upper()

# Validate input
if n <= 0:
    print("Number of disks must be greater than 0.")

elif source_rod not in ['A', 'B', 'C']:
    print("Invalid source rod.")

elif goal_rod not in ['A', 'B', 'C']:
    print("Invalid goal rod.")

elif source_rod == goal_rod:
    print("Source and goal rods must be different.")

else:

    path, move = tower_of_hanoi(n, source_rod, goal_rod)

    print("\nInitial State:")
    display_state(path[0])

    print("\nSolution:")

    for i in range(1, len(path)):

        s, d, disk = move[path[i]]

        print("\nMove disk", disk,
              "from", chr(65 + s),
              "to", chr(65 + d))

        display_state(path[i])

    print("\nGoal State:")
    display_state(path[-1])

    print("\nTotal number of moves:", len(path) - 1)