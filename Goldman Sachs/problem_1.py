# problem 1

def anagrams(words, n):
    def cal_hash(word):
        h=[0]*26
        for i in word.lower():
            h[ord(i)-97]+=1
        s=''
        for ind,cnt in enumerate(h):
            if cnt:
                s+= chr(97+ind)+str(cnt)
        return s

    grps = {}
    for word in words:
        h = cal_hash(word)
        if h in grps:
            grps[h].append(word)
        else:
            grps[h]=[word]

    return grps.values()

if __name__=='__main__':
    N = 5
    words = ['act','god','cat','dog','tac']
    grps = anagrams(words,N)
    for i in grps:
        print(*i)
    
