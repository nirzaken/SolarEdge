class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class MyTree:
    def __init__(self, data, mongoClient):
        self.root = Node(data)
        self.mongoClient = mongoClient

    def getRoot(self):
        return self.root

    def deleteTree(self):
        self.root = None

    def printLevelOrder(self):
        if self is not None and self.root is not None:
            self._printLevelOrder(self.root)
        else:
            return

    def _printLevelOrder(self, root):
        Q = [root]
        while len(Q) > 0:
            curr = Q.pop(0)
            print(curr.data, end=' ')
            if curr.left is not None:
                Q.append(curr.left)
                if curr.right is not None:
                    Q.append(curr.right)

    def printInOrder(self):
        if self is not None and self.root is not None:
            self._printInOrder(self.root)

    def _printInOrder(self, node):
        if node is not None:
            self._printInOrder(node.left)
            print(node.data, end=' ')
            self._printInOrder(node.right)

    def printPreOrder(self):
        if self is not None and self.root is not None:
            self._printPreOrder(self.root)

    def _printPreOrder(self, node):
        if node is not None:
            print(node.data, end=' ')
            self._printPreOrder(node.left)
            self._printPreOrder(node.right)

    def printPostOrder(self):
        if self is not None and self.root is not None:
            self._printPostOrder(self.root)

    def _printPostOrder(self, node):
        if node is not None:
            self._printPostOrder(node.left)
            self._printPostOrder(node.right)
            print(node.data, end=' ')

    def displayAncestors(self, node, datatofind):
        if node is None:
            return False

        if node.data == datatofind:
            return True

        if self.displayAncestors(node.left, datatofind) or self.displayAncestors(node.right, datatofind):
            myquery = {"_id": node.data}
            newvalues = {"$inc": {"count": 1}}
            self.mongoClient.myCol.update_one(myquery, newvalues)
            return True

        return False
