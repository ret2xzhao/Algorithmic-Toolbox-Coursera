#Uses python3
import sys

def largest_number_another(digits):
    #write your code here
    res = []
    for x in digits:
        for i in x:
            res.append(int(i))
    res.sort()
    res.reverse()
    sum = ''
    n = 0
    for i in range(len(res)):
        sum = sum + str(res[n])
        n = n + 1
    res = int(sum)
    return res

def is_greater(digit, max_digit):
    return digit + max_digit > max_digit + digit

def largest_number(digits):
    # write your code here
    res = ""

    while len(digits) > 0:
        max_digit = '0'
        for digit in digits:
            if is_greater(digit, max_digit):
                max_digit = digit
        res += max_digit
        digits.remove(max_digit)
    return int(res)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
