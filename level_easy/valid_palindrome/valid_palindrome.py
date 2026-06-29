class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        sLower = s.lower()
        for char in sLower :
            if char.isalnum() :
                result.append(char)

        return result == result[::-1]
