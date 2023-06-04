# find largest positive integer
def find_max_value_arr(arr: list[int], largest_val: int = -1)->int:    
    # recursively move in array or return largest_value
    if (len(arr) == 0):
        return largest_val
    else: 
        # compare current to largest value
        if (arr[len(arr) - 1] > largest_val):
            largest_val = arr[len(arr) - 1]

        return find_max_value_arr(arr[0:len(arr) - 1], largest_val)
