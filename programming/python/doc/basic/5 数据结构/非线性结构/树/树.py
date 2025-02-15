# def BinaryTree(r):
#     return [r, [], []]

# def insertLeft(root, newBranch):
#     t = root.pop(1)
#     if len(t) > 1:
#         root.insert(1, [newBranch, t, []])
#     else:
#         root.insert(1, [newBranch, [], []])
#     return root

# def insertRight(root, newBranch):
#     t = root.pop(2)
#     if len(t) > 1:
#         root.insert(2, [newBranch, [], t])
#     else:
#         root.insert(2, [newBranch, [], []])
#     return root

# def getRootVal(root):
#     return root[0]

# def setRootVal(root, newVal):
#     root[0] = newVal

# def getLeftChild(root):
#     return root[1]

# def getRightChild(root):
#     return root[2]

# r = BinaryTree(3)
# insertLeft(r, 4)
# insertLeft(r, 5)
# insertRight(r, 6)
# insertRight(r, 7)
# l = getLeftChild(r)
# print(f"l: {l}")
# setRootVal(l, 9)
# print(f"r:{r}")
# insertLeft(l, 11)
# print(f"r: {r}")
# print(f"getRightChild(getRightChild(r)): {getRightChild(getRightChild(r))}")


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key

r = BinaryTree('a')
print(f"r: {r.getRootVal()}")
r.insertLeft('b')
print(f"r.getLeftChild(): {r.getLeftChild().getRootVal()}")
r.insertRight('c')
print(f"r.getRightChild(): {r.getRightChild().getRootVal()}")
r.getRightChild().setRootVal('hello')
print(f"r.getRightChild() {r.getRightChild().getRootVal()}")
r.getLeftChild().insertRight('d')
print(f"r.getLeftChild(): {r.getLeftChild().getRootVal()}")


# 解析树
def buildParseTree(fpexp):
    flist = fprexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    for i in flist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootval(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree
# 利用表达式解析树求值

import operator
def evaluate(parseTree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()

# 三种遍历
# 前序遍历
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

# 后序遍历
def posorder(tree):
    if tree != None:
        posorder(tree.getLeftChild())
        posorder(tree.getRightChild())
        print(tree.getRootVal())
# 中序遍历
def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())
# 利用后续遍历进行表达式求值
def postordereval(tree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()

# 利用中序遍历进行表达式求值
def printexp(tree):
    sVal = ''
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal += str(tree.getRootVal())
        sVal += printexp(tree.getRightChild()) + ')'
    return sVal 

# 验证二叉搜索树
# 力扣 98
# 递归求解
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower = float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True
        return helper(root)
# 中序遍历求解
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True

# 101 对称二叉树
# 递归求解
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and check(q.left, p.right) and check(p.left, q.right)
        return check(root.left, root.right)

        
        

