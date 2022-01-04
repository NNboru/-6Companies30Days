from heapq import *
def getNthUglyNo(n):
    s=set()
    h=[1]
    while n!=1:
        a=heappop(h)
        for i in (2,3,5):
            new = a*i
            if new not in s:
                s.add(new)
                heappush(h,new)
        n-=1
    return heappop(h)

if __name__=='__main__':
    print(getNthUglyNo(10))
