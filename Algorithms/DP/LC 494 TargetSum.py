"""

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

"""


"""
APPROACH 

Given a list of nums, we want to add them together in such a way 
to reach Target T, and are asked to return how many ways we can do it

We can take the negative and positive versions of each number in the list
This is a combinations problem because we are asked how many combinations can we make that
satisify the criteria of summing to Target T

In this problem, for each element, we have 2 choices, to take it as positive or a negative
so we need to build out 2 paths recursively:
    if we took the current element as negative
    if we took the current element as positive

This is a combinations counting problem where we use the 
0 and 1 return pattern to keep count of how many combinations satisfy the condition

we use idx to iterate through list
and we use currsum to maintian a running sum to keep track if we hit the target

WE need to use ALL elements in each combination
so we cant just hit the target and still have elements left over

so our base cases are 
    if our idx has gone through all elements, AND our currsum == target
        RETURN 1 - because we have found a combination that satisifies the criterea
    if our idx has gone through all elements and currsum != target,
        RETURN 0 - invalid state - we've gone through all elements in the in list
            for this recursive call and we're not able to sum to the target

we will now have 2 recursive calls
    one where we take the current element as negative
    one where we take the current element as positive

The "little work" done before the next TWO recursive calls is:
    we advance idx to the next element in the list
    we add/subtract the current nums[idx] element to sum

    we use 2 variables to hold the results to the 2 recursive calls
    and return their sum at the end.
"""

#BRUTE FORCE REC NON DP
def TargetSum(nums,t):

    def go(idx,currsum):
        
        #BASE CASES
        #VALID STATE
        if idx == len(nums) and currsum == t:
            return 1

        #INVALID STATE
        #currsum != t implicitly checked
        if idx == len(nums):
            return 0

        #perform rec calls taking nums[idx] as negative by subtracting from currsum
        take_neg = go(idx+1,currsum-nums[idx])
        #perform rec calls taking nums[idx] as positive by adding to currsum
        take_pos = go(idx+1,currsum+nums[idx])

        #sum all the 1's and 0's returned from both rec calls
        return take_neg + take_pos
    
    #initial call to rec function starting at idx 0 of list and with currsum of 0
    return go(0,0)

# nums = [1,1,1,1,1]
# T = 3
# print(TargetSum(nums,3))

# =======================================================

# TOP DOWN MEMO DP VERSION
"""

The above solution is brute force. 
we end up solving the same sub problems more than once
So instead, we can just solve a problem once, store its solution for look up later
to save some time

use hashmap to store the # of ways to reach target sum from 
current index and current element
mapping index,current element to # of ways to reach target


"""

def TargetSumMemo(nums,T):

    
    memo = {}
    

    def go(idx,currsum):
        
        #check if we calculated # of ways to reach T from
        #curr idx and curr sum
        if (idx,currsum) in memo:
            return memo[(idx,currsum)]

        if idx >= len(nums) and currsum == T:
            return 1
        
        if idx >= len(nums):
            return 0
        
        take_neg = go(idx+1,currsum-nums[idx])
        take_pos = go(idx+1,currsum+nums[idx])

        memo[(idx,currsum)] = take_neg + take_pos
        return memo[(idx,currsum)]
        
    return go(0,0)

nums = [1,1,1,1,1]
T = 3
print(TargetSumMemo(nums,3))