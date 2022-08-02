def Lcm(x,y):
    if x>y:
        big=x
    else:
        big=y
    while(True):
        if(big%x==0) and (big%y==0):
            lcm=big
            break
        big+=1
    return lcm
num1=23
num2=45
print(Lcm(num1,num2))