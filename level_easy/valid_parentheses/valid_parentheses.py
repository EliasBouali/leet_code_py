class Solution:
    def isValid(self, s: str) -> bool:
        s_stack = []
        match = {")": "(", "]": "[", "}": "{"}

        for sign in s:
            if sign in match:
                if not s_stack:
                    return False
                test = s_stack.pop()
                if test != match[sign]:
                    return False

            else :
                s_stack.append(sign)

        return len(s_stack) == 0
