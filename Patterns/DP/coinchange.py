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

#BOTTOM UP DP - Kevin naughton

"""
Then we observed that this algorithm may compute coinChange of same amount 
for many times, which are kind of duplicate, if we can store 
"amount->fewest_coin_count" into hashtble, then we don't need to recompute 
again. Actually, this is DP (dynamic programming), aka. Memorization.

So the final solution is to add hashtbl implementation to the previous solution and problem solved, 
this is of upper time complexity O(n^c), which is polynomial:

"""

"""
Think of the problem as smaller subproblems
we're asked what is the fewest # of coins that we need to make some amount
    we can reduce this to, whats the smallest # of coins we need to make up 0
    and then 1 and 2 and so on.. up to original amount

Once smaller subproblems are solved, we can use them build the larger problem

APPROACH:
    we make a dp array that stores the fewest # of coins to make up current amount we are on
    we then initially fill up dp with invalid state of (amount+1)

    Whats the smallest subproblem we can solve? 
        the smallest subproblem would be what is the fewest coins we can use to make amount of 0
        the answer is just 0
        so we store the answer to this subproblem
            dp[0] = 0
        
    How do we continue solving for amounts from 0 to original amount size?
        we use a for loop
        one for loop for each subamount up to original amount
        and one for loop for each coin in coins

    Ok so?
        For each subamount leading up to original amount
            for each coin in coins
                if the current coin value is less than current subamount
                    compare and store min of:
                        whatever dp[i] currently is
                        vs. 
                        actually taking the coin and subtracting current coin value from amount
        when the loop terminates, we have dp array entirely populated
        
        the dp array stores the min num of coins to make current amount i
        from 0 to original amount
        so if amount = 3
        dp[3] stores the fewest num of coins needed to make an amount of 3


"""

def minCoins(coins,amount):
    
    dp = [amount+1]*(amount+1)
    dp[0] = 0
    for a in range(1,amount+1):
        for c in coins:
            if a - c >=0:
                dp[a] = min(dp[a],1+dp(a-c))

    return dp[amount] if dp [amount]!= amount + 1 else -1
   