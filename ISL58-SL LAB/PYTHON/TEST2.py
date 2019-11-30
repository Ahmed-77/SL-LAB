dict={
	"1MS17IS001":"AMAN",
	"1MS17IS002":"Ayush",
	"1MS17IS003":"Aditya",
	"1MS17IS004":"Pranjal",
	"1MS17IS014":"Himanshu"
      }
list = [] 
for key in dict.keys(): 
        list.append(key) 
#print(l1)
for i in range (0,len(list)):
	#print(l1[i])
	a=list[i]
	#print(a)
	b=int(a[7:10])
	#print(b)
	if(b%2==0):
		print(list[i])
		print(dict.get(a))
