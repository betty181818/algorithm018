class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in (range(len(digits)-1,-1,-1)):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
                if i == 0: # 是第一位，并等于 9
                    digits.insert(0, 1) # Python 可利用 insert 将数组长度加 1
                    return digits