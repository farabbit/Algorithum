"""
题目

分析
持续循环计算
如果结果是1 return Ture
如果这个数已经计算过 return False -> 否则会无限循环

思路
记录平方避免重算
去重 -> 若正在算的数在set中存在，返回False

"""

class Solution:
    def isHappy(self, n: int) -> bool:
        def v1(n):
            history = set()
            while n not in history:
                summ = sum(int(i)**2 for i in (str(n)))
                if summ == 1:
                    return True
                history.add(n)
                n=summ
            return False

        # merge n==1 and n!=1
        def v2(n):
            history = {1}
            while n not in history:
                summ = sum(int(i)**2 for i in (str(n)))
                history.add(n)
                n=summ
            return n==1

        return v2(n)