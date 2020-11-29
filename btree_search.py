from bi_tree import BiTree, BiNode


class IntBiTree(BiTree):
    def create_tree(self, definition):
        self.root = None
        self._definition = list(map(lambda x: x if x == '#' else int(x), definition.split('|'))) if definition else []
        self._definition_index = 0
        self._pre_create_tree()

    def search_tree(self, num):
        def _search(tree, parent_tree, num):
            if tree is None:
                return False, parent_tree

            if num == tree.data:
                return True, tree
            elif num < tree.data:
                return _search(tree.lchild, tree, num)
            else:
                return _search(tree.rchild, tree, num)

        return _search(self.root, None, num)

    def insert_search_tree(self, num):
        res, tree = self.search_tree(num)
        if not res:
            node = BiNode(num)
            if tree is None:
                self.root = node
            elif num < tree.data:
                tree.lchild = node
            else:
                tree.rchild = node
            return True
        else:
            return False

    def delete_search_tree(self, num):
        def _search(tree, parent_tree, num):
            if tree is None:
                return False, parent_tree
            if num == tree.data:
                return True, parent_tree
            elif num < tree.data:
                return _search(tree.lchild, tree, num)
            else:
                return _search(tree.rchild, tree, num)

        status, parent_node = _search(self.root, None, num)
        if not status:
            return False

        # 查找它是左结点还是右结点
        if num < parent_node.data:
            attr = 'lchild'
        else:
            attr = 'rchild'

        node = getattr(parent_node, attr)
        if node.rchild is None:
            setattr(parent_node, attr, node.lchild)
        elif node.lchild is None:
            setattr(parent_node, attr, node.rchild)
        else:
            # 左右孩子都不为空
            # 找到指定结点的前驱结点以及前驱结点的父结点
            # 前驱结点不会有右孩子
            before_parent_node = node
            before_node = node.lchild
            while before_node.rchild:
                before_parent_node = before_node
                before_node = before_node.rchild

            # 前驱结点的父节点的右孩子改为前驱结点的左孩子
            before_parent_node.rchild  = before_node.lchild
            # 前驱结点的左右孩子改为目标结点的左右孩子
            before_node.lchild = node.lchild
            before_node.rchild = node.rchild
            # 将目标结点替换为前驱结点
            setattr(parent_node, attr, before_node)


if __name__ == "__main__":
    bi_tree = IntBiTree()
    # bi_tree.create_tree('62|47|#|51|#|#|88|#|#')

    # bi_tree.travel('mid')
    rs = bi_tree.insert_search_tree(62)
    rs = bi_tree.insert_search_tree(88)
    rs = bi_tree.insert_search_tree(58)
    rs = bi_tree.insert_search_tree(47)
    rs = bi_tree.insert_search_tree(35)
    rs = bi_tree.insert_search_tree(73)
    rs = bi_tree.insert_search_tree(51)
    rs = bi_tree.insert_search_tree(37)
    rs = bi_tree.insert_search_tree(36)
    
    bi_tree.travel('mid')
    print('='*20)
    bi_tree.delete_search_tree(47)
    bi_tree.travel('mid')


