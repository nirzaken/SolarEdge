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

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(str(node.data) + ' ')
            self._printTree(node.right)

    def printInorder(self, node):
        if node is not None:
            self.printInorder(node.left)
            print(node.data)
            self.printInorder(node.right)

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
