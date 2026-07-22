class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        cur_num = 0
        cur_str = ""

        for i in s:

            if i.isdigit():
                cur_num = int(i)

            elif i == "[":
                num_stack.append(cur_num)
                str_stack.append(cur_str)
                cur_num = 0
                cur_str = ""

            elif i == "]":
                num = num_stack.pop()
                prev = str_stack.pop()
                cur_str = prev + cur_str * num

            else:
                cur_str += i
                
        return cur_str
