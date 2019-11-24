"""
题目
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

分析
遍历字符串，使用滑动窗口记录字串长度，保存最大窗口的大小

思路
创建标记位start记录窗口起始位置，maxLen记录历史最大窗口
创建记录当前字符是否存在于窗口的字典/集合
遍历字符串，i为窗口末端位置
若字符在集合中：将start置于最后出现该字符的位置+1
若不在列表中：将字符加入集合
"""

"""
执行用时 :76 ms, 在所有 python3 提交中击败了76.70%的用户
内存消耗 :13.9 MB, 在所有 python3 提交中击败了5.01%的用户
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s:
            start = maxLenth= 0
            CharDic = {}
            for i in range(len(s)):
                if s[i] not in CharDic:
                    maxLenth = max(maxLenth, i-start+1)
                elif start<=CharDic[s[i]]:
                    maxLenth = max(maxLenth, i-CharDic[s[i]])
                    start=CharDic[s[i]]+1
                else:
                    maxLenth = max(maxLenth, i-start+1)
                CharDic[s[i]] = i
            return maxLenth
        return 0
