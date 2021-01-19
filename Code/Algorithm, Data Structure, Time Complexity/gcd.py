def gcd(a, b):
    while(a*b!=0):
        if a>b:
            a = a%b
            b = b%a
    return a+b

print(gcd(12,8))