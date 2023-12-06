# Advent of Code 2023

# Day 1 -  Trebuchet?!
## Part 1
The solution for the part one is straightforward, we just iterate over the line moving two pointers, one pointing at the start of the line and the second pointing at its tail. When we found an index containing a digit, we stop updating the corrisponding pointer and when the first digit form the tail and the first digit from the head are found, we are done. 
| Time Complexity | Space Complexity |
|-----------------|------------------|
| O(n)            | O(1)             |

## Part 2
This time we are required to look for strings and not just for digits. We'll keep the same approach of iterating through each line from the head and from the tail, but will split the problem in two parts. 
1. First we will look for all the occurrences of the words that we are looking for in the line and then we will select the one located at the minimum possible index. 
2. Then we will do the same, but on the reversed string looking for the reversed words, this will be done using the same approach used in point 1

| Time Complexity | Space Complexity |
|-----------------|------------------|
| O(np) -> O(n)   | O(1)             |

where p is the number of patterns to match in the strings, which is 20 as we are looking for the digits or words stating for numbers from zero to nine

# Day 2 - Cube Conundrum
## Part 1 
Given a target game, for each line of the input file we check if the extractions in the line are compatible with the target game.
To do so, we gather the maximum number of cube for each color extracted during a game, let's call it "minimum viable game", and compare those numbers withe one in the target game. 

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(n)           | O(1)             |


## Part 2
We use the minimum viable game found in part 1, which is our solution.

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(n)           | O(1)             |

# Day 3 - Gear Ratios
I'll be honest, I struggled a bit with this one. 

## Part 1 
The flow of the algorithm is the following: 
1. Scan the matrix looking for anything but a digit, this is our symbol that "enables" the numbers in its surroundings. 
2. Once we found a symbol, we look in the the cells around it for digits and store their positions. 
    Let's take a sub matrix made as follows:
    ```
        __0___1___2__
     0  |_._|_2_|_3_|
     1  |_._|_$_|_._|
     2  |_1_|_._|_._|
    ```
    The output of this step with the example above is: [(0,1), (0,2), (2,0)]
3. For each index found in the previous step, parse the line containing the digit and merge the continuous digits as they are part of the same number. 
    Therefore the indexes found in step two will be evaluated as follows:
    ```
    (0,1), (0,2)    -> 23
    (2,0)           -> 1
    ```
4. sum up all the numbers

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(m*n)           | O(p)           |

Where:
- m is the number of rows
- n is the number of columns
- p is the number of digits in the matrix

## Part 2
What changes in the algorithm described in part one is the following: 
1. We are no more looking for anything but a digit in step 1, but we are looking only for '*'
2. In step 3, when we parse the numbers found in step two, we discard any * surrounded by more than three numbers

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(m*n)           | O(p)           |

Where:
- m is the number of rows
- n is the number of columns
- p is the number of digits in the matrix

# Day 4 - Scratchcards
## Part 1 
Just intersect the sets and use the number of common elements as exponent for the power of two. Et voilà!

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(n)           | O(1)           |



