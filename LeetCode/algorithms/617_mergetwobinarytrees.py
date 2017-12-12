"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
"""


def mergeTrees(t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if t1 is not None and t2 is not None:
        t = TreeNode(t1.val + t2.val)
        t.right = mergeTrees(t1.right, t2.right)
        t.left = mergeTrees(t1.left, t2.left)
        return t
    elif t1 is None and t2 is None:
        return None
    else:
        t3 = t1 if t1 else t2
        t = TreeNode(t3.val)
        t.right = mergeTrees(t3.right, None)
        t.left = mergeTrees(t3.left, None)
        return t
