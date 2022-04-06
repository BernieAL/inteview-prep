"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


"""

"""

SOLUTIONS
        #Approach 1
        For each price in prices
            check if price is lowest we've seen so far -> minpriceSeen = min(minp,prices[i])
            calc current profit using minpriceSeen -> currProfit = prices[i] - minpriceSeen
            check if current profit is highest we've seen for far -> maxProfSeen = max(maxProfSeen,currProfit)
            
        #Apprach 2 - Using Kadanes -> get max subarray
        For each price in prices
            calc profit between i and and i-1 -> prices[i] - prices[i-1]
            check if profit less than 0, if so, take 0 take whichever is greater as currMax -> currMax = max(0,currMax)
            check if currMax is highest we've seen so far -> maxProfSeen = max(maxProfSeen,currMax)

"""



"""
SOLUTION 1 APPROACH:


Iterate prices
    minp->track lowest price seen
    calc profit if we bought at current price and sold at min price
    track maxp calcualte so far


For each price in prices:
    see if its the lowest price we've seen for far
    calc current profit by selling at current price -> price-minp
    see if the calculated profit is the largest we've seen for far
"""

def maxProfit(prices):
    
    maxp = 0
    minp = float('inf')

    for price in prices:
        minp = min(minp,price)
        profit = price-minp
        maxp = max(maxp,profit)

    return maxp



"""

SOLUTION 2 USING KADANES ALGO

logic for this problem is same as max subarray problem using kadanes algo

logic:
    calc difference of original array and find a contiguous subarray giving max profit
    if the different falls between 0, reset it to 0
        calll different (maxCur += prices[i] - prices[i-1])
"""

def maxProfit2(prices):
    maxCur = 0
    maxSoFar = 0

    for i in range(len(prices)):
        maxCur += prices[i] - prices[i-1]
        maxCur = max(0, maxCur)
        maxSoFar = max(maxCur,maxSoFar)
    
    return maxSoFar