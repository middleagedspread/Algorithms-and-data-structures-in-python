# naive and very slow implementation (n*n-1)/2 operations

def max_pairwise_product_fast(number_list): 
    number_product = 0
    for i in range(0,len(number_list)): # for each number in list
        for j in range(i+1, len(number_list)): # for each number remaining after i
            number_product = max(number_product, number_list[i]* number_list[j])
    return number_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))


