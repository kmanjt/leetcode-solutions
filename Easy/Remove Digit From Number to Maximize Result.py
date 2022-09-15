class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        count = number.count(digit)
        if count == 0:
            number = number.replace(digit, "")
            return number
        else:
            temp = 0
            for i, char in enumerate(number):
                if char == digit:
                    num = int(number[:i] + number[i+1:])
                    if num > temp:
                        temp = num
            return str(temp)
