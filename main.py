import numpy as np
# Quantum Naughts and Crosses/Tick-Tac-Toe Solver


X_wins = {'111qqqqqq', 'qqq111qqq', '1qq1qq1qq'}
O_wins = {'000qqqqqq', 'qqq000qqq', '0qq0qq0qq'}


class Board:
    def __init__(self, initial_state='XOOXqqOqq'):
        self.state = initial_state

    def view_board(self):
        vis = list(self.state.replace('q', ' '))
        print('\n' + ' ' + vis[0] + ' | ' + vis[1] + ' | ' + vis[2] + '\n' + '---+---+---' + '\n' +
              ' ' + vis[3] + ' | ' + vis[4] + ' | ' + vis[5] + '\n' + '---+---+---' + '\n' +
              ' ' + vis[6] + ' | ' + vis[7] + ' | ' + vis[8] + '\n')

    def X_turn(self, location):
        self.state = list(self.state)
        if self.state[location] == 'q':
            self.state[location] = 'X'
        self.state = ''.join(self.state)

    def O_turn(self, location):
        self.state = list(self.state)
        if self.state[location] == 'q':
            self.state[location] = 'O'
        self.state = ''.join(self.state)

    def X_win_probability(self):
        return

    def visualize_probability(self):
        return

    def rotate_board(self): # Method that alters the state of the board by physical rotation
        board = self.state.replace('q', '2')
        board = board.replace('X', '1')
        board = board.replace('O', '0')
        board = np.asarray(list(map(int, board)))[:, np.newaxis]
        R = np.array([[0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 1, 0, 0, 0, 0, 0, 0]], dtype=int)
        board = np.transpose(np.matmul(R, board))
        board = [str(element) for element in board[0]]
        board = ''.join(board).replace('2', 'q')
        board = board.replace('1', 'X')
        board = board.replace('0', 'O')
        self.state = board

    def create_circuit(self):
        return


test = Board(initial_state='qXOqqXXqO')




