import CH_2.sorting as sorting
import random_number_functions.rand_num_fxns as ran_num_fxns

def main():
    rand_arr: list[int] = ran_num_fxns.generate_unordered_rand_list()
    print('random Arr: ', end="\n\t")
    print(rand_arr, end="\n\n")

    sorted_arr: list[int] = sorting.selection_sort(rand_arr, 'asc')
    
    print('selection_sort: ', end="\n\t")
    print(sorted_arr, end='\n\n')

    sorted_arr = rand_arr.copy()
    sorted_arr.sort()

    print('built in sort: ', end='\n\t')
    print(sorted_arr, end='\n\n')

if __name__ == '__main__':
    main()
