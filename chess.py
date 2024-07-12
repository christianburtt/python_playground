chess_board = {
    'a1':'',
    'a2':'',
    'a3':'',
    'a4':'',
    'a5':'',
    'a6':'',
    'a7':'',
    'a8':'',
    'b1':'',
    'b2':'',
    'b3':'',
    'b4':'',
    'b5':'',
    'b6':'',
    'b7':'',
    'b8':'',
    'c1':'',
    'c2':'',
    'c3':'',
    'c4':'',
    'c5':'',
    'c6':'',
    'c7':'',
    'c8':'',
    'd1':'',
    'd2':'',
    'd3':'',
    'd4':'',
    'd5':'',
    'd6':'',
    'd7':'',
    'd8':'',
    'e1':'',
    'e2':'',
    'e3':'',
    'e4':'',
    'e5':'',
    'e6':'',
    'e7':'',
    'e8':'',
    'f1':'',
    'f2':'',
    'f3':'',
    'f4':'',
    'f5':'',
    'f6':'',
    'f7':'',
    'f8':'',
    'g1':'',
    'g2':'',
    'g3':'',
    'g4':'',
    'g5':'',
    'g6':'',
    'g7':'',
    'g8':'',
    'h1':'',
    'h2':'',
    'h3':'',
    'h4':'',
    'h5':'',
    'h6':'',
    'h7':'',
    'h8':''
}
white_pieces = ['pawn','king']
occupied_spots = []
def print_board(board):
    for c in range(ord('a'), ord('h')+1):
        j= chr(c)
        for i in range(1,9):
            print(board[str(j)+str(i)] or "_", end="")
        print()

def choose_white(white_pieces, board):
    input_val = input("choose your piece, pawn or king, and a location. (E.g. pawn a2): ").lower()
    while " " not in input_val:
        input_val = input("choose your piece, pawn or king, and a location. (E.g. pawn a2): ").lower()
    piece, loc = input_val.split(" ")
    while piece not in white_pieces:
        print("not a valid piece.")
        piece = input("choose your piece, pawn or king: ").lower()
    while loc not in board.keys():
        print("not a valid location.")
        loc = input(f"place your {piece} (E.g. a2):  ").lower().strip()
    board[loc] = "W"
    return piece,loc

def choose_black(board,occupied):
    black_count = 0
    input_val = ""
    while input_val != "done" and black_count < 16:
        input_val = input("place at least 1 black piece on the board (a1-h8): ").lower().strip()
        if input_val == "done" and black_count==0:
            print("You must place at least 1 black piece")
            input_val = ""
            continue
        if input_val not in board.keys():
            print("not a valid location.")
            continue
        if input_val in occupied:
            print("that location is occupied already.")
            continue
        black_count+=1
        occupied.append(input_val)
        board[input_val] = "b"

white, w_loc = choose_white(white_pieces,chess_board)
occupied_spots.append(w_loc)
choose_black(chess_board, occupied_spots)
print_board(chess_board)
       