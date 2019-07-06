# python3
import sys

def compute_min_refills(distance, tank, stops):
    # write your code here
    num_refill = 0
    current_refill = 0
    stops.insert(0,0)
    stops.append(distance)
    n = len(stops) - 1
    while current_refill < n:
        last_refill = current_refill
        if (stops[current_refill+1] - stops[last_refill]) > tank:
            return -1
        while (current_refill < n and (stops[current_refill+1] - stops[last_refill]) <= tank):
            current_refill = current_refill + 1
        if current_refill < n:
            num_refill += 1
    return num_refill

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
