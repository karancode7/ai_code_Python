def display_environment(roomA, roomB):
    print("\nCurrent Environment")
    print("----------------------")
    print("Room A :", roomA)
    print("Room B :", roomB)
    print("----------------------")


def simple_reflex_agent(location, roomA, roomB):

    if location == "A":
        print("\nAgent is in Room A")

        if roomA == "Dirty":
            print("Percept : Room A is Dirty")
            print("Action  : SUCK")
            roomA = "Clean"

        # Move to Room B
        location = "B"

    elif location == "B":
        print("\nAgent is in Room B")

        if roomB == "Dirty":
            print("Percept : Room B is Dirty")
            print("Action  : SUCK")
            roomB = "Clean"

        # Move to Room A
        location = "A"

    return location, roomA, roomB


print("==========================================")
print(" SIMPLE REFLEX AGENT - VACUUM CLEANER WORLD")
print("==========================================")


roomA = input("Enter status of Room A (Clean/Dirty): ").strip().capitalize()
roomB = input("Enter status of Room B (Clean/Dirty): ").strip().capitalize()


location = "A"

display_environment(roomA, roomB)

step = 1


while roomA != "Clean" or roomB != "Clean":

    print("\n========== Step", step, "==========")

    location, roomA, roomB = simple_reflex_agent(location, roomA, roomB)

    display_environment(roomA, roomB)

    step += 1


print("\n========== Final Report ==========")
print("Room A :", roomA)
print("Room B :", roomB)
print("Both rooms are clean.")
print("Goal State Achieved.")
print("Program Completed Successfully.")