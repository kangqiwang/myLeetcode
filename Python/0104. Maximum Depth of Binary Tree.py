'''

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3


'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def countDepth(self,node,depth=0):
    #     if node:
    #         return max(self.countDepth(node.left,depth+1),self.countDepth(node.right,depth+1))
    #     else:
    #         return depth
    
    def countDepth(node,count):
        if node is None:
            return count
        count +=1
        return max(countDepth(node.left, count), countDepth(node.right, count))


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return countDepth(root,depth = 0)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l,r)+1


    
        
# TODO : countDepth not work at moment        
print(Solution().maxDepth([3,9,20,None,None,15,7]))