"""

Houses are arranged in circle



we can solve using houseRobber 1 logic

we can say the answer cannot contain first and last answer
because they are adjacent -> because circular form

what if we leave out alst element in array and then consider the array
we are leaving out last possible elmenet

apply prev houserobber logic to array leaving out last possible element

we're going to do a call leaving out first element
and we're going to do a call leaving out last element
because we cant have answer including both the frist and last elements
since they are adjacent




"""
# ========================================

"""
run h1 function on 2 subarrays of input array   
    one array doesnt include first element -> (nums[1:])
    one array doesnt include last element ->  (nums[:-1])

"""

def houserRobber2(nums):

    def go(nums):
        rob1,rob2 = 0,0

        for n in nums:
            newRob = max(rob1 + n,rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2


    """
    
    """
    return max(nums[0],(nums[1:]),go(nums[:-1]))





# ==========================================
def houseRobber2(nums):

    temp1 = []
    temp2 = []
    n = len(nums)

    for i in range(n):

        #build sequence without first element
        if i != 0:
            temp1.append(nums[i])
        #build sequence without last element
        if i != n-1:
            temp2.append(nums[i])

    return max()

# ===========================================


def houseRobber2(nums):

    def go(i):
        rob,not_rob = 0,0
        for idx in range(i,j):
            rob = not_rob  + nums[idx]
            not_rob = max(rob,not_rob)
        return max(rob,not_rob)

    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        n = len(nums)
    
        
# nums = [1,2,3,1]
# print(houseRobber2(nums))

# ========================================