# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif (p is None and q) or (q is None and p):
            return False
        
        pTree = self.createLevelOrderArray(p)
        print(pTree)
        qTree = self.createLevelOrderArray(q)
        print(qTree)

        return pTree == qTree
    
    def createLevelOrderArray(self, tree):
        queue = deque([tree])
        treeArr = []
        treeArr.append(tree.val)

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                treeArr.append(node.left.val)
            else:
                treeArr.append(None)

            if node.right:
                queue.append(node.right)
                treeArr.append(node.right.val)
            else:
                treeArr.append(None)
        
        return treeArr
