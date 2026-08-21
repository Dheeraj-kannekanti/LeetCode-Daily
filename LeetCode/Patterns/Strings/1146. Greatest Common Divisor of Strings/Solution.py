import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ""
        a = len(str1)
        b = len(str2)
        while b:
            a,b = b,a%b
        gcd_length = abs(a)
        return str1[:gcd_length]
        