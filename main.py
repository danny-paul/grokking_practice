import CH_2.sorting as sorting
import random_number_functions.rand_num_fxns as ran_num_fxns
from  CH_3.recursion_practice import factorial_by_recursion
from CH_4.recursion_area_example import largest_subsquare__recursion
from CH_4.recursion_summation_example import arr_summation
from CH_4.recursion_find_max import find_max_value_arr
from CH_4.binary_search_recur import bin_search_recursion
def main():
	ordered_rand_arr: list[int] = ran_num_fxns.generate_ordered_rand_list(10, 10, 20)
	find_me: int = 12
	found_value_bool: bool = bin_search_recursion(ordered_rand_arr, find_me)

	print('With an array of:', str(ordered_rand_arr), ', we see that our search value of ', str(find_me), ' is/is not present:', str(found_value_bool))


if __name__ == '__main__':
	main()
