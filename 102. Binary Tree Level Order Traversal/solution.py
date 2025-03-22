# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traverse(node, level=0, order=[]):
    if not node:
        return

    if len(order) <= level:
        order.append([])

    order[level].append(node.val)

    traverse(node.left, level+1, order)
    traverse(node.right, level+1, order)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        traverse(root, order=result)

        return result