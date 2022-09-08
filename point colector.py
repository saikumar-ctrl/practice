def solve(N,list1,list2,ans):
    List=list1+list2
    List.sort()
    list1=List[:N]
    list2=List[N:]
    for i in list1:
        if i>0:
            ans=ans+1
        else:
            ans=ans-1
    for i in list2:
        if i>0:
            ans=ans+2
        else:
            ans=ans-2
    return ans
n=int(input())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
a=int(input())
print(solve(n,l,l1,a))