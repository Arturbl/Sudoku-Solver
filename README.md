# Sudoku solver implemented with AC-3 algorithm for arc consistency inference constraints.

## Description
	The AC3 algorithm is a sudoku solver that uses the arc consistency inference constraints to solve the puzzle. 
    It uses a Constraint Satisfaction Problem (CSP) approach, 
    where it creates a queue of constraints and repeatedly revises the domains of variables to maintain consistency. 
    The class CSP is initialized with the game, and the variables, constraints, domains, and neighbours are defined.
    The constraints and neighbours are populated by checking the rows, columns, and clusters. 
    The revise function is used to check if the domain of a variable is consistent with its neighbours. 
    If a solution is not found, the algorithm returns false.

## Problem
&nbsp;&nbsp;![alt text](https://github.com/Arturbl/Sudoku-Solver/blob/main/utils/images/prob.jpeg)


## Solution
&nbsp;&nbsp;![alt text](https://github.com/Arturbl/Sudoku-Solver/blob/main/utils/images/solution.jpeg)
