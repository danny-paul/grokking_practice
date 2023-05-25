import CH_2.sorting as sorting
import random_number_functions.rand_num_fxns as ran_num_fxns
from  CH_3.recursion_practice import factorial_by_recursion
from CH_4.recursion_area_example import largest_subsquare__recursion

def main():
	ordered_rand_arr: list[int] = ran_num_fxns.generate_ordered_rand_list(2, 100, 400)

	length, width = largest_subsquare__recursion(ordered_rand_arr[0], ordered_rand_arr[1], 0)

	print('Given the area:\n\t', str(ordered_rand_arr[0]), ' x ', str(ordered_rand_arr[1]), '\n The largest subsquares that can compose this area is of size:\n\t', str(length), ' x ', str(width))


if __name__ == '__main__':
	main()
