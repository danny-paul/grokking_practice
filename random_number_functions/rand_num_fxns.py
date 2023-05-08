import random

# produces unordered ranodm list to be returned
def generate_unordered_rand_list(size: int = 10, lower_limit: int = 0, upper_limit: int = 100)->list[int]:
    rand_arr = [-1]*size

    for index in range(0, size):
        rand_arr[index] = random.randrange(lower_limit, upper_limit)
    
    return rand_arr

def generate_ordered_rand_list(size: int = 10, lower_limit: int = 0, upper_limit: int = 100)->list[int]:
    unordered_arr: list[int] = generate_unordered_rand_list(size, lower_limit, upper_limit)
    unordered_arr.sort()
    return unordered_arr

