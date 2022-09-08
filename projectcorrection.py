def minProject(errorScore,compP,othQ):
    sai=True
    c=-1
    count=0
    while sai:
        c=c+1
        if sum(errorScore)!=0:
            count=count+1
        else:
            sai=False
        if errorScore[c]!=0 and errorScore[c]>=compP:
            errorScore[c]=errorScore[c]-compP
        else:
            errorScore[c]=0
        for i in range(len(errorScore)):
            if errorScore[i]>=1 and i!=c:
                errorScore[i]-=othQ
    return count
print(minProject(list(map(int,input().split())),int(input()),int(input())))


