def maxProfit(prices):
    if len(prices) == 1:
        return 0
    buy,sell = prices[0],prices[0]
    profit = sell-buy
    profits = [0]
    if len(prices) == 2:
        return max(0,prices[1]-prices[0])
    for i in range(1,len(prices)):
        if buy > prices[i]:
            buy,sell = prices[i],prices[i]
            profits.append(profit)
            profit = sell - buy
        elif sell < prices[i]:
            sell = prices[i]
            profit = sell - buy
        
    profits.append(profit)   

    return max(profits)