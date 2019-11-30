def remove_duplicates(numbers):
	newlist = [] 
	for number in numbers:
		if number not in newlist:
			newlist.append(number);
  


 	print(newlist);
 	return newlist
remove_duplicates( [1,2,3,4,5,5,6,3,2] )
