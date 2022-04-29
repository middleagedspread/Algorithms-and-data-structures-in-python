# compact version of pairwise product using sort method

def max_pairwise_product_sort(number_list): 
    n = len(number_list)
    number_list.sort() # uses sort so may not be very fast
    biggest = number_list[n-1]
    second_biggest = number_list[n-2]
    return biggest * second_biggest

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print("Sort method")
    print(max_pairwise_product_sort(input_numbers))
