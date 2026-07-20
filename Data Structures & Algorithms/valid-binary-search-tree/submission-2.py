# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,p,q):
            if node is None :
                return True
            
            if (node.val<=p or node.val>=q):
                return False
            
            return (dfs(node.left,p,node.val) and 
                    dfs(node.right,node.val,q))
        
        return dfs(root,float("-inf"),float("inf"))