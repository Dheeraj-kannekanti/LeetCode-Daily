class Solution:
    def decodeString(self, s: str) -> str:
        num_stack , str_stack = [],[]
        current_num,current_str = 0,""
        for ch in s:
            if ch.isdigit():
                current_num = current_num*10+int(ch)
            elif ch=='[':
                num_stack.append(current_num)        
                str_stack.append(current_str)        
                #to initial values again
                current_num,current_str = 0,""
            elif ch==']':
                prev_str=str_stack.pop()
                num = num_stack.pop()
                current_str = prev_str+current_str*num
            else:
                current_str+=ch

        return current_str
