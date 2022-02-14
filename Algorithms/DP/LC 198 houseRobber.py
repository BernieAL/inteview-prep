"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police

"""

"""
SOLUTION GUIDE
https://leetcode.com/problems/house-robber/discuss/1605797/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP

"""


"""
APPROACH

If we rob current house, we cant rob next, but can rob after that
if we dont rob current, we can rob next

Recurrence relation is
    if we rob current house
        rob(i+2) + nums[i]
        where nums[i] is the loot value of current house we are taking

    if we dont rob current house
        rob(i+1)
    
To calc max loot
    max(rob(i+2)+nums[i], rob(i+1))

Base case is:
    if i >=len(nums)


we say rob(i+2) + nums[i]
because if we are adding the current houses loot value 
to the return of this call
and BECAUSE we are taking the current house, the next index to rob 
is i+2 since we cant rob houses next to eachother

the other option is we dont rob the current house and therefore
we can do i+1 to get to the next house
"""

#BRUTE FORCE
from re import L


def houseRobber(nums):

    def go(idx):

        if idx >= len(nums):
            return 0
        
        return max(go(idx+2)+nums[idx],go(idx+2))
    
    return go(0,0)

nums = [1,2,3,1]
print(houseRobber(nums))


# ==============================================================
"""
TOPDOWN MEMO DP

We use memo to store what the max loot is at current index
memo = {} #idx: max loot up to current idx

Time Complexity : O(N), We calculate the result for each index only once & there are N indices. Thus overall time complexity is O(N).
Space Complexity : O(N), required for dp and implicit recursive stack.
"""

def houseRobber(nums):
    memo = {} #idx: max loot up to current idx

    def go(idx):

        if idx in memo:
            return memo[idx]

        if idx >= len(nums):
            return 0
        memo[idx]= max(go(idx+2)+nums[idx],go(idx+1))
        return memo[idx]
    return go(0)
# ================================================
"""
BOTTOM UP ITERATIVE TABULATION

instead of recursing from top down until we hit a base case
we come up from the base case and compute values as we go

we use a dp array to save the results of computation
dp[i] is the max loot we can get up to index i
    at each index
        we can keep rob the current house and add it to loot we have at i-2 index
            dp[i-2]+nums[i]
        or we can keep not rob current house and keep same loot as prev index

Time Complexity : O(N), just single iteration is performed from 2 to N to compute each dp[i].
Space Complexity : O(N), required for dp.

"""

def houseRobber(nums):
    if len(nums) == 1:
        return nums[0]
    
    dp = [*nums]
    dp[1] = max(nums[0],nums[1])
    for i in range(2,len(nums)):
        dp[i] = max(dp[i-2]+nums[i],dp[i-1])
    return dp[-1]

"""
Space-Optimized BOTTOM DP
we only need to keep that last 2 values in memory 

Time Complexity : O(N)
Space Complexity : O(1), only constant extra space is used.

"""
def rob(nums):
    prev2,prev,cur = 0,0,0

    for i in nums:
        cur = max(prev,i+prev2)
        prev2 = prev
        prev = cur
    return cur