"""
题目
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。 
给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
输入: 
    2
   / \
  2   5
     / \
    5   7
输出: 5
说明: 最小的值是 2 ，第二小的值是 5 。

分析
* 根为最小的值
* 若root != left != right
    * return min(left, right)
* 若root == left ( or root == right )
    * 返回secondMinimum(left)(若有)
    * 否则return right
* 若root == left == right
    * 返回min(secondMinimum(left), secondMinimum(right))

思路
别玩那么多花里胡哨的
多种情况时，使用多个if往往比将相近情况叠加更简洁
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root) -> int:
        def v1(root):
            if root.left is None:
                return -1
            if root.val != root.left.val and root.val != root.right.val:
                return min(root.left.val, root.right.val)
            if root.val == root.left.val == root.right.val:
                minLeft = self.findSecondMinimumValue(root.left)
                minRight = self.findSecondMinimumValue(root.right)
                return min(minLeft, minRight) if minLeft != -1 and minRight != -1 else max(minLeft, minRight)
            if root.val == root.right.val:
                root.right, root.left = root.left, root.right
            # root.left.val == root.val
            minLeft = self.findSecondMinimumValue(root.left)
            return min(minLeft, root.right.val) if minLeft != -1 else root.right.val

        def v2(root):
            if root.left is None: return -1

            left, right = root.left.val, root.right.val

            if root.val != left and root.val != right: return min(left, right)

            # 取左右子树第二小值
            if root.val == right: right = self.findSecondMinimumValue(root.right)
            if root.val == left: left = self.findSecondMinimumValue(root.left)

            if left == right == -1: return -1
            if right == -1: return left
            if left == -1: return right
            return min(left, right)
        return v2(root)