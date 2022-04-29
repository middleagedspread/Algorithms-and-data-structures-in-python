def biggest_two_numbers(number_list):
    n = len(number_list)
    biggest = max(number_list[0], number_list[1])
    second_biggest = min(number_list[0], number_list[1])
    for number in number_list:
        print(number, biggest, second_biggest)
        if biggest < number:
            second_biggest = biggest
            biggest = number
    return biggest, second_biggest

def max_pairwise_product(numbers):
    first, second = biggest_two_numbers(numbers)
    n = len(numbers)
    max_product = first * second
    return max_product

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
