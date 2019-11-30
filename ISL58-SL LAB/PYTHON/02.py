class person:
 def __init__(self,name,age):
  self.name = name;
  self.age=age;

p1= person("Suppandi",14)

print(" \n Name of person is",p1.name)
print("\n Age of person is",p1.age)

print("\n***Printing after deleting age attribute***\n")
del p1.age #Deleting the age attribute
print ("\n Name of person 1 is",p1.name)

print ("\n*** Printing after deleting name for p1***")
del p1
print("\nName of person #1 is")

