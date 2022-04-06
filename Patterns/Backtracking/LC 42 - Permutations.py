
def permutations(nums):
    path = []
    res = []


    # for i in range(len(nums)-1,-1,-1):
    #     print(nums[i])

    for i in range(len(nums)):
        path.append(nums[i])

        for j in range(i-1,-1,-1):
            print(nums[j])
            path.append(nums[j])

        for k in range(i+1,len(nums)):
            path.append(nums[k])
        
        res.append(path.copy())
        path.clear()
    return res

nums = [1,2,3]
print(permutations(nums))