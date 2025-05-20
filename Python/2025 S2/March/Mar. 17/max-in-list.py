def max_int_in_list(my_list):
    biggest_int_so_far = my_list[0]
    for current_int in my_list:
        if current_int > biggest_int_so_far:
            biggest_int_so_far = current_int
    return biggest_int_so_far

my_list = [5, 2, -5, 10, 23, -21]
biggest_int = max_int_in_list(my_list)
print(f"The biggest integer in the list is: {biggest_int}") # This will print: The biggest integer in the list is: 23

another_list = [-10, -20, -3, -50]
largest = max_int_in_list(another_list)
print(f"The biggest integer in the second list is: {largest}") # This will print: The biggest integer in the second list is: -3

one_more_list = [100]
maximum = max_int_in_list(one_more_list)
print(f"The biggest integer in the third list is: {maximum}") # This will print: The biggest integer in the third list is: 100