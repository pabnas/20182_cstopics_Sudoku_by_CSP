# Description of the problem

## Theoretical foundations for the solution

The Sudoku is a puzzle played on a partially filled 9x9 grid. The task is to complete the assignment using numbers from 1 to 9 such that the entries in each row, each column and each major 3x3 block are pairwise different. Like for many logical puzzles the challenge in Sudoku does not just lie in finding a solution. Well posed puzzles have a unique solution and the task is to find it without guessing. There are going to be an agent that will solve Sudokus created before and exported in a plain text 

## Block and/or flow diagram

![alt text](http://url/to/img.png)

## Technical specifications of the implemented technique

There are several ways to solve Sudoku as there are several difficulties in this for example the difficulty easy can be solved by pruning the most complex need of backtracking as there are various numbers that match in two or more box; the algorithm is responsible for test the check with the lowest domain (less constraint) if there is any constraint returned in the assignment of numbers and test again until find a solution

## Screenshots

![alt text](https://user-images.githubusercontent.com/39195909/49085477-1c271a00-f220-11e8-8209-4814a2356295.png)

![alt text](https://user-images.githubusercontent.com/39195909/49085479-1cbfb080-f220-11e8-810a-52e32011d6a8.png)

## Link to project’s YouTube video

[Youtube Video](https://pages.github.com/)

# Dependencies and instructions to run the Project

The only external libraries that we're going to use are pygame and numpy; To run the program just use the command

```
phyton lab.py 
```

In the file called test_boards.py you can find 7 boards which can be loaded in the main program something like:

```
board = board0 
```

# Resources
[Sudoku as a Constraint Problem](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.88.2964&rep=rep1&type=pdf)

[The most difficult Sudoku puzzles are quickly solved by a straightforward depth-first search algorithm.](https://www.dcc.fc.up.pt/~acm/sudoku.pdf)

[Sudoku as a CSP](https://www.codeproject.com/Articles/34403/Sudoku-as-a-CSP)


###### Made by 

Santiago Barragan - Carolina Gomez

