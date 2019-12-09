"""
题目
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

优化暴力解法
分析
1. i < j < t, ai > aj, 必有v(i,t) >= v(j,t)，舍去aj
2. ai*(n-t) <= max, 舍去ai
最好情况：数列递减，时间复杂度O(n)
最差情况：数列递增，时间复杂度O(n^2)

思路
数组leftList，记录容器左边界可能的值，highestLeft记录表中左边界最大值
max记录当前最大容量，maxLeft, maxRight记录最大结果中左右边界值
遍历ai，计算leftList中与ai的乘积，用最大值覆盖max, maxLeft, maxRight
    若ai>highestLeft，加入leftList中


双指针法
分析
用双指针从两端开始移动，每次将移动较短的那根指针向内移动，并记录maxV
i<j<t,
    若Hi>Ht，则Vit > Vjt
移动较短的那根才有意义
时间复杂度O(n)
"""

class Solution:
    def maxArea(self, height) -> int:
        if len(height) < 2: return 0

        def bruteForce(height):
            leftList, highestLeft = {}, 0
            maxV = 0
            for i, h in enumerate(height):
                for left in leftList:
                    volumn = (i-left)*min(leftList[left], h)
                    maxV = max(volumn, maxV)
                if h>highestLeft:
                    highestLeft=h
                    leftList[i]=h
            return maxV

        def doublePointer(height):
            maxV=0
            i, j = 0, len(height)-1
            while i!=j:
                maxV = max(maxV, (j-i)*min(height[i], height[j]))
                if height[i] > height[j]: j-=1
                else: i+=1
            return maxV
        return doublePointer(height)