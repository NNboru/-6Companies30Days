import math as m
def gcdOfStrings(str1, str2):
        a,b = len(str1),len(str2)
        n = m.gcd(a,b)
        s= str1[:n]
        if s*(a//n) == str1 and s*(b//n) == str2:
            return s
        else: return ''
    


if __name__=='__main__':
    print(gcdOfStrings("ABABAB","ABAB"))
