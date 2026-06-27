"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None 
        
        hash = {}
        copy = Node(node.val)
        hash[node]=copy 
        q=deque([node])

        while q : 
            cur=q.popleft()
            for n in cur.neighbors:
                if n not in hash :
                    copy = Node(n.val)
                    hash[n]=copy 
                    q.append(n)
                hash[cur].neighbors.append(hash[n])
        return hash[node]