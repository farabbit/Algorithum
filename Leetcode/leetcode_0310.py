"""
题目
对于一个具有树特征的无向图，我们可选择任何一个节点作为根。图因此可以成为树，在所有可能的树中，具有最小高度的树被称为最小高度树。给出这样的一个图，写出一个函数找到所有的最小高度树并返回他们的根节点。

格式
该图包含 n 个节点，标记为 0 到 n - 1。给定数字 n 和一个无向边 edges 列表（每一个边都是一对标签）。
你可以假设没有重复的边会出现在 edges 中。由于所有的边都是无向边， [0, 1]和 [1, 0] 是相同的，因此不会同时出现在 edges 里。

分析
具有树特征的无向图-> 没有环
-> 一定有度为1的节点
-> 循环删除度为1的节点

思路 - 一层一层剥开洋葱
1. 将边数组转化为节点字典
    * key: 节点，value: 所有与该节点相连的点（set）
2. 初始化队列q，将所有度为1的节点加入其中
3. 循环从字典中删除在队列中出现的点
    * 从与这些点相连的点的value中去掉该节点
    * 若这些被相连的点value度变为1，加入预备队列t
    * 完成一轮循环后，使q=t
"""

import collections
class Solution:
    def findMinHeightTrees(self, n: int, edges):
        if not edges:
            return [0]
        nodeDict = collections.defaultdict(set)
        for a,b in edges:
            nodeDict[a] |= {b}
            nodeDict[b] |= {a}
        q = set(n for n in nodeDict if len(nodeDict[n])==1)
        while len(nodeDict) > 2:
            t=set() # 预备队列
            while q:
                n = q.pop()
                n2 = nodeDict[n].pop()
                nodeDict[n2].remove(n)
                del nodeDict[n]
                if len(nodeDict[n2]) == 1:
                    t |= {n2}
            q=t
        return [i for i in nodeDict]