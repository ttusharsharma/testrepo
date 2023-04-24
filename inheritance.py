
class Person:
	def __init__(self,name,id):
		self.name=name
		self.id=id
		print("base class")
# child class
class Employee(Person):
	def __init__(self,name,id,salary,post):
		super().__init__(name,id)
		self.salary=salary
		self.post=post
	def display(self):
		print(self.name)
		print(self.id)
		print(self.salary)
		print(self.post)

a = Employee("rahul",8989,50000,"intern")
a.display()
