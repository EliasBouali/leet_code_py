class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]

        for word in strs[1:]:
            temp = ""
            for i, letter in enumerate(word):
                if i < len(result) and letter == result[i]:
                    temp += letter
                else :
                    break
            result = temp

        return result
