def bin_search_recursion(arr: list[int], find_int: int) -> True:
    print()
    mid_point = int(len(arr) / 2)

    print('MidPoint: ', mid_point)
    if (len(arr) == 0 or find_int == arr[mid_point]):
        # base case- not found or matched 
        if (len(arr) == 0):
            return False
        else:
            return True
    else:
        if find_int > arr[mid_point]:
            return bin_search_recursion(arr[(mid_point + 1): len(arr)], find_int)
        else:
            return bin_search_recursion(arr[0: (mid_point)], find_int)
        
    #binary search--> ordered arr, cuts in half, checks midpoint, moves accordingly
    # --> base case: when len(arr) == 0 or search_value == arr[midpoint]
     