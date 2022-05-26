# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            # 根节点加入列表
            node = queue.popleft()
            res.append(node.val)
            # 加入左右节点到队列，这里就是层序遍历。
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

node = [3,9,20,None,None,15,7]