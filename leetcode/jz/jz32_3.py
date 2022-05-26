import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        if not root: return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = []
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2: tmp.insert(0, node.val) # 偶数层 -> 队列头部
                else: tmp.append(node.val) # 奇数层 -> 队列尾部
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(tmp)
        return res

sou = Solution()
sou.levelOrder(['a'])