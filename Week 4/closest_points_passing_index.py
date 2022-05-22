# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt
import random
import time


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def minimum_distance_squared(points):

    sorted_by_x = sorted(points, key = lambda x: x[0]) # sort by first (x) element of tuple O(nlogn) time
    sorted_by_y = sorted(points, key = lambda x: x[1]) # sort by second (y) element of tuple O(nlogn) time


    def min_dist_sqd_partition(left, right):
        if right-left < 1:
            return float("inf")
        elif right-left == 1:
            return distance_squared(sorted_by_x[left], sorted_by_x[right])
        else:
            # recursive calls to get minimum within-half-array distance O(log n) time
            mid = (left+right) //2
            min_left_sqd_distance = min_dist_sqd_partition(left, mid)
            # print("min_left_sqd_distance:", min_left_sqd_distance)
            min_right_sqd_distance = min_dist_sqd_partition(mid+1, right)
            # print("min_right_sqd_distance:", min_right_sqd_distance)

        min_within_array_sqd_distance = min(min_right_sqd_distance, min_left_sqd_distance)
        # print("min_within_array_sqd_distance:", min_within_array_sqd_distance)

        # now get the minimum between-half-array distance
        # find the midpoint between the far left and far right elements

        mid_line_x_coord = (sorted_by_x[mid][0] + sorted_by_x[mid+1][0]) / 2
        # print("mid_line_x_coord:",mid_line_x_coord)
        # print("minimum x coord:", mid_line_x_coord-sqrt(min_within_array_sqd_distance))
        # print("maximum x coord:", mid_line_x_coord+sqrt(min_within_array_sqd_distance))

        # define a strip of width 2 x sqrt(min_within_array_sqd_distance) centred on midline
        # and get a list of points in that strip from the sorted-by-y array
        mid_strip_points = [point for point in sorted_by_y if mid_line_x_coord-sqrt(min_within_array_sqd_distance) <= point[0] <= mid_line_x_coord+sqrt(min_within_array_sqd_distance)]
        # print("mid_strip_points:",mid_strip_points)
        # for each point in that mid-strip, get the distance to (up to) the next 7 points
        # in order of y coordinate. We only need to check 7 points because
        # at maximum 8 points can exist in a matrix of 8 squares (2 row x 4 column) each
        # of side 1/2 x sqrt(min_within_array_sqd_distance) without being closer to one another
        #than sqrt(min_within_array_sqd_distance) - a contradiction
        min_between_array_sqd_distance = float("inf")
        for i in range(0, len(mid_strip_points)-1):  # check each point in the mid-strip, stopping at the 8th to last point O(n) time
            # print("i:",i)
            for j in range(i+1, min(len(mid_strip_points), i+7)): # compare with next 7 points
                # print("j:",j)
                # if (mid_strip_points[i][1] - mid_strip_points[j][1]) < sqrt(min_between_array_sqd_distance):
                min_between_array_sqd_distance = min(min_between_array_sqd_distance, distance_squared(mid_strip_points[i], mid_strip_points[j]))

        return min(min_within_array_sqd_distance, min_between_array_sqd_distance)

    return min_dist_sqd_partition(0, len(points)-1)



# if __name__ == '__main__':
#     input_n = int(input())
#     input_points = []
#     for _ in range(input_n):
#         x, y = map(int, input().split())
#         input_point = Point(x, y)
#         input_points.append(input_point)
#
#     print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
# #


# testing_points = [Point(4, 4), Point(-2, -2), Point(-3, -4), Point(-1, 3), Point(2, 3), Point(-4, 0), Point(1, 1), Point(-1, -1), Point(3, -1), Point(-4, 2), Point(-2, 4)]
# testing_points = [Point(-9, -2), Point(-4, -8), Point(-4, -1), Point(-1, 7), Point(1, 10), Point(1, 6)]
# # testing_points = [Point(0, 0), Point(3, 4), Point(5, 4)]


def generate_test_cases(TEST_LENGTH=10, number_of_tests=10):
    all_tests = []
    for i in range(number_of_tests):
        all_tests.append([])
        lst1 = [random.randint(-10**9, 10**9) for i in range(TEST_LENGTH)]
        lst2 = [random.randint(-10**9, 10**9) for i in range(TEST_LENGTH)]
        for j in range(TEST_LENGTH):
            all_tests[i].append(Point(lst1[j], lst2[j]))
    return all_tests

number_of_tests = 50
TEST_LENGTH = 1000
list_of_big_points = generate_test_cases(TEST_LENGTH, number_of_tests)

tic = time.perf_counter()
for i in range(number_of_tests):
    print(sqrt(minimum_distance_squared(list_of_big_points[i])))
toc = time.perf_counter()
print(f"Ran {number_of_tests} test cases of length {TEST_LENGTH} in {toc - tic:0.8f} seconds")
print(f"Average time of {((toc - tic) / number_of_tests) } seconds")

# print(sqrt(minimum_distance_squared_naive(testing_points)))
# print(sqrt(minimum_distance_squared(testing_points)))

# for i in range(0, len(testing_points)-1):  # check each point in the mid-strip
#             print("i:",i)
#             for j in range(i+1, min(len(testing_points), i+8)): # compare with next 7 points
#                 print("j:",j)
#                 print(testing_points[i], testing_points[j])
