# CS310 Lab 4

Code and writeup by Ayden Diel.

## Q1

**O(n\*log(n)) + O(amount)** - **n** coins are sorted using merge sort, and then the 
whie loop runs **amount** times.

This solution was my original intuition for the problem, and checking online validated 
this intuition. First, the denominations are sorted in non-increasing order. Then, the 
largest coin value that's less than or equal to the remaining amount is subtracted from 
the remaining amount until the remaining value is 0. The number of subtractions from 
the original `amount` is tracked, and that is the value that gets returned.

This is a greedy approach because it makes the best choice for the given step without 
considering how the choice will affect future steps.

## Q2

**O(n\*log(n))** - **n** activities to sort using merge sort.

For this problem, based on what the professor said in the final lecture, I made the 
following assumptions to start out with:

1. Any given individual can  work a maximum of **8 hours in a given day**.
2. Task can be completed at **any time**, and the start/end times should be used 
    to calculate the **amount of time that it takes to complete a given task**,
    rather than when the task must be started and stopped.

## Q3

**O(n)** - Iterate through the list of jumps one time.

For this problem I had to do some research because I really could not come up with 
a solution. I found that you can actually start from the end of `nums` and work your 
way backwords, so rather than checking if every element can reach the end, you can 
find the closest element to the end that can reach it, and set that to be the new 
target. We continue this until we get to the first element, and check if it can 
reach any of the elements that can somehow reach the end.

## Q4

**O(nlogn)** - Merge sort is used on the items to sort them in order of value.

This is very similar to the coin problem, but rather than picking the largest capacity
that will fit in the bag, we pick the item with the largest value that will fit in 
the bag.

## Q5

**O(n + m)** - Where `n` is the total number of arrivals / departures, and `m` is 
               the maximum departure time.

This solution creates an array with an entry for each time unit (minutes), adding one 
and subtracting one from the minute corresponding to each arrival/departure time. With 
this array representation, to find the number of platforms at any given time, you can 
take the cumulative sum from the start until any given minute to find the number of 
platforms needed at that point in time.

To find the maximum number of trains in the station at any given time, we can take the 
cumulative sum for the entire array in a for loop, and use a variable called `result` to 
keep track of the max number of trains seen so far. Finally, we return `result`.

## Q6
