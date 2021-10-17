from BST.Node import Node

class BST:
    def __init__(self):
        self._root = None
        self._numberOfIndexes = 0

    def insertBST(self, inserNode, value):
        if inserNode is None:
            self._root = Node(value, self._numberOfIndexes)
            self._numberOfIndexes = self._numberOfIndexes + 1
        else:
            if inserNode.value > value:
                if inserNode.left is None:
                    node = Node(value, self._numberOfIndexes)
                    self._numberOfIndexes = self._numberOfIndexes + 1
                    inserNode.left = node
                else:
                    self.insertBST(inserNode.left, value)
            else:
                if inserNode.value < value:
                    if inserNode.right is None:
                        node = Node(value, self._numberOfIndexes)
                        self._numberOfIndexes = self._numberOfIndexes + 1
                        inserNode.right = node
                    else:
                        self.insertBST(inserNode.right, value)
                else:
                    return

    def searchBST(self, searchNode, value):
        if searchNode is None:
            return -1
        if searchNode.value > value:
            if searchNode.left is None:
                return -1
            else:
                self.searchBST(searchNode.left, value)
        else:
            if searchNode.value < value:
                if searchNode.right is None:
                    return -1
                else:
                    self.searchBST(searchNode.right, value)
            else:
                return searchNode.index

    def printBST(self, currentNode):
        if currentNode is None:
            return
        else:
            self.printBST(currentNode.left)
            print(currentNode.index, '--->', currentNode.value)
            self.printBST(currentNode.right)

    def getRoot(self):
        return self._root