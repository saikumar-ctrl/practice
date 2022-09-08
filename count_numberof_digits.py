#count number of digits in range first and second inclusivly
first=int(input())
second=int(input())
find=int(input())
count=0
for i in range(first,second+1):
    while i>0:
        if i%10==find:
            count=count+1
        i=i//10
print(count)
