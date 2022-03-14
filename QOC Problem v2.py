# A quantum tic-tac-toe problem

import numpy as np

# Creating individual qubit states
O = np.array([[1], [0]])
X = np.array([[0], [1]])
q = (1/np.sqrt(2))*np.array([[1], [1]])

# Creating dictionary mapping strings to states
qubit_dict = {'O': O, 'X': X, 'q': q}


# function to create a quantum state given a string of X,O and qs
def create_state(string):
    qubits = list(string)
    state = np.kron(qubit_dict[qubits[0]], qubit_dict[qubits[1]])
    state = np.kron(state, qubit_dict[qubits[2]])
    state = np.kron(state, qubit_dict[qubits[3]])
    return state


# Creating list of winning states, completely orthogonal, X reaches win condition first
w1 = create_state('XXOO')
w2 = create_state('XOOX')
win_states = [w1, w2]


# get win probability function using the Born probability rule from state string
def get_win_probability(state_string):
    prob_list = [np.dot(np.transpose(create_state(state_string)), w)[0][0]**2 for w in win_states]
    factor = state_string.count('q')
    prob = sum(prob_list)
    # if factor != 0:
    #     prob = 2*factor*prob
    return prob


# creating function to place X at specified index given the string of a state
def place_X(state_string, index):
    qubits = list(state_string)
    if qubits[index] == 'q':
        qubits[index] = 'X'
    new_state_string = ''.join(qubits)
    return new_state_string


# Blank initial state in problem as we are only interest in 4 remaining spaces
initial_string = 'qqqq'
initial = create_state(initial_string)

# calculating win probability
p1 = np.round(get_win_probability(initial_string), 3)  # p = 0.5


# building algorithm to test best condition
def get_best_move(state_string):
    current_win_prob = get_win_probability(state_string)
    best_p = 0
    best_i = 0
    for i in range(len(state_string)):
        p_i = get_win_probability(place_X(state_string, i))
        if p_i > best_p:
            best_p = p_i
            best_i = i
        i += 1
    if best_p <= current_win_prob:
        print("A strange game. The only winning move is not to play.")
    else:
        print("The best position to play is {}, with a win probability of {}.".format(best_i, best_p))
    return [best_i, best_p]


# Testing best move:
get_best_move('qqqq')  # Best move is in the centre of the board





