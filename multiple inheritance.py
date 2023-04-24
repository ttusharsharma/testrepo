class company:
    def __init__(self):
        print("company :-eloitte")
class department1(company):
    def __int__(self,dep1):
        super()
        self.dep1=dep1
        print("dep1:child class 1")

    def display(self):
        print(self.dep1)
class department2(company):
    def __int__(self,dep2):
        super()
        self.dep2=dep2
        print("dep2:child class 2")

    def display(self):
        print(self.dep2)
a1=department1("HR")
a2=department2("IT")
a1.display()
a2.display()
