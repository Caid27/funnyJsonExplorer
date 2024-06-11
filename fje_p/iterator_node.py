from collections.abc import Iterator
# 定义节点类
class TreeNode:
    def __init__(self, name, level, pos, value=None):
        self.name = name
        self.value = value
        self.children = []
        self.level = level
        self.pos = pos
        self.is_last = True
        self.isFinalNode = False

    def add_child(self, node):
        # 如果当前节点已经有子节点，则将最后一个子节点的is_last设置为False
        if self.children:
            self.children[-1].is_last = False

        # 将新添加的子节点的is_last设置为True
        node.is_last = True
        self.children.append(node)

    def check(self):
        if self.is_last and self.level == 0:
            self.isFinalNode = True
        return self.isFinalNode

# 定义树的迭代器

class TreeIterator(Iterator):
    def __init__(self, root):
        self.stack = [(root)]

    def __next__(self):
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        for child in reversed(node.children):
            self.stack.append(child )
        return node