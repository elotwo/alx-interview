#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    change = 0 
    for coin in coins:
        if total <= 0:
            break
        change += total // coin
        total = total % coin
    if total != 0 :
        return -1
    return change               
