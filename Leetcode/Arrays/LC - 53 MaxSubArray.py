# class Solution:
#     """
#     use D&C approach to keep halving the the array into left and right subarrays
#     each time checking for max in left and right
    
    
#     we use a helper recursive function to split 
#     keep halving the arrays into left and right
    
#     in the rec function we find max of left subarray
#     and max of subarray
    
#     then call the function again to further reduce the halves 
#     and find max of both again
    
#     keep going until i == j
#     at which point we have all single element arrays
#     """    
    
#     def maxSubArray(self, nums):
        
#         return helper(nums,0,len(nums)-1)
    
    
#         #keep halving array until single element arrays
#         #we want to get max sum of each subarray, so we keep generating the subarrays by halving
#         helper(nums,i,j):
            
#             #if single element array, return single element
#             if i == j:
#                 return nums[i]
    
#             #get mid of current array
#             mid = (i+j)//2
            
#             cs = 0
#             leftMaxSum = 0
#             rightMaxSum = 0
            
#             for L in range(mid,-1,-1):
#                 cs += nums[L]
#                 if cs > leftMaxSum:
#                     leftMaxSum = cs
            
#             #reset cs now for right half
#             cs = 0
#             for R in range(mid+1,j):
#                 cs+=nums[R]
#                 if cs > rightMaxSum:
#                     rightMaxSum = cs
            
#             #rec call with new updated bounds for halves
#             maxLeftRight = max(helper(i,mid),helper(mid+1,j))
#             return max(maxLeftRight,leftMaxSum+rightMaxSum)
        
cs = -2
a= 1

a,b = 0,1

print(a)