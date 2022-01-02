# problem_2

def doOverlap(L1, R1, L2, R2):
    ans=0

    if L2[0]<L1[0]:
        L1, R1, L2, R2 = L2, R2, L1, R1
    if L2[0]<=R1[0]:
        ans+=1
    if R2[1]<R1[1]:
        L1, R1, L2, R2 = L2, R2, L1, R1
    if R2[1]<=L1[1]:
        ans+=1
    
    return int(ans==2)

if __name__=='__main__':
    L1=(0 ,10)
    R1=(10,0 )
    L2=(5 ,5 )
    R2=(15,0 )
    print( doOverlap(L1, R1, L2, R2) )
