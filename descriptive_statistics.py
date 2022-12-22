import sys
import math

def mean(arr):
	# loop through list, add all #'s, divide by len
	if type(arr) != list:
		print("Please input a list as a string", file=sys.stderr)
	avg = 0
	for i in arr:
		avg += i
	avg = avg/len(arr)
	return avg

def median(arr):
	# check if len of list is even, if not: get middle #
	# if len is even, return avg of the 2 middle #'s
	if type(arr) != list:
		print("Please input a list as a string", file=sys.stderr)
	arr.sort()
	if len(arr) % 2 != 0:
		return arr[math.floor(len(arr)/2)]
	else:
		med = (arr[len(arr)/2 - 1] + arr[len(arr)/2 + 1]) / 2
		return med
	

def std_dev(arr):
	# std_dev = sqrt(sum((xi - u)^2)/(N-1))
	sd = 0
	sum_x_diff_squared = 0
	avg = mean(arr)
	for x in arr:
		sum_x_diff_squared += (math.pow((x - avg),2))
	sd = sum_x_diff_squared/(len(arr)-1)
	sd = math.sqrt(sd)
	return sd
	 


n = int(input("Enter number of elements: "))
input_ls = list(map(int,input("Enter the numbers (space seperated): ").strip().split()))[:n]


print("mean: ", mean(input_ls))
print("median: ",median(input_ls))
print("standard deviation: ",std_dev(input_ls))
