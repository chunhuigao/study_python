class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.ll = []
        self.deepFn(root,0)
        return self.ll
    def deepFn(self,root,idx):
        if not root:
            return 0
          
        if idx >= len(self.ll):
            self.ll.append([])
        self.ll[idx].append(root.val)
        self.deepFn(root.left,idx+1)
        self.deepFn(root.right,idx+1)

root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
result = Solution().levelOrder(root)
print(result)
            