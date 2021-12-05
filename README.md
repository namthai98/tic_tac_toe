# tic_tac_toe
 Tic tac toe game
Project: Tic tac toe
Programming language: Python
Additional module: T.B.D

- What is tic tac toe ?
Tic-tac-toe, noughts and crosses, or Xs and Os is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. It is a solved game, with a forced draw assuming best play from both players. 

- Introduction
The player (X) will go first. We will get input from the console.
Where each number represents a different number in the grid (top left is 1, bottom right is 9).
    | 1 | 2 | 3 |
    | 4 | 5 | 6 |
    | 7 | 8 | 9 |

Once the player moves, computer will automatically decide on it's move and make it (A.I)

- Algorithm
In this game, computer needs to play against the player. So we need A.I.
We need a simple A.I function for making computer move.
It will check the grid and determine the next move for computer.
The algorithm is described as below:
1. If there is a winning move, take it.
2. If player have a winning move in the next turn, take it.
3. If there is no winning move. Try to take the corner (random)
3. If not, try to take the center
4. Finally, try to take the edge (random)
5. If no move (move = 0), tie game