def dict_operation(dict):
	print("Original Dictionary :", dict)

	sym=input("Enter Unique Symbol : ").upper()
	dict[sym]=input("Enter Name : ").upper()
	print(dict,"\n")

	print("Number of terms in Dictionary :",len(dict))

	print("\n")
	sym=input("Enter Symbol for element retrieval : ")
	if sym in dict:
		print (dict[sym])
	else:
		print("element not present")


dict={'O':'OXYGEN', 'N':'NITROGEN', 'C':'CARBON'}
dict_operation(dict)
