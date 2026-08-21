class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        if len(s)==0:
            return True
        while j <len(t):
            if s[i]==t[j]:
                i+=1
                if len(s)==i:
                    return True
            j+=1
        return False
        
        