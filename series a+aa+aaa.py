a=int(input("enter range"))
s=input("enter number for series")
sum=0
for i in range(1,a+1):
    b=s*i
    sum+=int(b)
print(sum)