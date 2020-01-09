"""
Question
There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.

You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution. 

有 n 位用户参加活动，他们的 ID 从 0 到 n - 1，每位用户都 恰好 属于某一用户组。给你一个长度为 n 的数组 groupSizes，其中包含每位用户所处的用户组的大小，请你返回用户分组情况（存在的用户组以及每个组中用户的 ID）。

你可以任何顺序返回解决方案，ID 的顺序也不受限制。此外，题目给出的数据保证至少存在一种解决方案。

Analyse

Solution
Group people in a dictionary
unpack dictionay by using list comprehension and subsript(下标)
"""

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        resultDic = collections.defaultdict(list)
        for i,size in enumerate(groupSizes):
            resultDic[size].append(i)
        return [lst[i:i+size] for size, lst in resultDic.items() for i in range(0,len(lst),size)]
