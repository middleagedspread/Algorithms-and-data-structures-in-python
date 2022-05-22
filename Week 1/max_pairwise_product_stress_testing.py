import random
from unittest import result

def max_pairwise_product_sort(number_list): 
    n = len(number_list)
    number_list.sort() # uses sort so may not be very fast
    biggest = number_list[n-1]
    second_biggest = number_list[n-2]
    return biggest * second_biggest

def max_pairwise_product_fast(number_list): #a faster algorithm, requires n comparisons
    # parameter is a list of integers
    n = len(number_list)
    if n == 1:
        return number_list[0] * 1
    if n == 2: #if only two elements
        return number_list[0] * number_list[1]
    
    if number_list[0] > number_list[1]: #assign first two elements to biggest, second biggest
        biggest, second_biggest = number_list[0],  number_list[1]
    else:
        biggest, second_biggest = number_list[1],  number_list[0]
    
    for i in range(2,n): #compare biggest to remaining eleements
        if number_list[i] >= biggest:
            second_biggest, biggest = biggest, number_list[i]
        elif number_list[i] > second_biggest:
            second_biggest = number_list[i]
    return biggest * second_biggest

def stress_test(array_size, max_number):
    while True:
        n = random.randint(2,array_size)
        test_nums = []
        for i in range(0,n):
            test_nums.append(random.randint(0,max_number))
        print(test_nums)
        result1 = max_pairwise_product_sort(test_nums)
        result2 = max_pairwise_product_fast(test_nums)
        if result1 == result2:
            print("OK")
        else:
            print("Wrong Answer")
            return   


stress_test(5,10)

