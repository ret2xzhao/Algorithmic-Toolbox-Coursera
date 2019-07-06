#Uses python3
import sys
import math
import random

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return str([self.x,self.y])

def construct_point(x_list, y_list):
    return [Point(x_list[i], y_list[i]) for i in range(len(x_list))]

def distance(Point_a, Point_b):
    return math.sqrt((Point_a.x - Point_b.x)**2 + (Point_a.y - Point_b.y)**2)

def calculate_small_region(points):
    if len(points) == 2:
        return distance(points[0],points[1])
    result = sys.maxsize
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            result = min(result, distance(points[i],points[j]))
    return result

def pre_process(x_list, y_list):
    points = construct_point(x_list, y_list)
    points = sorted(points, key=lambda a: a.x)
    return points

def minimum_distance(points):
    #sorted by the x-coordinates
    if len(points) <= 3:
        return calculate_small_region(points)
    mid = len(points) // 2
    left_side_min_dis = minimum_distance(points[0:mid])
    right_side_min_dis = minimum_distance(points[mid:])
    min_dis_in_small_region = min(left_side_min_dis, right_side_min_dis)
    split_vertical_line = (points[mid-1].x + points[mid].x)/2

    middle_area_point = []
    #for the left part:
    for i in range(len(points[0:mid])):
         if abs(points[i].x - split_vertical_line) <= min_dis_in_small_region:
             middle_area_point.append(points[i])

    # for the right part:
    for i in range(len(points[mid:])):
         if abs(points[mid+i].x - split_vertical_line) <= min_dis_in_small_region:
             middle_area_point.append(points[mid+i])

    middle_area_point = sorted(middle_area_point, key = lambda a: a.y)
    result = min_dis_in_small_region
    for i in range(len(middle_area_point)):
        for j in range(i+1, min(i+8, len(middle_area_point))):
            if abs(middle_area_point[i].y - middle_area_point[j].y) <= result:
                result = min(result, distance(middle_area_point[i], middle_area_point[j]))

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = pre_process(x,y)
    print("{0:.9f}".format(minimum_distance(points)))
