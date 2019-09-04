class Student:
 def __init__(self,name,age,m1,m2,m3):
  self.name=name;
  self.age=age;
  self.m1=m1;
  self.m2=m2;
  self.m3=m3;

n1=input("Enter the name\n");
a1=input("Enter the age\n");
m=input("Enter the m1\n");
n=input("enter the m2\n");
u=input("Enter the m3\n");
p1=Student(n1,a1,m,n,u)
print (p1.name,p1.age,p1.m1,p1.m2,p1.m3)
