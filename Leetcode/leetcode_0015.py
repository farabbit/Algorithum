"""
题目
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

排序+双指针
"""

import collections

class Solution:
    def threeSum(self, nums):

        # 排序+双指针
        def v2_sort_2pointer(nums):
            nums.sort()
            resultSet = set()
            for i,num in enumerate(nums[:-1]):
                left, right = i+1, len(nums)-1
                while left<right:
                    if (num, nums[left], nums[right]) in resultSet:
                        right -= 1
                        left += 1
                        continue
                    result = nums[left] + nums[right] + num
                    if result == 0:
                        resultSet.add((num, nums[left], nums[right]))
                        right -= 1
                        left += 1
                    elif result > 0:
                        right -= 1
                    else:
                        left += 1
            return resultSet

        class UnorderedTuple(tuple):
            def __hash__(self):
                sortedList = list(set(self))
                sortedList.sort()
                return tuple.__hash__(tuple(sortedList))
            
            def __eq__(self, other):
                if isinstance(other, self.__class__):
                    return self.__hash__()==other.__hash__()
                else:
                    return False


        # 两个数等一个数
        def v1(nums):
            dic = collections.defaultdict(set)
            resultSet = set()
            for i,num in enumerate(nums):
                resultSet |= {UnorderedTuple(nega+(num,)) for nega in dic[-num]}
                for prevNum in nums[0:i]:
                    dic[prevNum+num] |= {UnorderedTuple((prevNum, num))}
            return resultSet
        return v2_sort_2pointer(nums)

print(Solution().threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
