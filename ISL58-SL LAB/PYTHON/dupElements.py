def remove_duplicates(numbers):
	newlist = []
	for number in numbers:
		print(number)
		if number not in newlist:
			newlist.append(number)
		
	print(numbers)
	print(newlist)
	return newlist

# python 2
#list = raw_input("Enter the elements").split(",")

# python 3
s = input()
list = list(map(int,s.split()))
#remove_duplicates([1,2,3,4,4,4,5,5,6,7,8,8,8,8,9])
remove_duplicates(list)
