# Pawn Puzzle Brute Force Solver

## per https://www.reddit.com/r/puzzles/comments/1f7o8mo/whats_the_fastest_way_to_solve_this_puzzle/

The search space is just small enough that a simple BFS can solve it in a reasonable amount of time.

Proves that the optimal solution is 22 steps.

Output
```
Searched up to 1 moves
Searched up to 2 moves
Searched up to 3 moves
Searched up to 4 moves
Searched up to 5 moves
Searched up to 6 moves
Searched up to 7 moves
Searched up to 8 moves
Searched up to 9 moves
Searched up to 10 moves
Searched up to 11 moves
Searched up to 12 moves
Searched up to 13 moves
Searched up to 14 moves
Searched up to 15 moves
Searched up to 16 moves
Searched up to 17 moves
Searched up to 18 moves
Searched 100000 positions
Searched up to 19 moves
Searched up to 20 moves
Searched up to 21 moves
Searched 200000 positions
Searched up to 22 moves
Searched 300000 positions
Success!
NBRN
BBNR
R RN
Q  B

Number of Moves: 22
Path: ['R', 'N', 'B', 'R', 'B', 'R', 'P', 'B', 'N', 'R', 'P', 'N', 'R', 'P', 'R', 'Q', 'N', 'R', 'Q', 'N', 'R', 'Q']
```
