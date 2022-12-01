import sys

def factorial(n):
	if type(n) != int:
		print("Please input an int.", file=sys.stderr)
	else:
		output = 1
		for i in range(1, n+1):
			output = output*i
		return output
		


n = int(input("Enter number: "))
print(factorial(n))

