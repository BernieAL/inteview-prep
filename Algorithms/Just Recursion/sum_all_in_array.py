"""

This function will sum all numbers in given array and return

    base case:
        if array is empty
        
    Recursive case:
        each rec call we're passing in modified list starting from i+1: to end of list
        we are summing the calls to the current element
        return array[i] + go(array[i+1:])

State variables that tell us what state we are is index i
using index i, we keep reducing the input array, reducing the number of elements until there are no more elements to get / array is empty

"""



# def driverFunc(nums):

#     def findSum(nums):
#         #if nums is empty - could be given as empty or we could have gone through all elements
#         if len(nums) == 1:
#             return nums[0]
#         return nums[0]+findSum(nums[1:])
    
#     return findSum(nums)
# nums = [1,2,3,4]
# print(driverFunc(nums))


def driver(nums):

    return findSum2(0,nums)

def findSum2(i,nums):
    if i == len(nums):
        return 0

    return nums[i] + findSum2(i+1,nums)

nums = [1,2,3,4]
print(driver(nums))