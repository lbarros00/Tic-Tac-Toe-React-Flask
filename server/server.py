from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from random import choice

SERVER_URL = ''

app = Flask(__name__)
CORS(app)

infinity = float("inf")

class Game():
    def __init__(self, player='X', computer='O'):
        self.player = player
        self.computer = computer
        self.board = [0] * 9

    def __getitem__(self, item):
        return self.board[item]

    # MODIFIED
    def wins(self, board, player):
        """
        This function tests if a specific player wins.
        :param board: the board of the current board
        :param player: a human or a computer
        :return: True if the player wins
        """
        win_board = [
            [board[0], board[1], board[2]],
            [board[3], board[4], board[5]],
            [board[6], board[7], board[8]],
            [board[0], board[3], board[6]],
            [board[1], board[4], board[7]],
            [board[2], board[5], board[8]],
            [board[0], board[4], board[8]],
            [board[2], board[4], board[6]]
        ]
        if [player, player, player] in win_board:
            return True
        else:
            return False

    def evaluate(self, board):
        """
        Function to heuristic evaluation of board.
        :param board: the board of the current board
        :return: +1 if the computer wins; -1 if the human wins; 0 draw
        """
        if self.wins(board, self.computer):
            score = +1
        elif self.wins(board, self.player):
            score = -1
        else:
            score = 0
        return score

    # MODIFIED
    def empty_cells(self):
        """
        Each empty cell will be added into cells' list
        :param board: the board of the current board
        :return: a list of empty cells
        """
        cells = []

        for i, cell in enumerate(self.board):
            if cell == 0: cells.append([i])

        return cells

    # MODIFIED
    def valid_move(self, index):
        """
        A move is valid if the chosen cell is empty
        :param index: an integer value
        :return: True if the board[index] is empty
        """
        if [index] in self.empty_cells():
            return True
        else:
            return False

    # MODIFIED
    def set_move(self, index, player):
        """
        Set the move on board, if the coordinates are valid
        :param index: an integer value
        :param player: computer or human
        :return: True if player mark was set on the board
        """
        if self.valid_move(index):
            self.board[index] = player
            return True
        else:
            return False

    def game_over(self, board):
        """
        This function test if the human or computer wins
        """
        return self.wins(board, self.player) or self.wins(board, self.computer)

    # MODIFIED
    def minimax(self, board, depth, player):
        """
        AI function that choice the best move
        """
        if player == +1:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        if depth == 0 or self.game_over(board):
            score = self.evaluate(board)
            return [-1, -1, score]

        for cell in self.empty_cells():
            x = cell[0]
            board[x] = player
            score = self.minimax(board, depth - 1, -player)
            board[x] = 0
            score[0] = x

            if player == +1:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value
        return best

    # MODIFIED
    def ai_turn(self):
        """
        It calls the minimax function if the depth < 9,
        else ai chooses a random coordinate.
        """
        depth = len(self.empty_cells())
        if depth == 0 or self.game_over(self.board):
            return

        if depth == 9:
            index = choice([0, 1, 2])
        else:
            move = self.minimax(self.board, depth, +1)
            index = move[0]

        self.set_move(index, self.computer)

    # MODIFIED
    def human_turn(self, index):
        """
        human turn for a valid index in the board
        """
        depth = len(self.empty_cells())
        if depth == 0 or self.game_over(self.board):
            return

        # Dictionary of valid moves
        move = -1
        moves = {
            0: [0], 1: [1], 2: [2],
            3: [3], 4: [4], 5: [5],
            6: [6], 7: [7], 8: [8],
        }
        while (move < 0 or move > 8):
            try:
                move = index
                coord = moves[move]
                try_move = self.set_move(coord[0], self.player)

                if try_move == False:
                    print('Bad move')
                    move = -1
            except KeyboardInterrupt:
                print('Bye')
                exit()
            except:
                print('Bad choice')


@app.route('/round/<human_mark>', methods=['get','post'])
@cross_origin(origin='*')
def start(human_mark):
    # import pdb; pdb.set_trace()
    post = request.get_json()

    game = Game()
    game.board = post.get('board')
    game.player = post.get('player')
    game.computer = post.get('computer')

    print(human_mark)

    if len(game.empty_cells()) > 0 and not game.game_over(game.board):
        game.human_turn(int(human_mark))
        game.ai_turn()
    else:
        if game.wins(game.board, game.player):
            print('YOU WIN!')
        elif game.wins(game.board, game.computer):
            print('YOU LOSE!')
        else:
            print('DRAW!')

    print(game.board)
    return jsonify(game.board)

if __name__ == '__main__':
    app.run(host=SERVER_URL,debug=True)