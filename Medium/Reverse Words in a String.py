class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        
        res = []
        while words:
            res.append(words.pop())
        return " ".join(res)
