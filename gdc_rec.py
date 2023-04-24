def gcd(a, b):
    if (a == 0):
        return b

    return gcd(b%a,a)

a = int(input("enter first number"))
b = int(input("enter second number"))
if (gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')