from copy import deepcopy


class Board:
    def __init__(self):
        self.board = []
        self.chars = ("-", "X", "O")
        self.move_stack = []
        self.solutions = 0
        self.games = 0
        self.setup()

    def setup(self):
        self.solutions = 0
        self.games = 0
        self.move_stack = []
        self.board = [
            [-1, -1, 1, 1, 1, -1, -1],
            [-1, -1, 1, 1, 1, -1, -1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [-1, -1, 1, 1, 1, -1, -1],
            [-1, -1, 1, 1, 1, -1, -1]
        ]

    def print(self):
        for row in self.board:
            print(f'{" ".join(self.chars[x+1] for x in row)}')

    def list_moves(self):
        moves = []
        for n, row in enumerate(self.board):
            for m, piece in enumerate(row):
                if piece == 1: 
                    moves += self.get_moves_for_piece(n, m)
        return moves

    def get_moves_for_piece(self, n, m):
        moves = []
        if self.safe_query(n-1, m, 1) and self.safe_query(n-2, m, 0):
            moves.append([n, m, "up"])
        if self.safe_query(n, m+1, 1) and self.safe_query(n, m+2, 0):
            moves.append([n, m, "right"])
        if self.safe_query(n+1, m, 1) and self.safe_query(n+2, m, 0):
            moves.append([n, m, "down"])
        if self.safe_query(n, m-1, 1) and self.safe_query(n, m-2, 0):
            moves.append([n, m, "left"])
        return moves

    def safe_query(self, n, m, value):
        if 0 <= n <= 6 and 0 <= m <= 6 and self.board[n][m] == value:
            return True

    def solve(self):
        moves = self.list_moves()
        if len(moves) == 0:
            self.games += 1
        if self.is_solved():
            self.solutions += 1
        for move in moves:
            self.make_move(move)
            self.solve()
            self.undo_move(move)

    def is_solved(self):
        if sum([sum(row) for row in self.board]) == -15:
            return True
        return False

    def make_move(self, move):
        self.move_stack.append(move)
        if move[2] == "up":
            self.board[move[0]][move[1]] = 0
            self.board[move[0]-1][move[1]] = 0
            self.board[move[0]-2][move[1]] = 1
        if move[2] == "right":
            self.board[move[0]][move[1]] = 0
            self.board[move[0]][move[1]+1] = 0
            self.board[move[0]][move[1]+2] = 1
        if move[2] == "down":
            self.board[move[0]][move[1]] = 0
            self.board[move[0]+1][move[1]] = 0
            self.board[move[0]+2][move[1]] = 1
        if move[2] == "left":
            self.board[move[0]][move[1]] = 0
            self.board[move[0]][move[1]-1] = 0
            self.board[move[0]][move[1]-2] = 1

    def undo_move(self, move):
        self.move_stack.pop()
        if move[2] == "up":
            self.board[move[0]][move[1]] = 1
            self.board[move[0]-1][move[1]] = 1
            self.board[move[0]-2][move[1]] = 0
        if move[2] == "right":
            self.board[move[0]][move[1]] = 1
            self.board[move[0]][move[1]+1] = 1
            self.board[move[0]][move[1]+2] = 0
        if move[2] == "down":
            self.board[move[0]][move[1]] = 1
            self.board[move[0]+1][move[1]] = 1
            self.board[move[0]+2][move[1]] = 0
        if move[2] == "left":
            self.board[move[0]][move[1]] = 1
            self.board[move[0]][move[1]-1] = 1
            self.board[move[0]][move[1]-2] = 0

    def replay_solve(self):
        self.setup()
        self.print()
        stack = deepcopy(self.move_stack)
        for move in stack:
            input("\n\n")
            self.make_move(move)
            self.print()


def main():
    game = Board()
    game.solve()
    # game.replay_solve()
    print(f"Total games: {game.games}")
    print(f"Winning games: {game.solutions}")
    

if __name__ == "__main__":
    main()