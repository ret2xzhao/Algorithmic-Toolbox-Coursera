# Uses python3
import sys

"""
def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result
"""

def knapSack(total_w, per_weight):
    value = per_weight
    num = len(per_weight)
    diagram = [[0 for i in range(total_w+1)] for x in range(num+1)]
    for i in range(num+1):
        for j in range(total_w+1):
            if i==0 or j==0:
                diagram[i][j] = 0
            elif per_weight[i-1] <= j:
                diagram[i][j] = max(diagram[i-1][j-per_weight[i-1]]+value[i-1], diagram[i-1][j])
            else:
                diagram[i][j] = diagram[i-1][j]
    return diagram[num][total_w]

if __name__ == '__main__':
    input = sys.stdin.read()
    total_w, n, *per_weight = list(map(int, input.split()))
    print(knapSack(total_w, per_weight))
