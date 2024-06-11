from iterator_node import TreeNode, TreeIterator

# 定义访问者模式的基类
class Renderer:
    def render(self, node, isFinalNode, total):
        raise NotImplementedError

class TreeStyleRenderer(Renderer):
    def render(self, node, isFinalNode, total):

        connector = '└─ ' if node.is_last else '├─ '
        if node.level > 0:
            pprefix = '│  '+ (node.level) * '   ' if not isFinalNode else "   " + (node.level) * '   '
        else:
            pprefix = ""
        print(f"{pprefix}{connector}{node.name}")

class RectangleStyleRenderer(Renderer):
    def render(self, node, isFinalNode, total):
        prefix = ''
        if node.pos == 1:
            connector = "┌─"
            str_len = len(f"{prefix}{connector}{node.name}")
            resside = '─' * (41 - str_len)
            resside = resside + "┐"
        elif node.pos == total:
            prefix = "└──"
            connector = "┴─"
            str_len = len(
                f"{prefix}{connector}{node.name}")
            resside = '─' * (40 - str_len)
            resside = resside + "─┘"
        else:
            prefix = '│  ' * (node.level)  if not isFinalNode else '│  ' * (node.level)
            connector = "├─"
            str_len = len(
                f"{prefix}{connector}{node.name}")
            resside = '─' * (40 - str_len)
            resside = resside + "─┤"

        print(f"{prefix}{connector}{node.name} {resside}")
