def answer(t, n):

	# Holds the count for # of ways to reach each spot on the board
	counter = [0] * n
	counter[0] = 1
	
	# Go through each dice roll
	for roll in xrange(t):
		# Make a temporary counter to update
		temp = [0] * n
		temp[-1] = counter[-1]
		
		# Move through each position and update the possibilities
		for pos in xrange(n-1):
			# Stay
			temp[pos] += counter[pos]
			# Left
			if pos > 0:
				temp[pos-1] += counter[pos]
			# Right
			if pos < n-1:
				temp[pos+1] += counter[pos]
			
		# Update the counter
		counter = temp

	return counter[-1] % 123454321
