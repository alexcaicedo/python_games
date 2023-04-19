ALL_SPACES = list('123456789')
X, O, BLANK = 'X', 'O', ' '

class TTTBoard:
    def __init__(self, usePrettyBoard=False, useLogging=False):
        self._spaces = {}
        for space in ALL_SPACES:
            self._spaces[space] = BLANK
    
    def getBoardStr(self):
        return f'''
      {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']}  1 2 3
      -+-+-
      {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']}  4 5 6
      -+-+-
      {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']}  7 8 9'''

    def isValidSpace(self, space):
        return space in ALL_SPACES and self._spaces[space] == BLANK
    
    def isWinner(self, player):
        s, p = self._spaces, player
        return ((s['1'] == s['2'] == s['3'] == p) or # Across the top
                (s['4'] == s['5'] == s['6'] == p) or # Across the middle
                (s['7'] == s['8'] == s['9'] == p) or # Across the bottom
                (s['1'] == s['4'] == s['7'] == p) or # Down the left
                (s['2'] == s['5'] == s['8'] == p) or # Down the middle
                (s['3'] == s['6'] == s['9'] == p) or # Down the right
                (s['3'] == s['5'] == s['7'] == p) or # Diagonal
                (s['1'] == s['5'] == s['9'] == p))   # Diagonal
    
    def isBoardFull(self):
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False
        return True
    
    def updateBoard(self, space, player):
        self._spaces[space] = player

def run():
    print('Welcome to Tic-Tac-Toe!')
    gameBoard = TTTBoard()
    currentPlayer, nextPlayer = X, O

    while True:
        print(gameBoard.getBoardStr())
        move = None
        while not gameBoard.isValidSpace(move):
            print(f'What is {currentPlayer}\'s move? (1-9)')
            move = input("> ")
        gameBoard.updateBoard(move, currentPlayer)

        if gameBoard.isWinner(currentPlayer):
            print(gameBoard.getBoardStr())
            print(currentPlayer + ' has won the game!')
            break
        elif gameBoard.isBoardFull():
            print(gameBoard.getBoardStr())
            print('The game is a tie!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Thanks for playing!')

if __name__ == '__main__':
    run()