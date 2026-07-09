class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        def expand(left, right) :
            while left >= 0 and right < len(s) and s[right] == s[left] :
                left -= 1
                right += 1
            return s[left+1:right]

        for i in range(len(s)) :
            odd = expand(i, i)
            even = expand(i, i+1)
            candidate = max(odd, even, key=len)
            if len(candidate) > len(result):
                result = candidate

        return result
