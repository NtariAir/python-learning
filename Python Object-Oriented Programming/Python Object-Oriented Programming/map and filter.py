print("====\tMAP\t====")
def add_five(x,y,z):
	return x*y/z
	
nums = [11, 22, 33, 44, 55, 600]
arr2 = [1,   2,  3,  4,  5]
delit = [1,2,16,26]
result = list(map(add_five, nums, arr2, delit))
print(result) #[16,27,38,49,60]

print("====\tfilter\t====")
def more_five(x):
	return x > 5
arr =  [1, 10, 2, 15, 3, 5, 6]
filt_arr = list(filter(more_five, arr))
print(filt_arr)

