# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        left_leaf = []
        right_leaf = []
        self.dfs(root1 , left_leaf)
        self.dfs(root2 , right_leaf)
        return left_leaf == right_leaf
    def dfs(self,node,leaf):
        if node == None:
            return 0
        if node.left == None and node.right ==None:
            leaf.append(node.val)
        self.dfs(node.left,leaf)
        self.dfs(node.right,leaf)

        

