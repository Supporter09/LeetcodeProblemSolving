
def findWinners(matches):
    winners = []
    losers = []

    for match in matches:
        winner, loser = match
        if winner not in winners: 
            winners.append(winner)

        if loser in winners: 
            winners.remove(loser)

        if loser not in losers: 
            losers.append(loser)
        elif loser in losers:
            losers.remove(loser)

    return [winners, losers]
print(findWinners([[2,3],[1,3],[5,4],[6,4]]))
