#-------------------------ASSIGNMENT 1----------------------------------

l1=["html","javascript","python","ruby","perl"]

print("length of the list is " ,len(l1))                                    #Length of List

l2=l1									    #New list as an element of existing List
print("New List as an element of existing list ", l2)

l3=slice(1,7,2)								    #Slicing of List
print(l1[l3])

l1[1]="apple"								    #Replacing element in List
print("List after replacing second element",l1)
				
l4=l1+l2								    #Concatenation of List
print(l4)

l5=l1[ : ]								    #Method 1 to copy and clone a list
print(l5)

l6=list(l1)								    #Method 2 to copy and clone a list
print(l6)

l7=list()
l7.extend(l1)
print(l7)

lm=list(range(100))
step=10
l_chunk=[lm[i:i+10] for i in range(0,100,10)]
print ("Chunked list : ")
for i in l_chunk:
	print (i)

print("\n")


#---------------------------ASSIGNMENT 2------------------------------------

t1=("one","two","three")
print("First element of Tuple")
print(t1[0])
print("Tuple is:")
print(t1)
print("converting tuple to a list")
result = [] 
for t in t1: 
        result.append(t)
print(result) 





