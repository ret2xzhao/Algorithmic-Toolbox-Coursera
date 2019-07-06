#Uses python3
import sys

def lcs3(s1, s2, s3):
    m = len(s1)
    n = len(s2)
    o = len(s3)
    L = [[[None]*(o+1) for j in range(n+1)] for k in range(m+1)]

    """ Following steps build L[m+1][n+1][o+1] in bottom up fashion. Note that L[i][j][k]
    contains length of lcs3 of s1[0...i-1] and s2[0...j-1] and s3[0...k-1] """
    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if (i == 0 or j == 0 or k == 0):
                    L[i][j][k] = 0
                elif (s1[i-1] == s2[j-1] and s1[i-1] == s3[k-1]):
                    L[i][j][k] = L[i-1][j-1][k-1] + 1
                else:
                    L[i][j][k] = max(L[i-1][j][k], L[i][j-1][k], L[i][j][k-1]) 
    return L[m][n][o] 

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    s1n = data[0]
    data = data[1:]
    s1 = data[:s1n]
    data = data[s1n:]
    s2n = data[0]
    data = data[1:]
    s2 = data[:s2n]
    data = data[s2n:]
    s3n = data[0]
    data = data[1:]
    s3 = data[:s3n]
    print(lcs3(s1, s2, s3))
