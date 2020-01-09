"""
题目
将非负整数转换为其对应的英文表示。可以保证给定输入小于 2^31 - 1 。

代码来自StefanPochmann
"""

class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def helper(num):
            if num < 20:
                return to19[num - 1:num] # a[-1:0] = '' <-> -1~0 not exist
            if num < 100:
                return [tens[num // 10 - 2]] + helper(num % 10)
            if num < 1000:
                return [to19[num // 100 - 1]] + ["Hundred"] + helper(num % 100)
            for p, w in enumerate(["Thousand", "Million", "Billion"], 1):
                if num < 1000 ** (p + 1):
                    return helper(num // 1000 ** p) + [w] + helper(num % 1000 ** p)

        return " ".join(helper(num)) or "Zero"
