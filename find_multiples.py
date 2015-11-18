def find_multiples(n):
	count = 0
	for i in range(n):
		if i%3==0 or i%5==0:
			count+=i
	return count

print(find_multiples(10))
print(find_multiples(1000))