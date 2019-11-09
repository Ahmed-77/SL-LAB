lst = [12,24,35,70,88,120,155]

lst = [i for i in lst if i%2==0]

print("list after removing the odd numbers:\n",lst)

for i in lst:
	if i%5==0:
		print(i," is divisibe by 5")
	if i%7==0:
		print(i," is divisible by 7")
	if i%5!=0 and i%7!=0:
		print(i," is neither divisible by 5 nor by  7")
