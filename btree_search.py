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


if __name__ == "__main__":
    bi_tree = IntBiTree()
    # bi_tree.create_tree('62|47|#|51|#|#|88|#|#')

    # bi_tree.travel('mid')
    rs = bi_tree.insert_search_tree(61)
    rs = bi_tree.insert_search_tree(23)
    rs = bi_tree.insert_search_tree(45)
    print(rs)
    bi_tree.travel('mid')


