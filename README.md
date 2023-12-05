# Advent of Code 2023

# Day One -  Trebuchet?!
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
