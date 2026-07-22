# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [] 
        def dfs(node):
            if node is None :
                return None 
            res.append(node.val)
            return (dfs(node.left) or dfs(node.right))
        dfs(root)
        res= sorted(res)
        for i in range(len(res)):
            if i == k-1 :
                return res[i]
        return 0 