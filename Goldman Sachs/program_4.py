def encode(arr):
    s=''
    a=arr[0]
    cnt=0
    for c in arr:
        if c==a:
            cnt+=1
        else:
            s+=a+str(cnt)
            cnt=1
            a=c
    s+=a+str(cnt)
    return s

if __name__=='__main__':
    print(encode('aaaabbbccc'))
