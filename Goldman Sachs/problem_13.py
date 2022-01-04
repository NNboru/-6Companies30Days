def decodedString(s):
    n=len(s)
    def process(ind):
        nonlocal s
        ans=''
        while ind<n and s[ind]!=']':
            c=s[ind]
            if ord(c)<97:
                j=ind
                while s[j]!='[':
                    j+=1
                c = s[ind:j]
                ss,ind = process(j+1)
                ans+= ss*int(c)
            else:
                ans+=c
            ind+=1
        return ans,ind
    return process(0)[0]

if __name__=='__main__':
    s='11[b1[ca]]'
    print(decodedString(s))
