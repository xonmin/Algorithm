import sys

n = int(sys.stdin.readline())


def preorder(node):
    if node:
        print(node.value, end='')
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end='')
        inorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end='')


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


node_dict = {}
tree = sys.stdin.readline().split()
node = Node(tree[0])
node_dict[tree[0]] = node
if tree[1] != '.':
    node.left = Node(tree[1])
    node_dict[tree[1]] = node.left
if tree[2] != '.':
    node.right = Node(tree[2])
    node_dict[tree[2]] = node.right

for i in range(n - 1):
    tree = sys.stdin.readline().split()
    node = node_dict[tree[0]]
    if tree[1] != '.':
        node.left = Node(tree[1])
        node_dict[tree[1]] = node.left
    if tree[2] != '.':
        node.right = Node(tree[2])
        node_dict[tree[2]] = node.right

first_node = node_dict['A']

preorder(first_node)
print()
inorder(first_node)
print()
postorder(first_node)
