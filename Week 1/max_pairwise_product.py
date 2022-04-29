def max_pairwise_product(number_list):
    n = len(number_list)
    number_list.sort()
    biggest = number_list[n-1]
    second_biggest = number_list[n-2]
    return biggest * second_biggest

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
