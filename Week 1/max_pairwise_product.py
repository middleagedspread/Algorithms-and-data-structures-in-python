#def max_pairwise_product(number_list): 
#    n = len(number_list)
#    number_list.sort() # uses sort so may not be very fast
#    biggest = number_list[n-1]
#    second_biggest = number_list[n-2]
#    return biggest * second_biggest

def max_pairwise_product(number_list): #a faster algorithm, requires n comparisons
    # parameter is a list of integers
    n = len(number_list)
    if n == 2: #if only two elements
        return number_list[0] * number_list[1]
    
    if number_list[0] > number_list[1]: #assign first two elements to biggest, second biggest
        biggest, second_biggest = number_list[0],  number_list[1]
    else:
        biggest, second_biggest = number_list[1],  number_list[0]
    
    for i in range(2,n): #compare biggest to remaining eleements
        if number_list[i] >= biggest:
            second_biggest, biggest = biggest, number_list[i]
    return biggest * second_biggest    

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
