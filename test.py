def buyChoco(prices, money):
    # Second way: O(n) => Iterate and find first and second smallest element
    first = 105
    second = 106
    for i in range(len(prices)):
        if prices[i] < first: 
            if prices[i] <= first < second:
                second = first
            first = prices[i]
            
        elif first <= prices[i] < second:
            second = prices[i]

    res = money - (first + second) if first + second <= money else money
    print(first, second)
    return res

buyChoco([69,91,78,19,40,13], 94)