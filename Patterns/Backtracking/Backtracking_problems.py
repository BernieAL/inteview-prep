"""

https://leetcode.com/problems/combination-sum/discuss/429538/General-Backtracking-questions-solutions-in-Python-for-reference-%3A


https://leetcode.com/problems/combinations/discuss/844096/backtracking-cheatsheet-simple-solution

Backtracking is general algo for finding all or some solutions to 
computational problems
backtracking builds candidates that are potential solutions to the problem
and abandans a candidate(backtracks) as soon as it determines the candidate 
cannot lead to a valid solution

def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)


Candidate enumeration is done in 2 levels:
    at firs tlevel, the function is implemented as recurssion
    each occurence of recursion, the funcion is one step further towards final solution

    at second level, within recursion, we have an iteration that allows us to explore all
    candidates that are of the same progress to the final solution

"""


# ========================================================
"""
Explore all combinations of numbers from 1 to n of length k

"""

def combine(n,k):
    sol = []
    
    
    def backtrack(remain,comb,nex):
        #if solution found
        if remain == 0:
            sol.append(comb.copy())
        else:
            for i in range(nex,n+1):
                #add candidate
                comb.append(i)
                #backtrack
                backtrack(remain-1,comb,i+1)
                #remove candidate
                comb.pop
    backtrack(k,[],1)
    return sol

# print(combine(20,2))


# ========================================================

def subsets1(nums):

    res = []

    def dfs(nums,idx,path,res):
        res.append(path)
        for i in range(idx,len(nums)):
            dfs(nums,i+1,path+[nums[i]],res)
    
    dfs(nums,0,[],res)
    return res

def subsetsV2_NEETCODE(nums):
    
    res = []

    subset = []
    def dfs(i):
        
        if i >= len(nums):
            res.append(subset.copy())
            return 
        
        #decision to include nums[i]
        subset.append(nums[i])
        dfs(i+1)
        
        #decision not to include nums[i]
        #pop last added element
        subset.pop()
        dfs(i+1)    
    dfs(0)
    return res

nums = [1,2,3]
# print(subsets1(nums))
print(subsetsV2_NEETCODE(nums))
    
# ==============================================

# https://www.youtube.com/watch?v=DBLUa6ErLKw
# https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS)./307079
def permutations_general(nums):
    res = []
    
    def dfs(self,nums,path,res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)
    
    dfs(nums,[],res)
    return res



def permute_NEETCODE(nums):
    res = []

    if(len(nums) == 1):
        return [nums.copy()]
    
    for i in range(len(nums)):
        #pop first value from nums
        n = nums.pop(0)
        #get perms of reminaing values in nums
        perms = permute_NEETCODE(nums)

        for perm in perms:
            perm.append(n)
        res.extend(perms)
        #append popped value to permutations
        nums.append(n)
    return res
