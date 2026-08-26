# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root , root.val)
        return self.count
        
        
    def dfs(self,node,max_so_far):
        if node ==None:
            return 0
        if node.val >= max_so_far:
            self.count+=1
            max_so_far = node.val
        self.dfs(node.left , max_so_far)
        self.dfs(node.right , max_so_far)
        


        