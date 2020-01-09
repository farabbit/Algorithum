"""
题目：相同的树
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

思路：遍历两棵树，DFS, BFS
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q) -> bool:
        def DFS(p, q):
            if p is None or q is None:
                return p==q
            return (p.val==q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        def BFS(p, q):
            import queue
            que = queue.Queue()
            que.put((p, q))
            while not que.empty():
                first, second = que.get()
                if first is None or second is None:
                    if first!=second: return False
                    else: continue
                if first.val != second.val:
                    return False
                que.put((first.left, second.left))
                que.put((first.right, second.right))
            return True
        return BFS(p,q)