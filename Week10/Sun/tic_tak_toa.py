"""Tic-Tac-Toe game implementation with win/draw detection."""
from abc import ABC, abstractmethod
from typing import List, Optional,Tuple
import random

# Abstract base class for game
class TicTacToaGame(ABC):
    """Abstract base class for Tic-Tac-Toe game."""   
    @abstractmethod
    def play(self):
        """Start the game."""       
    @abstractmethod
    def check_winner(self) -> Optional[str]:
        """Check for a winner and return 'X', 'O', or None."""
    @abstractmethod
    def is_draw(self) -> bool:
        """Check if the game is a draw."""    
class TicTacToe(TicTacToaGame):
    """ Concrete implementation of Tic-Tac-Toe game"""
    def __init__(self):
        """Initialize the game board and starting player."""
        self.board: List[List[str]] = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player: str = 'X'
    def display_board(self) -> None:
        """Display the current state of the game board."""
        print("\n")
        for row in self.board:
            print("|".join(row))
            print("-" * 5)
        print("\n")
    def play(self) -> None:
        """Main game loop handling player and computer moves."""        
        while True:
            self.display_board()
            if self.current_player == 'X':
                row, col = self.get_player_move()
            else:
                row, col = self.get_computer_move()

            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                if self.check_winner():
                    self.display_board()
                    print(f"Player {self.current_player} wins!")
                    break
                if self.is_draw():
                    self.display_board()
                    print("It's a draw!")
                    break
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            else:
                print("Invalid move. Try again.")             
    def get_player_move(self) -> Tuple[int, int]:
        """Get and validate player's move input."""
        while True:
            try:
                move = input("Enter your move (row and column) as 'row,col': ")
                row, col = map(int, move.split(','))
                if row in range(3) and col in range(3):
                    return row, col
                print("Row and column must be between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter row and column as 'row,col'.")
    def get_computer_move(self) -> Tuple[int, int]:
        """Generate a random valid move for the computer."""
        empty_cells = [
            (r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' '
            ]
        return random.choice(empty_cells)   
    def check_winner(self) -> Optional[str]:
        """Check all winning combinations for a winner."""
        lines = (
            # Horizontal
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # Vertical
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            # Diagonal
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        )
        for line in lines:
            a, b, c = line
            if (self.board[a[0]][a[1]] == 
                self.board[b[0]][b[1]] == 
                self.board[c[0]][c[1]] != ' '
                ):
                return self.board[a[0]][line[1]]
        return None   
    def is_draw(self) -> bool:
        """Check if the board is full and there is no winner."""
        return all(cell != ' ' for row in self.board for cell in row) and not self.check_winner()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
