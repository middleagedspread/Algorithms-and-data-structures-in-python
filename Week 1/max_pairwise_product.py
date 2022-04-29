
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
    
    for i in range(2,n): #compare biggest to remaining elements
        if number_list[i] >= biggest: # if the next number is bigger than biggest
            second_biggest, biggest = biggest, number_list[i] #update both biggest and second biggest
        elif number_list[i] > second_biggest: # if it is only bigger than second biggest
            second_biggest = number_list[i] # update second_biggest
    return biggest * second_biggest # return the product of the two biggest numbers


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))


