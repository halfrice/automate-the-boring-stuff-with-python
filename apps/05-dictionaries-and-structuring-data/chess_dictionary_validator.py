#!/usr/bin/evn python3

# chess_dictionary_validator.py


def is_valid_chess_board(board):
    # Construct chessboard positions
    positions = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for x in range(8):
        for y in range(8):
            positions.append(letters[x] + str(y + 1))

    # Construct chess piece names
    colors = ('w', 'b')
    names = {'king': 1, 'queen': 1, 'rook': 2, 'bishop': 2, 'knight': 2, 'pawn': 8}
    pieces = {}
    for color in range(len(colors)):
        for name, count in names.items():
            pieces[colors[color] + name] = count

    # Construct the current game board (who, what, where)
    current_pieces = {}
    for pos, piece in board.items():
        # Check if piece name is valid before adding to current_pieces
        if piece not in pieces:
            return False

        current_pieces.setdefault(piece, 0)
        current_pieces[piece] += 1

        # Check if there are too many pieces
        if current_pieces[piece] > pieces[piece]:
            return False

        # Check if the position is on a valid space
        if pos not in positions and pos[::-1] not in positions:
            return False

    # The chessboard is valid
    return True


# This is the example board provided in figure 5-2 from the book
# Note that the keys are backwards from real chess positiional notation (1h instead of h1)
# Instead of changing them to be correct, we'll adjust our validation to accept both ways
test_board = {
    '1h': 'bking',
    '6c': 'wqueen',
    '2g': 'bbishop',
    '5h': 'bqueen',
    '3e': 'wking',
    '9z': 'brook',  # If left uncommented, this will invalidate the chessboard
}
print(is_valid_chess_board(test_board))

# The starting positions for a standard chess game
starting_board = {
    'a1': 'wrook',
    'b1': 'wknight',
    'c1': 'wbishop',
    'd1': 'wqueen',
    'e1': 'wking',
    'f1': 'wbishop',
    'g1': 'wknight',
    'h1': 'wrook',
    'a2': 'wpawn',
    'b2': 'wpawn',
    'c2': 'wpawn',
    'd2': 'wpawn',
    'e2': 'wpawn',
    'f2': 'wpawn',
    'g2': 'wpawn',
    'h2': 'wpawn',
    # 'e5': 'wking', # If uncommented, this will invalidate the chessboard
    'a7': 'bpawn',
    'b7': 'bpawn',
    'c7': 'bpawn',
    'd7': 'bpawn',
    'e7': 'bpawn',
    'f7': 'bpawn',
    'g7': 'bpawn',
    'h7': 'bpawn',
    'a8': 'brook',
    'b8': 'bknight',
    'c8': 'bbishop',
    'd8': 'bqueen',
    'e8': 'bking',
    'f8': 'bbishop',
    'g8': 'bknight',
    'h8': 'brook',
}
print(is_valid_chess_board(starting_board))
