# Advent of Code 2023

# Day One -  Trebuchet?!
## Part 1
The solution for the part one is straightforward, we just iterate over the line moving two pointers, one pointing at the start of the line and the second pointing at its tail. When we found an index containing a digit, we stop updating the corrisponding pointer and when the first digit form the tail and the first digit from the head are found, we are done. 
| Time Complexity | Space Complexity |
|-----------------|------------------|
| O(n)            | O(1)             |


