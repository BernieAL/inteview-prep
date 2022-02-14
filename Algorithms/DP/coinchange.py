"""
return the min number of ways to make the amount

backtracking dfs approach
    explore until dead end, then return up one level to prev call
    check for unexplored paths, explore those until dead end
    Repeat until all paths have been explored

    for amt 5 and 2 options to make 5
    we end up with 10 rec calls

    5-1 -> 4-1 -> 3-1 -> 2-1 -> 1-1 -> hit 0, stop and return, explore unexplored   
    perform same thing but on the way back up to 5 and subtracting 2 now
"""


"""
APPROACH:

We want to find the min # of coins needed to make the target amount
For each coin, we have the option to TAKE/USE the coin, which decreases the amount by the value of the coin
    amount - coin[i]
Or we have the option to skip the coin all together

DETAILS:
    Each coin has inifinite supply -> a single coin can be used infinite times, theres no use constraint
    2 options for each coin, take and use and skip
    we are looking for min combo of coins to make target amount

    because we are looking the minimum number of coins to make the target,
    we need to explore all possible options, find the min, and return it

    We do this by fully exploring the paths for all coins.
        the 2 paths for each coin are:
            if we kept taking the same coin, can we hit the target amount with current coin value?
                or is it not possible, meaning, we would exceed the the target coin value 
            if we didnt take the current coin value at all and moved onto next coin


        using idx to iterate through coins
             we perform a rec call not taking the current coin, and increment idx to next coin
                    ---> go(i+1,T)
             we perform a rec call taking the current coin:
                         if and only if current coin value is less than equal to target
                         subtract coin value from target amount
                         we stay at same coin and do not increment idx
                         and attach '1+' to the rec call to keep count of the num of coins used 
                    ---> 1+go(i,T-coins[i])


                        
"""

def minCoins(coins,T):

    def go(i,T):
        
        if T == 0:
            return 0
        if i == len(coins):
            return 1e9
        
        #simulate not taking curr coin
        """
        this call we are going to next coin without TAKING IT
        """
        res = go(i+1,T)

        #simulate taking current coin
        """
        only peform take coin and peform rec call if current coin is less than or equal to T
        if its greater than, dont take because will end up with T < 0
        we are adding 1 to the call as a way of saying we are taking an addtl coin
        the '1+' keeps track of the num of coins taken

        in this step we also compare the result from not taking to the result of taking
        and return the min
        """
        if coins[i] <= T:
            res = min(1+go(i,T-coins[i]),res)
        return res

        

    return go(0,T)
coins = [1,2,3]
print(minCoins(coins,7))

# ===============================================

#TOP DOWN MEMO 