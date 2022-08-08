'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []



'''
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res =[]
        def inorder(root,res):
            if not root: return
            inorder(root.left,res)
            res.append(root.val)
            inorder(root.right,res)
            
        inorder(root,res)
        return res
    
    def preorder(root):
        return [root.val] + preorder(root.left) + preorder(root.right) if root else []
    def inorder(root):
        return  inorder(root.left) + [root.val] + inorder(root.right) if root else []
    def postorder(root):
        return  postorder(root.left) + postorder(root.right) + [root.val] if root else []

            
print(Solution().inorderTraversal([1,None,2,3]))