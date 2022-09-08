def hcf(a,b):
    while b:
        a,b=b,a%b
    return a
n=int(input())
n1=int(input())
a=hcf(n,n1)
print("hcf of two numbers",a)
print("lcm of two numbers,",n*n1/a)
