# Given a length and width number positive integer (truncates decimals), 
# 	will return the largest possible squares that could compose the overall area
# Solved via recursion
# iteration_is tracks the stack position of the recursive call--> for visual/debugging
def largest_subsquare__recursion(length: int, width: int, iteration_is: int)->list[int]:
	# truncate to int
	length = int(length)
	width = int(width)

	# ensure positive
	if (length < 0 or width < 0):
		return -1, -1

	# testing
	iteration_is += 1
	
	

	large = max(length, width)
	small = min(length, width)
	remainder = large % small

	print('larger: ', str(large), '\tsmaller: ', small, '\tstack: ', str(iteration_is))

	if (remainder == 0):
		# found answer, return
		print('R==0: ', large, str('----'), small, 'stack: ', str(iteration_is))
		return small, small
	else:
		# no answer, process then move forward
		large = remainder
		print('R!=0: \t', large, str('X'), small, '\tstack: ', str(iteration_is))
		large, small = largest_subsquare__recursion(large, small, iteration_is)
		print('popping: \t', large, str('X'), small, '\tstack: ', str(iteration_is))
		return large, small
