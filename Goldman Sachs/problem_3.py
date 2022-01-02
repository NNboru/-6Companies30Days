# problem_3

def cnt_subarr(a, n, k):
    p = 1
    res = 0
    start = 0
    end = 0
    while end < n:
        p *= a[end]
 
        while start < end and p >= k:
            p = p//a[start]
            start += 1
 
        if p < k:
            cnt = end - start + 1
            res += cnt
 
        end += 1
 
    return res

if __name__=='__main__':
    a = [1,2,3,4]
    n=4
    k=100
    cnt_subarr(a, n, k)
