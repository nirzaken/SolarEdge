import json
from builtins import print
from random import randint

from MongoDBClient import MongoDBClient
from MyGraph import MyGraph
from MyTree import *


def initTree(mongoClient):
    tree = MyTree(0, mongoClient)

    tree.getRoot().left = Node(1)
    tree.getRoot().right = Node(2)

    tree.getRoot().left.left = Node(3)
    tree.getRoot().left.right = Node(5)
    tree.getRoot().right.right = Node(6)
    tree.getRoot().right.left = Node(4)

    tree.getRoot().left.left.left = Node(7)
    tree.getRoot().left.left.right = Node(9)
    tree.getRoot().left.right.left = Node(11)
    tree.getRoot().left.right.right = Node(13)
    tree.getRoot().right.left.left = Node(8)
    tree.getRoot().right.left.right = Node(10)
    tree.getRoot().right.right.left = Node(12)
    tree.getRoot().right.right.right = Node(14)

    tree.getRoot().left.left.left.left = Node(15)
    tree.getRoot().left.left.left.right = Node(17)
    tree.getRoot().left.left.right.left = Node(19)
    tree.getRoot().left.left.right.right = Node(21)
    tree.getRoot().left.right.left.left = Node(23)
    tree.getRoot().left.right.left.right = Node(25)
    tree.getRoot().left.right.right.left = Node(27)
    tree.getRoot().left.right.right.right = Node(29)
    tree.getRoot().right.left.left.left = Node(16)
    tree.getRoot().right.left.left.right = Node(18)
    tree.getRoot().right.left.right.left = Node(20)
    tree.getRoot().right.left.right.right = Node(22)
    tree.getRoot().right.right.left.left = Node(24)
    tree.getRoot().right.right.left.right = Node(26)
    tree.getRoot().right.right.right.left = Node(28)
    tree.getRoot().right.right.right.right = Node(30)
    return tree


def main():
    IP = "localhost"
    PORT = "27017"
    DB = "tree"
    COLLECTION = "CountAncestors"
    mongoClient = MongoDBClient(IP, PORT, DB, COLLECTION)
    mongoClient.initDB()
    if mongoClient is None or mongoClient.myClient is None or mongoClient.myDb is None or mongoClient.myCol is None:
        return

    mongoClient.initDB()
    tree = initTree(mongoClient)
    ITERATIONS = randint(100, 1000)

    randList = [randint(0, 30)]
    for i in range(ITERATIONS):
        tree.displayAncestors(tree.getRoot(), randList[-1])
        randList.append(randint(0, 30))

    ids = []
    counts = []
    for x in mongoClient.myCol.find():
        record = json.loads(str(x).replace("'", "\""))
        for elem in record:
            if elem == '_id':
                ids.append(record[elem])
            else:
                counts.append(record[elem])

    print("\n-----------------")
    print("ITERATIONS: " + str(ITERATIONS), end=' ')
    print("\n-----------------")
    print("BFS: Level Order::")
    tree.printLevelOrder()
    print("\n-----------------")
    print("DFS: Pre Order::")
    tree.printPreOrder()
    print("\n-----------------")
    print("DFS: In Order::")
    tree.printInOrder()
    print("\n-----------------")
    print("DFS: Post Order::")
    tree.printPostOrder()
    print("\n-----------------")
    print("Counts::")
    print(counts, end=' ')
    print("\n-----------------")
    print("MongoDB: show dbs::")
    print(mongoClient.myClient.list_database_names())
    print("MongoDB: use tree; show collections::")
    print(mongoClient.myDb.list_collection_names())
    print("MongoDB: db.tree.CountAncestors.find()::")
    for x in mongoClient.myCol.find():
        print(x)
    print("\n-----------------")

    myGraph = MyGraph(ids, counts)
    tree.deleteTree()
    myGraph.deleteGraph()


if __name__ == '__main__':
    main()
