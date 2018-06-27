import numpy as np
from collections import defaultdict

####################################################################
# MCTS - Monte Carlo Tree Search pseudocode                        #
####################################################################


# def monte_carlo_tree_search(root):
#     while resources_left(time, computational power):
#         leaf = traverse(root) # leaf = unvisited node
#         simulation_result = rollout(leaf)
#         backpropagate(leaf, simulation_result)
#     return best_child(root)


# def traverse(node):
#     while fully_expanded(node):
#         node = best_uct(node)
#     return pick_univisted(node.children) or node # in case no children are present / node is terminal


# def rollout(node):
#     while non_terminal(node):
#         node = rollout_policy(node)
#     return result(node)


# def rollout_policy(node):
#     return pick_random(node.children)


# def backpropagate(node, result):
#     if is_root(node) return
#     node.stats = update_stats(node, result)
#     backpropagate(node.parent)


# def best_child(node):
#     pick child with highest number of visits


####################################################################
# Beginning of actual implementation                               #
####################################################################

####################################################################
# Creating games for checking purpose                              #
####################################################################
class TwoPlayersGameState(object):

    def __init__(self, state, next_to_move):
        self.state = state
        self.next_to_move = next_to_move

    def game_result(self):
        raise NotImplemented("Implement game_result function")

    def is_game_over(self):
        raise NotImplemented("Implement is_game_over function")

    def move(self, action):
        raise NotImplemented("Implement move function")

    def get_legal_actions(self):
        raise NotImplemented("Implement get_legal_actions function")


class Action:
    pass


class TicTacToeMove(Action):

    def __init__(self, x_coordinate, y_coordinate, value):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.value = value

    def __repr__(self):
        return "x:" + str(self.x_coordinate) + " y:" + str(self.y_coordinate) + " v:" + str(self.value)


class TicTacToeGameState(TwoPlayersGameState):

    x = 1
    o = -1

    def __init__(self, state, next_to_move=1):
        if len(state.shape) != 2 or state.shape[0] != state.shape[1]:
            raise ValueError("Please play on 2D square board")
        self.board = state
        self.board_size = state.shape[0]
        self.next_to_move = next_to_move

    @property
    def game_result(self):
        # check if game is over
        rowsum = np.sum(self.board, 0)
        colsum = np.sum(self.board, 1)
        diag_sum_tl = self.board.trace()
        diag_sum_tr = self.board[::-1].trace()

        if any(rowsum == self.board_size) or any(colsum == self.board_size) \
           or diag_sum_tl == self.board_size or diag_sum_tr == self.board_size:
            return 1.
        elif any(rowsum == -self.board_size) or any(colsum == -self.board_size) \
                or diag_sum_tl == -self.board_size or diag_sum_tr == -self.board_size:
            return -1.
        elif np.all(self.board != 0):
            return 0.
        else:
            # if not over - no result
            return None

    def is_game_over(self):
        return self.game_result is not None

    def is_move_legal(self, move):
        # check if correct player moves
        if move.value != self.next_to_move:
            return False

        # check if inside the board
        x_in_range = move.x_coordinate < self.board_size and move.x_coordinate >= 0
        if not x_in_range:
            return False

        # check if inside the board
        y_in_range = move.y_coordinate < self.board_size and move.y_coordinate >= 0
        if not y_in_range:
            return False

        # finally check if board field not occupied yet
        return self.board[move.x_coordinate, move.y_coordinate] == 0

    def move(self, move):
        if not self.is_move_legal(move):
            raise ValueError("move " + move + " on board " + self.board + " is not legal")
        new_board = np.copy(self.board)
        new_board[move.x_coordinate, move.y_coordinate] = move.value
        next_to_move = TicTacToeGameState.o if self.next_to_move == TicTacToeGameState.x else TicTacToeGameState.x
        return TicTacToeGameState(new_board, next_to_move)

    def get_legal_actions(self):
        indices = np.where(self.board == 0)
        return [TicTacToeMove(coords[0], coords[1], self.next_to_move)
                for coords in list(zip(indices[0], indices[1]))]


