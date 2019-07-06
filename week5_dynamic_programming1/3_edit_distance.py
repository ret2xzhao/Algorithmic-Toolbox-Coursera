# Uses python3
# Recurrence:
# D(i,j) = min:{D(i,j-1)+1
#               D(i-1,j)+1
#               D(i-1,j-1)+1 if A[i] =! B[j]
#               D(i-1,j-1)   if A[i] == B[j]}

def edit_distance(s, t):
    #write your code here
    diagram = [[0] * (len(s)+2) for i in range(len(t)+2)]
    a = 0
    a_index = 1
    b = 0
    b_index = 1
    for i in range(2, len(s)+2):
        diagram[0][i] = s[a]
        diagram[1][i] = a_index
        a += 1
        a_index += 1
    for j in range(2, len(t)+2):
        diagram[j][0] = t[b]
        diagram[j][1] = b_index
        b += 1
        b_index += 1

    #1_insertion
    #   diagram[i,j-1]+1
    #2_deletion
    #   diagram[i-1,j]+1
    #3_mismatch
    #   if diagram[i] =! diagram[j]:
    #   diagram[i-1,j-1]+1
    #4_match
    #   if diagram[i] == diagram[j]:
    #   diagram[i-1,j-1]
    for i in range(2,len(t)+2):
        for j in range(2,len(s)+2):
            if diagram[i][0] == diagram[0][j]:
                diagram[i][j] = diagram[i-1][j-1]
            elif diagram[i][0] != diagram[0][j]:
                diagram[i][j] = min(diagram[i][j-1] + 1,diagram[i-1][j] + 1, diagram[i-1][j-1] + 1)

    return diagram[i][j]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
