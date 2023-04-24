str1 = "This is Pyhton"
print("Slice of String : ", str1[1 : 4 : 1])
print("Slice of String : ", str1[0 : -1 : 2])


x = "python was developed by abcd and the latest version has been updated"
subx1 = x[0:8]
subx2 = x[19:34]
subx3 = x[6:]
subx4 = x[::2]
subx5 = x[::-1]
print(subx1)
print(subx2)
print(subx3)
print(subx4)
print(subx5)

num1 = 2
num2 = 1
num3 = 3
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)


strings = ['masks', 'maps', 'bears', 'messy', 'minus', 'massy', 'mules', 'messy', 'files']

result = [s for s in strings if s.startswith('m') and s.endswith('s') and len(s) == 5]

print(result)

a=[1,2,3,4,5,6,7,8,9]
res=[i for i in a if (i%2==0)]
print(res)



text = "the qUIck brown fox"
print(text.title())

st=input("enter no.")
revn= st[::-1]
print(revn)



class Employee():
   def __init__(self, name, salary, dep):
      self.name = name
      self.salary = salary
      self.dep = dep

   def displayEmployee(self):
      print("Name : ", self.name, ", Salary: ", self.salary, ", depatment: ", self.dep)


name = {}
salary = {}
dep = {}
emp = {}

n=int(input("enter no. of employees"))
for i in range(1, n+1):
   print("Enter Your Details for Employee %d" % (i))
   name[i] = input("Enter Your Name for employee:")
   salary[i] = float(input("Enter Your Salary for employee:"))
   dep[i] = input("Enter Your department for employee:")
   emp[i] = Employee(name[i], salary[i], dep[i])

for i in range(1, 3):
   emp[i].displayEmployee()
   print("____________________________________________________")


def sum(a):
   if a == 0:
      return 0
   else:
      return a + sum(a - 1)


res = sum(10)
print(res)



class vehicle:
	def __init__(self,name,id):
		self.name=name
		self.id=id
		print("vehicle class")
# child class
class bus(vehicle):
	def __init__(self,name,id,make,fuel):
		super().__init__(name,id)
		self.make=make
		self.fuel=fuel
	def display(self):
		print(self.name)
		print(self.id)
		print(self.make)
		print(self.fuel)

a = bus("rahul",8989,2010,"cng")

# calling a function of the class Person using its instance
a.display()
