from abc import ABC, abstractmethod

class Board:
    """Handles the game board logic"""

    def __init__(self) -> None:
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        """Display the boarding"""
        print("\n")
        for row in self.grid:
            print(' | '.join(row))
            print("-" * 9)
        
    def is_valid_move(self, row, col):
        """Checks if a move is valid"""
        return 0 <= row <= 3 and 0 <= col <= 3 and self.grid[row][col] == " "
    
    def make_move(self, row, col, symbol):
        """Assign the move to the board"""
        self.grid[row][col] = symbol

    def check_winner(self):
        """Checks if there is a winner"""

        #checks for the rows and columns
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != " ":
                return self.grid[i][0]
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != " ":
                return self.grid[0][i]
            
        #check for the diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[0][2] != " ":
            return self.grid[0][2]

        return None 
    
    def is_draw(self):
        "Checks for the draws"
        for row in self.grid:
            if " " in row:
                return False
            return True
    
#abstract class for the player 
class Player(ABC):
    """Abstract class for a player"""

    @abstractmethod
    def get_move(self):
        pass

class HumanPlayer(Player):
    """Handles human player input"""

    def __init__(self, symbol):
        self.symbol = symbol
    
    def get_move(self):
        """Prompts the player for their move."""
        while True:
            try:
                move = input(f"Player {self.symbol}, enter your move(row, column, space-sperated)")
                row,col = map(int, move.split())
                return row, col
            except ValueError:
                print("Invalid input. Please enter two integers seperated by the spaces")

class TicTacToe:
    """Main game logic"""

    def __init__(self):
        self.board = Board()
        self.players = [
            HumanPlayer("X"),
            HumanPlayer("O")
        ]
        self.current_player_index = 0
    
    def play(self):
        """Plays the game."""
        print("Welcome to Tic Tac Toe")
        self.board.display()

        while True:
            current_player = self.players[self.current_player_index] 
            print(f"\n Player {current_player.symbol}'s turn")

            while True:
                row, col = current_player.get_move()
                if self.board.is_valid_move(row, col):
                    self.board.make_move(row, col, current_player.symbol)
                    break
                else:
                    print("Invalid Move. Try again.")
                
            self.board.display()
            
            #check for the winner
            winner = self.board.check_winner()
            if winner:
                print(f"Player {winner} wins!")
                break
            if self.board.is_draw():
                print("It is a draw")
                break

            #switch to other player
            self.current_player_index = 1- self.current_player_index

if __name__ == "__main__":
    game = TicTacToe()
    game.play()    