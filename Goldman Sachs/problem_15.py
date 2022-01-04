def canPair(nums, k):
    n=len(nums)
    if n%2:
        return False
    for i in range(n):
        nums[i]%=k
    nums.sort()
    cnt=nums.count(0)
    if cnt%2:
        return False
    nums=nums[cnt:]
    n-=cnt
    for i in range(n//2):
        if (nums[i]+nums[n-i-1])%k:
            return False
    return True
if __name__=='__main__':
    print(canPair([9, 5, 7, 3],6))
