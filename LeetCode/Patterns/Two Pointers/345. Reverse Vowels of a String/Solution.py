class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        left = 0
        right = len(s)-1
        result = list(s)
        while left<right:
            if result[left] not in vowels:
                left+=1
            elif result[right] not in vowels:
                right-=1
            else:
                result[left],result[right]=result[right],result[left]
                left+=1
                right-=1
        return "".join(result)
        