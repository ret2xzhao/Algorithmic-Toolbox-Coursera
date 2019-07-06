#Uses python3
import sys

def lcs2(s1 , s2):
    a = len(s1)
    b = len(s2) 
    L = [[None]*(b+1) for i in range(a+1)]
    for i in range(a+1):
        for j in range(b+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
    return L[a][b]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    s1 = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    s2 = data[:m]

    print(lcs2(s1, s2))
