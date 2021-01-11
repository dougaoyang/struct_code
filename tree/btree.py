# 二叉树

class BiNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BiTree:
    def __init__(self, root=None):
        self.root = root

    def create_tree(self, definition):
        self.root = None
        self._definition = definition
        self._definition_index = 0
        self._pre_create_tree()

    def _pre_create_tree(self):
        """前序插入创建"""
        if self._definition_index >= len(self._definition):
            return None

        char = self._definition[self._definition_index]

        if char == '#':
            return None

        node = BiNode(char)
        if self.root is None:
            self.root = node
        
        self._definition_index += 1
        node.lchild = self._pre_create_tree()
        self._definition_index += 1
        node.rchild = self._pre_create_tree()

        return node

    def travel(self, way='pre'):
        if way == 'pre':
            self._pre_travel(self.root)
        elif way == 'mid':
            self._mid_travel(self.root)
        elif way == 'after':
            self._after_travel(self.root)

    def _pre_travel(self, root):
        """前序遍历"""
        if root == None:
            return

        print(root.data)
        self._pre_travel(root.lchild)
        self._pre_travel(root.rchild)

    def _mid_travel(self, root):
        """中序遍历"""
        if root == None:
            return

        self._mid_travel(root.lchild)
        print(root.data)
        self._mid_travel(root.rchild)

    def _after_travel(self, root):
        """后序遍历"""
        if root == None:
            return

        self._after_travel(root.lchild)
        self._after_travel(root.rchild)
        print(root.data)


if __name__ == "__main__":
    bi_tree = BiTree()
    bi_tree.create_tree('AB#D##C##')

    bi_tree.travel('pre')
    print('='*10)
    bi_tree.travel('mid')
    print('='*10)
    bi_tree.travel('after')
