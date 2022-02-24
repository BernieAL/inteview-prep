"""
Find all duplicates in array and return as list



check if i is not at index nums[nums[i]-1] and check that the value at nums[i-1]
is not i already


Option 2 is to mark the element at n-1 as negative
and if we come across an element that is marked negative already
we add it res array as a duplicate



"""


"""
nums[i] gets the element at i
nums[i]-1 gets the element at position [i] and subtract 1 from it
nums[i-1] get the element at position [i-1]
nums[nums[i]-1] gets the index at position nums[i]-1

"""




def findDuplicates(nums):
     

    #ALTERNATE USING element iteration instead of index (num in nums vs i in range(len(nums)))
    
    ans = []
     for num in nums:
        #check if value at correct index is less than 0 (num = 4 -> 4-1 = 3, 3 is where 4 should go)
        if nums[abs(num)-1] < 0:
            ans.append(abs(num))
        else:
            nums[abs(num)-1] *= -1
    return ans
     
    ans = []
    for i in range(0,len(nums)):
       curr_element = abs(nums[i])
       print(f"curr_element{curr_element}")
       #this gets the value at index of where curr_element should be
       #we mark this value negative to mark that curr element exists in the array 
       
       val_at_indexToBeChecked = nums[curr_element - 1]
       print(f"val_at_indexToBeChecked:{val_at_indexToBeChecked}")
       
       if val_at_indexToBeChecked < 0:
           ans.append(curr_element)
       else:

            nums[curr_element-1] *= -1

    print(ans)

nums = [4,3,2,7,8,2,3,1]
findDuplicates(nums)


# print(nums[2]-1) #--> 5
# print(nums[2-1]) #--> 4
# print(nums[nums[2]-1]) #--> 3 (first 3)
    #this gets the correct index for where an element should go

