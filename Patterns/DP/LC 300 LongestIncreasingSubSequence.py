"""

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

"""


"""
https://leetcode.com/problems/longest-increasing-subsequence/discuss/300914/Python-DP-Easy
APPROACH::

comparing i and j
we are storing max LIS up tp current i


"""



def lengthOfLis(nums):

    dp = [1]*len(nums)

    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],1+dp[j])
    return max(dp)