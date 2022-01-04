def minSubArrayLen(target: int, nums: list[int]) -> int:
    n=len(nums)
    l,r=0,1
    ans=n+1
    s=nums[0]
    if s>=target: ans=1
    while True:
        if s>=target:
            s-=nums[l]
            l+=1
        else:
            if r==n:
                break
            s+=nums[r]
            r+=1
        if s>=target:
            ans=min(r-l,ans)
    if ans==n+1:
        return 0
    else:
        return ans

if __name__=='__main__':
    print(minSubArrayLen(7,[2,3,1,2,4,3]))
