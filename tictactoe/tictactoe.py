"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cX = 0
    cO = 0
    for row in range(len(board)):
        for col in range(len(board[2])):
            if board[row][col] == 'X':
                cX += 1
            elif board[row][col] == 'O' :
                cO += 1
    if cX == cO:
        return X
    else:
        return O




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    avmove = set()
    for r in range(len(board)):
        for c in range(len(board[2])):
            if board[r][c] == EMPTY:
                avmove.append((r,c))
    return avmove



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (i,j) = action

    tempboard =  copy.deepcopy(board)
    tempboard[i][j] = player(board)


    if i < 0 or j < 0 or i > len(board)+1 or j > len(board[0])+1:
        raise IndexError()
    elif board [i][j] != EMPTY:
        print ('invalid move')

    return tempboard




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def ChckRow(board,player):
        for r in range(len(board)):
            count= 0
            for c in range(len(board[0])):
                if board[r][c] == player:
                    count += 1
            if count == 3:
                return True
        return False

    def ChckCol(board,player):
        for c in range(len(board[0])):
            count = 0
            for r in range(len(board)):
                if board[r][c] == player:
                    count += 1
            if count == 3:
                return True

        return False

    def ChckDiagTop(board,player):
        count = 0
        for r in range(len(board)):
            for c in range(len(board)):
                if r == c and board[r][c] == player:
                    count += 1
        if count == 3:
            return True

    def ChckDiagBot(board,player):
        count = 0
        for r in range(len(board)):
            for c in range(len(board)):
                if (len(board)-1-r) == c and board[r][c] == player:
                    count += 1
        if count == 3:
            return True

    if ChckRow(board,X) or ChckCol(board,X) or ChckDiagTop(board,X) or ChckDiagBot(board,X):
        return X
    elif ChckRow(board,O) or ChckCol(board,O) or ChckDiagTop(board,O) or ChckDiagBot(board,O):
        return O
    else:
        return None




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    def Tie(board):
        rez = len(board)* len(board[0])
        for r in range(len(board)):
            for c in range (len(board[0])):
                if board[r][c] != EMPTY:
                    rez -= 1
        return rez == 0


    if winner(board) or Tie(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        if terminal(board):
            return utility(board)
        m = float('-inf')
        for act in actions(board):
            m = max(m,min_value(result(board,act)))
        return m


    def min_value(board):
        if terminal(board):
            return utility(board)
        m = float('inf')
        for act in actions(board):
            m=min(m,max_value(result(board,act)))
        return m


    if terminal(board):
        return None
    elif player(board) == X:
        lst = []
        for action in actions(board):
            lst.append([min_value(result(board,action)),action])
        return sorted(lst,key=lambda x: x[0], reverse = True)[0][1]
    elif player(board) == O:
        lst = []
        for action in actions(board):
            lst.append([max_value(result(board,action)),action])
        return sorted(lst, key = lambda x: x[0])[0][1]


