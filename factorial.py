def factorial(n):
	result = 1
	while n>=1:
		result = result * n
		n = n-1
	return result

print factorial(10)	
#more efficient than break