#!/usr/bin/evn python3

# conway.py - Conway's Game of Life

import copy
import random
import time

WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells
next_cells = []
for x in range(WIDTH):
    column = []  # Create a new column
    for y in range(HEIGHT):
        # if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):
        if random.randint(0, 1) == 0:
            column.append('#')  # Add a living cell
        else:
            column.append(' ')  # Add a dead cell
    next_cells.append(column)  # next_cells is a list of column lists

while True:  # Main program loop
    print('\n\n\n\n\n')  # Separate each step with a new line
    current_cells = copy.deepcopy(next_cells)

    # Print current_cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='')  # Print the # or space
        print()  # Print a newline at the end of the row

    # Calculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates
            # `% WIDTH` ensures left_coord is always between 0 and WIDTH - 1
            left_coord = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT

            # Count the number of living neighbors
            number_of_neighbors = 0
            if current_cells[left_coord][above_coord] == '#':
                number_of_neighbors += 1  # Top-left neighbor is alive
            if current_cells[x][above_coord] == '#':
                number_of_neighbors += 1  # Top neighbor is alive
            if current_cells[right_coord][above_coord] == '#':
                number_of_neighbors += 1  # Top-right neighbor is alive
            if current_cells[left_coord][y] == '#':
                number_of_neighbors += 1  # Left neighbor is alive
            if current_cells[right_coord][y] == '#':
                number_of_neighbors += 1  # Right neighbor is alive
            if current_cells[left_coord][below_coord] == '#':
                number_of_neighbors += 1  # Bottom-left neighbor is alive
            if current_cells[x][below_coord] == '#':
                number_of_neighbors += 1  # Bottom neighbor is alive
            if current_cells[right_coord][below_coord] == '#':
                number_of_neighbors += 1  # Bottom-right neighbor is alive

            # Set cells based on Conway's Game of Life rules
            if current_cells[x][y] == '#' and (
                number_of_neighbors == 2 or number_of_neighbors == 3
            ):
                # Living cells with 2 or 3 neighbors stay alive
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' ' and number_of_neighbors == 3:
                # Dead cells with 3 neighbors become alive
                next_cells[x][y] = '#'
            else:
                # Everything else dies or stays dead
                next_cells[x][y] = ' '
    time.sleep(1)  # Add 1 second pause to reduce flickering
