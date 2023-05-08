# returns positive index position of value if found, else reutrns -1
def binary_search(arr: list, search_value) -> int:
    upper_bound = len(arr) - 1
    lower_bound = 0
    search_index = (int)((upper_bound - lower_bound) / 2)
    found_index = -1
    continue_loop = True

    # need do while here, DNE in python
    while (continue_loop):
        if (arr[search_index] == search_value):
            continue_loop = False
            found_index = search_index
        elif (search_value > arr[search_index]):
            lower_bound = search_index + 1
        else:
            upper_bound = search_index - 1

        search_index = ((int)((upper_bound - lower_bound) / 2)) + lower_bound

        # do-while loop
        if (upper_bound < lower_bound):
            continue_loop = False

        print("upper_bound: ", upper_bound, " lower_bound: ", lower_bound, end='\n\n')

    return found_index