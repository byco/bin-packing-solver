<h1>Bin Packing Problem Solver</h1>

In the bin packing problem, objects with different volumes are packed into a finite number of bins in an order that minimizes the number of bins used. This Python program uses three greedy approximation algorithms to solve the bin packing problem.

Check out a demo here: https://repl.it/@byco/Bin-Packing-Solver

<h1>How to edit bin.txt</h1>

This program will use a text file (titled here as "bin.txt") that includes information in this order: number of test cases, weight capacity of the bin, number of items to be put into the bins and the weights of the items on one line, seaparated by a space.  Using this data -- which will be converted from strings to ints and stored in arrays, the program will determine how to put the items into the bins using first fit, first fit descending, and best fit algorithms and output the number of bins used according to each algorithm into the terminal window.

Sample input in bin.txt:

    3
    10
    6
    5 10 2 5 4 4
    10
    20
    4 4 4 4 4 4 4 4 4 4 6 6 6 6 6 6 6 6 6 6
    10
    4
    3 8 2 7

Sample output:

    Test Case 1 

    First Fit: 4, First Fit Decreasing: 3, Best Fit: 4 

    Test Case 2

    First Fit: 15, First Fit Decreasing: 10, Best Fit:15

    Test Case 3 

    First Fit: 3, First Fit Decreasing: 2, Best Fit: 2

<h1>How to run locally</h1>

PREREQUISITES
You should have bin.txt in the same directory as binpack.py.

INSTALLING
Using a terminal window, go to the directory where binpack.py and bin.txt are saved. To compile the sorting programs, type the below into the terminal window and run:

python binpack.py

RUNNING THE PROGRAMS
The program results can be read in the terminal window.

BUILT WITH
CLion, 
Flip on the OSU server
