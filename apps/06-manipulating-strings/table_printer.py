#!/usr/bin/env python3

# table_printer.py


def print_table(data):
    # Calculate the max width of each column
    column_widths = []
    for column in data:
        largest = 0
        for item in column:
            if len(item) > largest:
                largest = len(item)
        column_widths.append(largest)

    # Construct the table row by row
    table = []
    for y in range(len(data[0])):
        row = []
        for x in range(len(data)):
            row.append(data[x][y].rjust(column_widths[x]))
        table.append(' '.join(row))

    # Display the table
    print('\n'.join(table))


table_data = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose'],
]

# Additional test case
test_data = [
    ['1:', '2:', '3:', '4:', '99:'],
    ['BIGGESTWORDFIRST', 'SECONDBiggest', 'ThirdBiggest', 'fourthbig', 'small'],
    ['one', 'two', 'three', 'four', 'ninetynine'],
]

print_table(table_data)
# print_table(test_data)
