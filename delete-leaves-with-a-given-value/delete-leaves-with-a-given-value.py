# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if (root.left != None):
            root.left = self.removeLeafNodes(root.left, target)
        if (root.right != None):
            root.right = self.removeLeafNodes(root.right, target)

            print("None")
        if (root.left == None and root.right == None):
            if (root.val == target):
                return None
        return root