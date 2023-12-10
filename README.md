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
|  O(n)           | O(p)             |

Where p are the numbers on each card

## Part 2 
This time we build a map where for each card we store its number of occurrences. The map is initially built counting each card once, than each time we found a winning card, we increment the number of occurrences of the won cards. 
When incrementing the number of occurrences of a card, we have to keep in mind that the increment must be weighted for the actual number of scratchcard we have won so far for a given card. 

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(n)           | O(n)             |

# Day 5: If You Give A Seed A Fertilizer 

## Part 1
Considering the limited number of seeds in input, we can just evaluate all the mappings and then grab the minimum)
| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(n)           | O(n+m)           |

Where: 
- n is the number of seeds in input
- m are the ranges in the maps

## Part 2
This time the number of seeds is not so small and a brute force approach would take too much time and memory. Even changing the implementation to store only the smallest location found while we evaluate the seeds, we wouyld solvi only the space problem, not the time one. 

The solution I found was the following: instead of mapping all the seeds in the input ranges and look for the minimum, do the opposite. Which is: start from the minimum location possible, map it back to an hypotetical corresponding seed and check if the seed is in one of the ranges in input. 

It is still quite a brute force approach, and potentially there can be more efficient and smart ways to solve the problem, but it is a fairly simple solution to code and give us back the result in less the a couple of seconds on my machine. 

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(l)           | O(m)             |

Where l is the number of locations between 0 and l_min that does not map into any of the input seed ranges

# Day 6: Wait For It

## Part 1
I think I can say that the solution I gave for this part of the problem is probably the worst solution one can find, but I leave it here to remind to myself that more often than not, the first idea you have is not the best idea you can have. 

My idea was: ok, the distance I can run at each millisecond is the distance of the previous millisecond plus the time I kept the button down... It seems tailored for a dynamic programming approach! So I made the worst dynamic programmi implementation of my life...

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(n^2)           | O(n^2)         |

## Part 2
... and soon I paid for that, as it was impossible to get a solution for part two with that starting point. 

So I started over again and did the math right this time: 
- The distance you make in the end of the race is all that matters to know if you are going to win or not
- The distance you can actually make in the end is tc * ta, where tc is the time the boat spend running and ta is the time you spend pressing the button
- for every ta where ta*tc is greater than the duration of the race, you have a new possibility to win

So this time we can brute force the solution without having to wait a life time. 

It is still a brute force solution, but is super easy to implement and runs in a couple of seconds and this is what metters in a competitive programming challange I guess

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(n)           | O(1)             |

# Day 7: Camel Cards

## Part 1
Given that the type fo the card making a point is not relevant, a QQQQQ is the same of a 22222 in a first moment, we can say that all that metters for determining the points in a hand is the number of occurrences of any given card in a hand, not considering which card has a give count number.

For example: 
```
>>> c = Counter("AAAJJ")
>>> c
Counter({'A': 3, 'J': 2})

```
And 
```
>>> c = Counter("QQQJJ")
>>> c
Counter({'Q': 3, 'J': 2})

```
Are totally equivalent points regardless the fact that we have 3 As in the first hand and 3 Qs in the second hand

When we compare euqlas points between to hands, in this case we use the alphabet: `AKQJT98765432` to determine which hand is the strongest one. 

So we can define a custom comparator for a hand that takes into account the aforementioned rules, sort the hands and use their index in the sorted array as a rank. 


| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(nlog(n))     | O(n)             |

Where the main time complexity cames from sorting the list of hands


## Part 2

We can totally use the same algorithm of part 1, we just need to: 
- update the hand to replace all the Js with the stronger point in the hand (taking into account that the hand 'JJJJJ' stays as it is
- change the alphabet used for the comparison of hands with the same point with: `AKQT98765432J`

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(nlog(n))     | O(n)             |


