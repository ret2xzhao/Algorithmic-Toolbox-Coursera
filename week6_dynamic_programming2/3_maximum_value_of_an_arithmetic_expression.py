# Uses python3

def evalt(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        assert False

def min_and_max(i, j, op, M, m):
    min_num = float("inf")
    max_num = float("-inf")
    for k in range(i, j):
        a = evalt(M[i][k], op[k], M[k+1][j])
        b = evalt(M[i][k], op[k], m[k+1][j])
        c = evalt(m[i][k], op[k], M[k+1][j])
        d = evalt(m[i][k], op[k], m[k+1][j])
        min_num = min(min_num, a, b, c, d)
        max_num = max(max_num, a, b, c, d)
    return (min_num, max_num)

def get_maximum_value(dataset):
    #write your code here
    digit = dataset[::2]
    op = dataset[1::2]
    n = len(digit)
    m = [[0]*n for i in range(n)]
    M = [[0]*n for i in range(n)]
    for i in range(n):
        m[i][i] = int(digit[i])
        M[i][i] = int(digit[i])
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j, op, M, m)
    return M[0][n-1]

if __name__ == "__main__":
    print(get_maximum_value(input()))
