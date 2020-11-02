import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        if root==None:
            return -1
        queue = []
        queue.append(root)
        while len(queue)!=0:
            current = queue[0]
            print(current.data, end=' ')
            if(current.left != None):
                queue.append(current.left)
            if (current.right != None):
                queue.append(current.right)
            queue.pop(0)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
