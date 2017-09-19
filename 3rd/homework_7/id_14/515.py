"""
Find Largest Value in Each Tree Row

You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
from queue import PriorityQueue
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = deque()
        queue.append(root)
        results = []
        while len(queue):
            size = len(queue)
            currentLevel = PriorityQueue()
            while size > 0:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                currentLevel.put(-node.val)
                size -= 1
            results.append(-currentLevel.get())
        return results


from collections import deque


class Solution2(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = deque()
        queue.append(root)
        results = []
        while len(queue):
            size = len(queue)
            currentMax = None
            while size > 0:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                currentMax = max(currentMax, node.val) if currentMax != None else node.val
                size -= 1
            if currentMax != None:
                results.append(currentMax)
        return results