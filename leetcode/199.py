# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ll = []
        def dfs(node:Optional[TreeNode],level:int) -> None:
            if node is None:
                return
            if level >= len(ll):
                ll.append([])
                ll[level].append(node.val)
            else:
                ll[level].append(node.val)
            dfs(node.right,level+1)
            dfs(node.left,level+1)
        dfs(root,0)
        # 右视图
        res = []
        for i in range(len(ll)):
            print(ll[i])
            if len(ll[i]) > 0:
                res.append(ll[i][0])
            else:
                res.append(None) 
        return res
  
root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
result = Solution().rightSideView(root)
print(result)
