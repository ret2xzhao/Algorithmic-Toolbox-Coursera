# Uses python3
import sys

def get_change(money):
    #write your code here
    denominations = [1, 3, 4]
    min_num_coins = []
    min_num_coins.append(0)
    num_coins = 0
    for m in range(1, money+1):
        min_num_coins.append(sys.maxsize)
        for i in range(len(denominations)):
            if m >= denominations[i]:
                num_coins = min_num_coins[m-denominations[i]]+1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    return min_num_coins[money]

if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(get_change(money))
