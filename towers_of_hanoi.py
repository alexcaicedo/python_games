import copy
import sys

TOTAL_DISKS = 4  # The more disks, the more difficult the puzzle

# Start with all disks on tower A
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))

def run():
    towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}
    
    while True:  # Game loop
        # Display the towers and disks:
        display_towers(towers)

        # Ask user for a move
        from_tower, to_tower = get_player_move(towers)

        # Move the top disk from_tower to to_tower
        disk = towers[from_tower].pop()
        towers[to_tower].append(disk)

        # Check if user has solved the puzzle
        if SOLVED_TOWER in (towers["B"], towers["C"]):
            display_towers(towers)  # Display the towers one last time.
            print("You have solved the puzzle! Well done!")
            sys.exit()

def get_player_move(towers):
    """Asks the player for a move. Returns (fromTower, toTower)."""
    while True:  # Keep asking player until they enter a valid move
        print('Enter the letters of "from" and "to" towers, or Q to QUIT.')
        print("(e.g., AB to move a disk from tower A to tower B.)")
        print()
        response = input("> ").upper().strip()

        if response == "Q":
            print("Thanks for playing!")
            sys.exit()
        
        # Make sure the user entered valid tower letters
        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("Enter one of AB, AC, BA, BC, CA or CB")
            continue  # Ask player again for their move

        # Use more descriptive variable names
        from_tower, to_tower = response[0], response[1]

        if len(towers[from_tower]) == 0:
            # The "from_tower cannot be an empty tower"
            print("You selected a tower with no disks.")
            continue  # Ask player again for their move
        elif len(towers[to_tower]) == 0:
            # Any disk can be moved onto an empty "to" tower
            return from_tower, to_tower
        elif towers[to_tower][-1] < towers[from_tower][-1]:
            print("Can't put a larger disk on top of smaller ones.")
            continue  # Ask player again for their move
        else:
            # This is a valid move, so return the selected towers
            return from_tower, to_tower

def display_towers(towers):
    """Display the three towers with their disks."""
    
    # Display the three towers
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                display_disks(0)  # Display the bare pole with no disks
            else:
                display_disks(tower[level])  # Display the disk
        print()
    
    # Display the tower A, B and C
    empty_space = " " * (TOTAL_DISKS)
    print("{0} A{0}{0} B{0}{0} C\n".format(empty_space))

def display_disks(width):
    """Display a disk of the given width. A width of 0 means no disk."""
    empty_space = " " * (TOTAL_DISKS - width)

    if width == 0:
        # Display a pole segment without a disk
        print(f"{empty_space}||{empty_space}", end="")
    else:
        # Display the disk
        disk = "@" * width
        num_label = str(width).rjust(2, "_")
        print(f"{empty_space}{disk}{num_label}{disk}{empty_space}", end="")

# If this program was run (instead of imported), run the game
if __name__ == "__main__":
    run()