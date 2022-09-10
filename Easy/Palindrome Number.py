class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        if num[0] == "-":
            return False
        if num == num[::-1]:
            return True
        else:
            return False
