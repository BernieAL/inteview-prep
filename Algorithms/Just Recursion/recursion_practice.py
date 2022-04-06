"""
https://leetcode.com/problems/combination-sum-iv/

Given an array of distinct integers nums and a target
 integer target, return the number of possible combinations that add up to target.

"""

# def sumToK(nums,k):

#     res = set()
    
#     #use for loop to get through all elements in nums
#     def dfs(k,nums,path):

#         if k == 0:
#           res.append(path.copy)
#           return 0

#         for i in range(len(nums)):
#             return 1 + dfs(k-nums[i],nums,path.append(nums[i]))

#         return len(res)
#     return dfs(6,nums,[])

# nums = [1,2]
# print(sumToK(nums,4))



# ==================================


"""
reverse an array - printing w/ slicing
"""

# def go(nums):
#     if not nums:
#         return 0
#     print (nums[-1])
#     go(nums[:-1])

# nums = [1,2,3]
# go(nums)   


"""
reverse array 
"""


# ================================================

"""
palindrome check using 2 var

using 2 var"""
def pal(l,r,S):
    pass
    
# S = "MACAM"
# n = len(S)
# print(pal(0,-1,S))


""" 
Palindrome check using 1 var

"""


"""
backtracking subsequence pattern

Taking and not taking

"""
def go(idx,path,nums,res):

    res.append(path.copy())
    if idx == len(nums):
        res.append(path.copy())
        return res

    path.append(nums[idx])
    go(idx+1,path,nums,res)
    path.pop()
    go(idx+1,path,nums,res)

nums = [3,1,2]
res = []
print(go(0,[],nums,res)) 