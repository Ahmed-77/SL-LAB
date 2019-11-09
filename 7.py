def unique(num):
	lst = []
	for i in num:
		if i not in lst:
			lst.append(i)
	return lst
	
def isPrime(num):
	count = 0
	if num == 1:
		return False
	prime = True
	for i in range(2,num):
		if num%i == 0:	
			prime = False
			break
	return prime

lst = [1,2,2,3,4,4,5,6,7,7,8,9,10,11,1,11,12,12,23,45]

lst = unique(lst)

print("Unique numbers of the list are:",lst)

for i in lst:
	if isPrime(i):
		print(i," is prime")
	else:
		print(i,"is not prime")
