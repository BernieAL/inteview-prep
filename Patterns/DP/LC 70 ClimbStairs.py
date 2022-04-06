"""
Climb n stairs by 1 or by 2

"""

#BASIC DFS APPROACH
def climbstairs(N):
    def go(i,N):
        if i == N:
            return 1
        if i > N:
            return 0
        return (go(i+1,N) + go(i+2,N))
    
    return go(0,N)

# N = 5
# print(climbstairs(5))


#TOP DOWN MEMO VERSION
def climbstairsMemo(N):

    memo = {} # i:num of ways to reach N from current i

    def go(i):
        
        if i in memo:
            return memo[i]
        if i == N:
            return 1
        if i > N:
            return 0
        
        memo[i] = (go(i+1)+go(i+2))
        return memo[i]
    return go(0)
# N = 5
# print(climbstairsMemo(5))


#BOTTOM UP DP VERSION
"""
starting from base case where we are at Nth step
one represents the number of ways to reach Nth step from current position by 1
two represents the number of eways to reach the Nth step from current position by 2

Ex. If we are at 5
    one = 1
    two = 1

"""


def climbstairsBottomUp(N):

    one,two = 1,1

    for i in range(N-1):
        temp = one
        one = one+two
        two = temp
    return one
N = 5
print(climbstairsBottomUp(5))