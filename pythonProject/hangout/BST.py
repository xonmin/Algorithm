class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, value): #O(logN)
        self.cur_node = self.root

        while True:
            if value < self.cur_node.value:
                if self.cur_node.left is not None:
                    self.cur_node = self.cur_node.left
                else:
                    self.cur_node.left = Node(value)
                    break
            else:
                if self.cur_node.right is not None:
                    self.cur_node = self.cur_node.right
                else:
                    self.cur_node.right = Node(value)
                    break

    def search(self, value): #O(logN)
        self.cur_node = self.root
        while self.cur_node:
            if self.cur_node.value == value:
                return True
            elif self.cur_node.value > value:
                self.cur_node = self.cur_node.left
            else:
                self.cur_node = self.cur_node.right
        return False

    def delete(self, value): #시간 복잡도 O(h)  h = logn
        is_search = False
        self.cur_node = self.root
        self.parent = self.root

        while self.cur_node:
            if self.cur_node.value == value:
                is_search = True
                break
            elif value < self.cur_node.value:
                self.parent = self.cur_node
                self.cur_node = self.cur_node.left
            else:
                self.parent = self.cur_node
                self.cur_node = self.cur_node.right

        if is_search is False:
            return False

        # 삭제할 값 발견 시
        if self.cur_node.left is None and self.cur_node.right is None: # 자식이 아무도 없다면

            if value < self.parent.value: # 찾고자하는 값이 부모 값보다 작으면
                self.parent.left = None #찾는값(자식)은 왼쪽일거고 그걸 삭제
            else:
                self.parent.right = None #찾는값(자식)은 오른쪽 그걸 삭제

        if self.cur_node.left is not None and self.cur_node.right is None: #찾은 값의 왼쪽 자식이 잇다면
            if value < self.parent.value: # 찾은 값(현재 노드가) 부모보다 작으면
                self.parent.left = self.cur_node.left #  #현재 값 왼쪽 자식을 부모 왼쪽에다가
            else:
                self.parent.right = self.cur_node.left
        if self.cur_node.left is None and self.cur_node.right is not None:
            if value < self.parent.value:
                self.parent.left = self.cur_node.right
            else:
                self.parent.right = self.cur_node.right

        if self.cur_node.left is not None and self.cur_node.right is not None: # 찾은 노드의 자식이 모두 있다면
            self.change_node = self.cur_node.right # 올릴 녀석 - 더 큰 녀석(우측)
            self.change_node_parent = self.cur_node.right # 올릴 녀석 - 더 큰 녀석(우측)

            while self.change_node.left is not None: # 우측 자식의 왼쪽 자식이 없을 때 까지 - 자식 중 삭제하려는 값과 가장 차이가 적은 큰 녀석 찾을 떄 까지
                #서브트리의 가장 왼쪽 노드 찾기
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left

            if self.change_node.right is not None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None

            if value < self.parent.value:
                self.parent.left = self.change_node
                self.change_node.right = self.cur_node.right
                self.change_node.left = self.cur_node.left
            else:
                self.parent.right = self.change_node
                self.change_node.left = self.cur_node.left
                self.change_node.right = self.cur_node.right

        return True


arr = [5, 2, 4, 22, 10, 12, 15, 60, 44, 9]
root = Node(30)
bst = BST(root)
for i in arr:
    bst.insert(i)

print(bst.search(22))
print(bst.search(61))
print(bst.search(60))
print(bst.delete(60))
print(bst.search(60))
print(bst.delete(22))
print(bst.delete(44))
print(bst.search(22))
print(bst.search(44))