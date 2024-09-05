from copy import deepcopy
import heapq


class Piece:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, board, empty_square):
        empty_square_bp = empty_square
        empty_square = (self.y_pos, self.x_pos)
        self.y_pos, self.x_pos = empty_square_bp
        if isinstance(self, Pawn) and self.y_pos == 0:
            board[self.y_pos][self.x_pos] = Queen(self.x_pos, self.y_pos)
        else:
            board[self.y_pos][self.x_pos] = self
        board[empty_square[0]][empty_square[1]] = None
        return empty_square

    def __lt__(self, other):
        return False


class Knight(Piece):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

    def can_move(self, empty_square):
        y, x = empty_square
        if (abs(self.x_pos-x) == 2 and abs(self.y_pos-y) == 1) or (abs(self.x_pos-x) == 1 and abs(self.y_pos-y) == 2):
            return True
        return False

    def __str__(self):
        return "N"


class Rook(Piece):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

    def can_move(self, empty_square):
        y, x = empty_square
        if (self.x_pos == x and abs(self.y_pos-y) == 1) or (self.y_pos == y and abs(self.x_pos-x) == 1):
            return True
        return False

    def __str__(self):
        return "R"


class Bishop(Piece):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

    def can_move(self, empty_square):
        y, x = empty_square
        if abs(self.x_pos-x) == abs(self.y_pos-y) == 1:
            return True
        return False

    def __str__(self):
        return "B"


class Queen(Piece):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

    def can_move(self, empty_square):
        y, x = empty_square
        if abs(self.x_pos-x)<=1 and abs(self.y_pos-y)<=1:
            return True
        return False

    def __str__(self):
        return "Q"


class Pawn(Piece):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

    def can_move(self, empty_square):
        y, x = empty_square
        if self.x_pos == x and abs(self.y_pos-y) == 1:
            return True
        return False

    def __str__(self):
        return "P"


def init():
    board = [[None for i in range(4)] for j in range(4)]
    # 4 knights at x=0, y=0,1,2,3
    for i in range(4):
        board[0][i] = Knight(i, 0)
    # 4 bishops at x=1, y=0,1,2,3
    for i in range(4):
        board[1][i] = Bishop(i, 1)
    # 4 rooks at x=2, y=0,1,2,3
    for i in range(4):
        board[2][i] = Rook(i, 2)
    # 1 pawn at x=3, y=3
    board[3][3] = Pawn(3, 3)
    return board


def check_success(board):
    return isinstance(board[3][0], Queen)


def hash_board(board):
    result = ""
    for row in board:
        for piece in row:
            if piece is None:
                result += " "
            else:
                result += str(piece)
        result += "\n"
    return result

def search():
    positions_seen = set()
    total_iters = 0
    search_queue = [(0, ((3,0), init()))]  # (iter, (empty_square, board))
    prev_iter = 0
    while len(search_queue) > 0:
        iters, (empty_square, board) = heapq.heappop(search_queue)
        board_hashed = hash_board(board)
        if board_hashed in positions_seen:
            continue
        positions_seen.add(board_hashed)
        if iters != prev_iter:
            print(f"Number of Moves: {iters}")
            prev_iter = iters
        total_iters += 1
        if total_iters%100000 == 0:
            print(f"Searched {total_iters} positions")
        if check_success(board):
            print("Success!")
            print_board(board)
            print(f"Number of Moves: {iter}")
            return
        # find all possible moves
        board_bp = [[deepcopy(board[j][i]) for i in range(4)] for j in range(4)]
        empty_square_bp = deepcopy(empty_square)
        for i in range(4):
            for j in range(4):
                if board[i][j] is not None and board[i][j].can_move(empty_square):
                    empty_square = board[i][j].move(board, empty_square)
                    heapq.heappush(search_queue, (iters+1, (empty_square, board)))
                    empty_square = deepcopy(empty_square_bp)
                    board = deepcopy(board_bp)
    print(f"Total iterations: {total_iters}")


def print_board(board):
    print(hash_board(board))


if __name__ == "__main__":
    search()
