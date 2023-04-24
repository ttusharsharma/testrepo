a=int(input("enter first number"))
b=int(input("enter second number"))
for i in range(max(a,b),(a*b)+1):
    if i%a==i%b==0:
        lcm=i
        print("lcm is ",lcm)
        break
