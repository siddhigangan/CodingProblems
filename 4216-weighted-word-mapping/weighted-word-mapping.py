class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""
        for i in words:
            val = 0
            for j in range(len(i)):
                pos = ord(i[j].lower()) - ord('a')
                val+= weights[pos]
            val = val % 26
            letter = chr(97 + ((26 - val) - 1))
            res += letter
        return res
