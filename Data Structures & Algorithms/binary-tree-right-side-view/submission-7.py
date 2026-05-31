# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        li = [root.val]
        q = deque()
        q.append(root)
        level = 0
        next_level = 0
        while len(q) > 0:
            for i in range(len(q)):
                curr = q.popleft()
                if level != next_level:
                    li.append(curr.val)
                    next_level = level
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
            level += 1
        return li 
            