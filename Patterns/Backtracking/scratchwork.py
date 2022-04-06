def permute(nums):
        res = []
        dfs(nums, [], res)
        return res

def dfs( nums, path, res):
        if not nums:
            res.append(path)
            #return # backtracking
        print(path)
        for i in range(len(nums)):
            dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

nums = [1,2,3,4]
print(permute(nums))