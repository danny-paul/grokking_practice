# unsorted arr of integers and order as str of 'asc' or 'desc'
def selection_sort(unsorted_arr: list[int], order: str='asc'):
    if (len(unsorted_arr) == 0):
        return []
    
    start: int = 0
    end: int = len(unsorted_arr) - 1
    index: int = 0
    temp: int = 0

    while start < end:
        max_value_index: int = start
        index = start + 1
        
        # obtain index of largest (or smallest) remaining value
        while index <= end:
            if order == 'desc':
                # descending order, find max
                if unsorted_arr[max_value_index] < unsorted_arr[index]:
                    max_value_index = index
            else:
                # ascending order, find min
                if unsorted_arr[max_value_index] > unsorted_arr[index]:
                    max_value_index = index
            index += 1
        
        # swap positions for this iteration
        temp = unsorted_arr[start]
        unsorted_arr[start] = unsorted_arr[max_value_index]
        unsorted_arr[max_value_index] = temp

        # print('iteration[', str(start), ']:', str(max_value_index))
        start += 1
        
    return unsorted_arr