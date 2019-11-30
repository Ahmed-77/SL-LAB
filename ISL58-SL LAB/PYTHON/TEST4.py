dict={'O':'OXYGEN', 'N':'NITROGEN', 'C':'CARBON'}
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

#elname=input("Enter element for symbol retrieval : ").upper()
#if elname in list(dict.values()):
#	for i in dict:
#		if dict[i]==elname:
#			print (i)
