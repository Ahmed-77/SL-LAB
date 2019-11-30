class Student:
	def __init__(self,name="Aman",age=20):
		self.name = name
		self.age = age
		self.marks = [100, 100, 100]
	def display(self):
		print("Name :", self.name)
		print("Age :", self.age)
		print("Marks in three subject :", self.marks)

	def entry(self):
		print("Modify Data :")
		self.name = input("Enter new name :")
		self.age = input("Enter new age :")
		self.marks[0] = int(input("Enter marks#1 :"))
		self.marks[1] = int(input("Enter marks#2 :"))
		self.marks[2] = int(input("Enter marks#3 :"))
st1=Student()
while True:
	res=int(input('Enter Response (1-display, 2-modify, 3-quit) :'))
	if res == 1:
		st1.display()
	elif res ==2:
		st1.entry()
	elif res ==3:
		exit(0)
	else:
		print("Invalid Response")

