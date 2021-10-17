from BST.BST import BST

bst = BST()

bst.insertBST(bst.getRoot(), 'a')
bst.insertBST(bst.getRoot(), 'a')
bst.insertBST(bst.getRoot(), 'b')
bst.insertBST(bst.getRoot(), 'q')
bst.insertBST(bst.getRoot(), 'd')

print(bst.searchBST(bst.getRoot(), 'a'))
print(bst.searchBST(bst.getRoot(), 't'))

f = open("LanguageStructure/token.in", "r")
lines = f.readlines()
tokens = []
for line in lines:
    tokens.append(line)
print(tokens)
f.close()

bst.printBST(bst.getRoot())