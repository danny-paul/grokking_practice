def arr_summation(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0
    else:
        print('Stack Arr:', str(arr))
        return arr[len(arr) - 1] + arr_summation(arr[0:(len(arr) - 1)])