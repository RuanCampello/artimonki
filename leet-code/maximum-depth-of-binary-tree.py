from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)

    return max(right, left) + 1
