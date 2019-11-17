"""
分析：
两数和为target，若一个数确定，另一个数也能确定
每种输入只对应一个答案 --> 除两个整数外，没有与他们相同的数


思路
建临时数组diff，遍历nums，每遇到一个数i，若其在diff中，返回两个数的下标
若其不在diff中，将其加入diff
"""

class Solution:
    def twoSum(self, nums, target):
        diff = []
        for i, int1 in enumerate(nums):
            print(int1)
            print(diff)
            for t, int2 in enumerate(diff):
                if int1 == int2:
                    return i, t
                diff.append(target-int1)
                print(diff)
            print("here")

print(Solution().twoSum([2,7,11,15], 9))