####################################################################
# Monte Carlo Tree Node                                            #
####################################################################
class MonteCarloTreeSearchNode(object):

    def __init__(self, state: TwoPlayersGameState, parent=None):
        self.state = state
        self.parent = parent
        self.children = []

    @property
    def untried_actions(self):
        raise NotImplemented()

    @property
    def q(self):
        raise NotImplemented()

    @property
    def n(self):
        raise NotImplemented()

    def expand(self):
        raise NotImplemented()

    def is_terminal_node(self):
        raise NotImplemented()

    def rollout(self):
        raise NotImplemented()

    def backpropagate(self, reward):
        raise NotImplemented()

    def is_fully_expanded(self):
        return len(self.untried_actions) == 0

    def best_child(self, c_param = 1.4):
        choices_weights = [
            (c.q / (c.n)) + c_param * np.sqrt((2 * np.log(self.n) / (c.n)))
            for c in self.children
        ]
        return self.children[np.argmax(choices_weights)]

    def rollout_policy(self, possible_moves):
        return possible_moves[np.random.randint(len(possible_moves))]


class TwoPlayersGameMonteCarloTreeSearchNode(MonteCarloTreeSearchNode):

    def __init__(self, state: TwoPlayersGameState, parent):
        super(TwoPlayersGameMonteCarloTreeSearchNode, self).__init__(state, parent)
        self._number_of_visits = 0.
        self._results = defaultdict(int)

    @property
    def untried_actions(self):
        if not hasattr(self, '_untried_actions'):
            self._untried_actions = self.state.get_legal_actions()
        return self._untried_actions

    @property
    def q(self):
        wins = self._results[self.parent.state.next_to_move]
        loses = self._results[-1 * self.parent.state.next_to_move]
        return wins - loses

    @property
    def n(self):
        return self._number_of_visits

    def expand(self):
        action = self.untried_actions.pop()
        next_state = self.state.move(action)
        child_node = TwoPlayersGameMonteCarloTreeSearchNode(next_state, parent=self)
        self.children.append(child_node)
        return child_node

    def is_terminal_node(self):
        return self.state.is_game_over()

    def rollout(self):
        current_rollout_state = self.state
        while not current_rollout_state.is_game_over():
            possible_moves = current_rollout_state.get_legal_actions()
            action = self.rollout_policy(possible_moves)
            current_rollout_state = current_rollout_state.move(action)
        return current_rollout_state.game_result

    def backpropagate(self, result):
        self._number_of_visits += 1.
        self._results[result] += 1.
        if self.parent:
            self.parent.backpropagate(result)


####################################################################
# Monte Carlo Tree Search                                          #
####################################################################
class MonteCarloTreeSearch(object):
    def __init__(self, node: MonteCarloTreeSearchNode):
        self.root = node

    def best_action(self, simulations_number):
        for _ in range(0, simulations_number):
            v = self.tree_policy()
            reward = v.rollout()
            v.backpropagate(reward)
        # exploitation only
        return self.root.best_child(c_param=0.)

    def tree_policy(self):
        current_node = self.root
        while not current_node.is_terminal_node():
            if not current_node.is_fully_expanded():
                return current_node.expand()
            else:
                current_node = current_node.best_child()
        return current_node


####################################################################
# Verifying if MCTS works properly                                 #
####################################################################
def test_if_initial_state_no_result():
    state = TicTacToeGameState(np.zeros((3, 3)), next_to_move=1)
    assert state.game_result is None


def test_if_1_wins_diagonal_case1():
    gamestate = -np.ones((3, 3))
    gamestate[0, 0] = 1
    gamestate[1, 1] = 1
    gamestate[2, 2] = 1

    state = state = TicTacToeGameState(gamestate, next_to_move=-1)
    assert state.game_result == 1
    return state


def test_if_1_wins_diagonal_case2():
    gamestate = -np.ones((3, 3))
    gamestate[0, 2] = 1
    gamestate[1, 1] = 1
    gamestate[2, 0] = 1

    state = state = TicTacToeGameState(gamestate, next_to_move=-1)
    assert state.game_result == 1
    return state


def test_if_0_wins_diagonal_case1():
    gamestate = np.ones((3, 3))
    gamestate[0, 2] = -1
    gamestate[1, 1] = -1
    gamestate[2, 0] = -1
    return gamestate


def test_if_0_wins_diagonal_case2():
    gamestate = np.ones((3, 3))
    gamestate[0, 0] = -1
    gamestate[1, 1] = -1
    gamestate[2, 2] = -1

    state = state = TicTacToeGameState(gamestate, next_to_move=1)
    assert state.game_result == -1
    return state


####################################################################
# Checking time                                                    #
####################################################################
if __name__ == "__main__":
    state = test_if_initial_state_no_result()
    astate = test_if_0_wins_diagonal_case1()
