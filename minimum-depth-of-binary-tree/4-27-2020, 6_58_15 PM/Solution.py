// https://leetcode.com/problems/minimum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None or root.right is None:
            return max(self.minDepth(root.left),self.minDepth(root.right))+1
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1