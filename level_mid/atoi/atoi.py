class Solution:
    def myAtoi(self, s: str) -> int:
        s_clean = s.strip()

        if not s_clean :
            return 0

        sign = 1
        if s_clean[0] == '-':
            sign = -1
        if s_clean[0] == '+':
            sign = 1

        result = ""
        i = 0
        if s_clean[0] in '+-' :
            i = 1

        for char in s_clean[i:] :
            if char.isdigit() :
                result += char
            else :
                break

        if not result :
            return 0

        result = sign * int(result)
        if result > 2**31 - 1:
            result = 2**31 - 1
        if result < -2**31 :
            result = -2**31

        return result
