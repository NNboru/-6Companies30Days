def lastPosition(n, m, k):
    if m <= n-k+1:
       return m+k-1
    m = m - (n - k + 1)
    if m%n == 0:
        return n
    else:
        return m % n

if __name__=='__main__':
    print(lastPosition(5,8,2))
