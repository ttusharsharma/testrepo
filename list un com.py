list_a=input("enter the elements in list 1").split(" ")
list_b=input("enter the elements in list 2").split(" ")
com=[i for i in list_a if i in list_b]
print("common elements are",com)
un_a=[i for i in list_a if i not in list_b]
print("unique elements of first list are",un_a)
un_b=[i for i in list_b if i not in list_a]
print("unique elements of first list are",un_b)