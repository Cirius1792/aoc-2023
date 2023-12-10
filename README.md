# Advent of Code 2023

- [Day 1 -  Trebuchet?!](#day-1-trebuchet)
   * [Part 1](#part-1)
   * [Part 2](#part-2)
- [Day 2 - Cube Conundrum](#day-2-cube-conundrum)
   * [Part 1 ](#part-1-1)
   * [Part 2](#part-2-1)
- [Day 3 - Gear Ratios](#day-3-gear-ratios)
   * [Part 1 ](#part-1-2)
   * [Part 2](#part-2-2)
- [Day 4 - Scratchcards](#day-4-scratchcards)
   * [Part 1 ](#part-1-3)
   * [Part 2 ](#part-2-3)
- [Day 5: If You Give A Seed A Fertilizer ](#day-5-if-you-give-a-seed-a-fertilizer)
   * [Part 1](#part-1-4)
   * [Part 2](#part-2-4)
- [Day 6: Wait For It](#day-6-wait-for-it)
   * [Part 1](#part-1-5)
   * [Part 2](#part-2-5)
- [Day 7: Camel Cards](#day-7-camel-cards)
   * [Part 1](#part-1-6)
   * [Part 2](#part-2-6)

<!-- TOC --><a name="day-1-trebuchet"></a>
# Day 1 -  Trebuchet?!
<!-- TOC --><a name="part-1"></a>
## Part 1
The solution for part one is straightforward, we just iterate over the line moving two pointers, one pointing at the start of the line and the second pointing at its tail. When we find an index containing a digit, we stop updating the corresponding pointer and when the first digit from the tail and the first digit from the head are found, we are done. 
| Time Complexity | Space Complexity |
|-----------------|------------------|
| O(n)            | O(1)             |

<!-- TOC --><a name="part-2"></a>
## Part 2
This time we are required to look for strings and not just for digits. We'll keep the same approach of iterating through each line from the head and the tail but will split the problem into two parts. 
1. First we will look for all the occurrences of the words that we are looking for in the line and then we will select the one located at the minimum possible index. 
2. Then we will do the same, but on the reversed string looking for the reversed words, this will be done using the same approach used in point 1

| Time Complexity | Space Complexity |
|-----------------|------------------|
| O(np) -> O(n)   | O(1)             |

where p is the number of patterns to match in the strings, which is 20 as we are looking for the digits or words stating numbers from zero to nine

<!-- TOC --><a name="day-2-cube-conundrum"></a>
# Day 2 - Cube Conundrum
<!-- TOC --><a name="part-1-1"></a>
## Part 1 
Given a target game, for each line of the input file, we check if the extractions in the line are compatible with the target game.
To do so, we gather the maximum number of cubes for each colour extracted during a game, let's call it a "minimum viable game", and compare those numbers with the one in the target game. 

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(n)           | O(1)             |


<!-- TOC --><a name="part-2-1"></a>
## Part 2
We use the minimum viable game found in part 1, which is our solution.

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(n)           | O(1)             |

<!-- TOC --><a name="day-3-gear-ratios"></a>
# Day 3 - Gear Ratios
I'll be honest, I struggled a bit with this one. 

<!-- TOC --><a name="part-1-2"></a>
## Part 1 
The flow of the algorithm is the following: 
1. Scan the matrix looking for anything but a digit, this is our symbol that "enables" the numbers in its surroundings. 
2. Once we find a symbol, we look in the cells around it for digits and store their positions. 
    Let's take a sub-matrix made as follows:
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

<!-- TOC --><a name="part-2-2"></a>
## Part 2
What changes in the algorithm described in part one are the following: 
1. We are no longer looking for anything but a digit in step 1, but we are looking only for '*'
2. In step 3, when we parse the numbers found in step two, we discard any * surrounded by more than three numbers

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(m*n)           | O(p)           |

Where:
- m is the number of rows
- n is the number of columns
- p is the number of digits in the matrix

<!-- TOC --><a name="day-4-scratchcards"></a>
# Day 4 - Scratchcards
<!-- TOC --><a name="part-1-3"></a>
## Part 1 
Just intersect the sets and use the number of common elements as the exponent for the power of two. Et voilà!

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(n)           | O(p)             |

Where p are the numbers on each card

<!-- TOC --><a name="part-2-3"></a>
## Part 2 
This time we build a map where for each card we store its number of occurrences. The map is initially built by counting each card once, then each time we find a winning card, we increment the number of occurrences of the won cards. 
When incrementing the number of occurrences of a card, we have to keep in mind that the increment must be weighted for the actual number of scratchcards we have won so far for a given card. 

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(n)           | O(n)             |

<!-- TOC --><a name="day-5-if-you-give-a-seed-a-fertilizer"></a>
# Day 5: If You Give A Seed A Fertilizer 

<!-- TOC --><a name="part-1-4"></a>
## Part 1
Considering the limited number of seeds in input, we can just evaluate all the mappings and then grab the minimum)
| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(n)           | O(n+m)           |

Where: 
- n is the number of seeds in the input
- m are the ranges in the maps

<!-- TOC --><a name="part-2-4"></a>
## Part 2
This time the number of seeds is not so small and a brute force approach would take too much time and memory. Even changing the implementation to store only the smallest location found while we evaluate the seeds, we would solve only the space problem, not the time one. 

The solution I found was the following: instead of mapping all the seeds in the input ranges and looking for the minimum, do the opposite. Which is: start from the minimum location possible, map it back to a hypothetical corresponding seed and check if the seed is in one of the ranges in input. 

It is still quite a brute force approach, and potentially there can be more efficient and smart ways to solve the problem, but it is a fairly simple solution to code and give us back the result in less the a couple of seconds on my machine. 

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(l)           | O(m)             |

Where l is the number of locations between 0 and l_min that do not map into any of the input seed ranges

<!-- TOC --><a name="day-6-wait-for-it"></a>
# Day 6: Wait For It

<!-- TOC --><a name="part-1-5"></a>
## Part 1
I think I can say that the solution I gave for this part of the problem is probably the worst solution one can find, but I leave it here to remind myself that more often than not, the first idea you have is not the best idea you can have. 

My idea was: ok, the distance I can run at each millisecond is the distance of the previous millisecond plus the time I kept the button down... It seems tailored for a dynamic programming approach! So I made the worst dynamic programming implementation of my life...

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(n^2)           | O(n^2)         |

<!-- TOC --><a name="part-2-5"></a>
## Part 2
... and soon I paid for that, as it was impossible to get a solution for part two with that starting point. 

So I started over again and did the math right this time: 
- The distance you make at the end of the race is all that matters to know if you are going to win or not
- The distance you can make in the end is tc * ta, where tc is the time the boat spends running and ta is the time you spend pressing the button
- for every ta where ta*tc is greater than the duration of the race, you have a new possibility to win

So this time we can brute force the solution without having to wait a lifetime. 

It is still a brute-force solution, but is super easy to implement and runs in a couple of seconds and this is what matters in a competitive programming challenge I guess

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(n)           | O(1)             |

<!-- TOC --><a name="day-7-camel-cards"></a>
# Day 7: Camel Cards

<!-- TOC --><a name="part-1-6"></a>
## Part 1
Given that the type of the card making a point is not relevant, a QQQQQ is the same as a 22222 in the first moment, we can say that all that matters for determining the points in a hand is the number of occurrences of any given card in a hand, not considering which card has a give count number.

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
Are equivalent points regardless of the fact that we have 3 As in the first hand and 3 Qs in the second hand

So we can compare two hands by doing the following: 
1. Compare the most common cards in each hand 
    If the most common card in a hand has, for example, occurrs 4 times and the most common card in the second hand occurrs 3 times, we already know that hands 1 wins. 
2. If both hands have the same number of occurrences for their cards, we start comparing the cards one by one by considering the priority between the cards being: `AKQJT98765432`

So we can define a custom comparator for a hand that takes into account the aforementioned rules, sorts the hands and uses their index in the sorted array as a rank. 


| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(nlog(n))     | O(n)             |

Where the main time complexity comes from sorting the list of hands


<!-- TOC --><a name="part-2-6"></a>
## Part 2

We can totally use the same algorithm as part 1, we just need to: 
- update the hand to replace all the Js with the stronger point in the hand, which will be the card that has the bigger occurrence count. We have also to take into account that the hand 'JJJJJ' stays as it is
- change the alphabet used for the comparison of hands with the same points with: `AKQT98765432J`

| Time Complexity | Space Complexity |
|-----------------|------------------|
|  O(nlog(n))     | O(n)             |


