class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        replace_idx=0
        while i < len(chars):
            ch = chars[i]
            count = 0
            while i <len(chars) and ch == chars[i]:
                count +=1
                i+=1
            if count == 1:
                chars[replace_idx]=ch
                replace_idx+=1
            else:
                chars[replace_idx]=  ch
                replace_idx+=1
                for dig in str(count):
                    chars[replace_idx] = dig
                    replace_idx+=1
        return replace_idx
        