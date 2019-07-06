# Uses python3
import sys

def optimal_summands(n):
    summands = []  
    count = 1

    if n ==1 or n == 2:
        summands.append(n)
        return summands

    while n > 2 * count:
        summands.append(count)
        n = n - count
        count = count + 1
        if n <= 2 * count:
            summands.append(n)
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
