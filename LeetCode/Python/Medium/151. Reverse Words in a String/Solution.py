class Solution:
    def reverseWords(self, s: str) -> str:
        output = s.strip().split()
        l,r = 0,len(output)-1
        while l<r:
            output[l],output[r] = output[r],output[l]
            l+=1
            r-=1
        return " ".join(output)
