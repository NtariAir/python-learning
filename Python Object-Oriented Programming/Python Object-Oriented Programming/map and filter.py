def more_five(x):
	return x > 5
arr = [1, 10, 2, 15, 3, 5, 6]
filt_arr = list(filter(more_five, arr))
print(filt_arr)

