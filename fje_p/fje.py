import json
from collections.abc import Iterator
from iterator_node import TreeNode, TreeIterator
from renderer import Renderer, TreeStyleRenderer, RectangleStyleRenderer
import  argparse


# 定义节点图标
class IconFamily:
    def __init__(self, icon_family=None ):
        self.iconFamily = self.load_icons(icon_family)
        self.mid_node_icon = self.iconFamily[0]
        self.leaf_node_icon = self.iconFamily[1]

    def load_icons(self, icon_family_name):
        with open('./icon.json', 'r') as file:
            icons_config = json.load(file)
        for family in icons_config['iconFamilies']:
            if family['name'] == icon_family_name:
                return family['icons']
                break

# 定义主要的探索器类
class FunnyJsonExplorer:
    def __init__(self, json_file, icon_family, style='tree'):
        self.json_file = json_file
        self.icon_family = icon_family
        self.style = style
        self.isFinalNode = False
        self.pos = 0
        self.total = 0

    def count_keys(self,data_dict):
        count = len(data_dict)  # 计算当前层的键数
        for value in data_dict.values():
            if isinstance(value, dict):
                count += self.count_keys(value)  # 递归调用以计算嵌套字典的键数
        return count

    def load_json(self):
        with open(self.json_file, 'r') as file:
            data = json.load(file)
            self.total = self.count_keys(data)
            return data

    def build_tree(self, data, level = 1, parent=None):
        if parent is None:
            parent = TreeNode('root', level, self.pos)
        for key, value in data.items():
            self.pos = self.pos + 1
            if isinstance(value, dict):
                node = TreeNode(f"{self.icon_family.mid_node_icon} {key}", level, self.pos)
                parent.add_child(node)
                self.build_tree(value, level+1, node)
            else:
                node = TreeNode(f"{self.icon_family.leaf_node_icon} {key}: {value}", level, self.pos)
                parent.add_child(node)

        return parent

    def render(self):
        root = self.build_tree(self.load_json(),  level=0)
        if self.style == 'tree':
            renderer = TreeStyleRenderer()
        elif self.style == 'rectangle':
            renderer = RectangleStyleRenderer()
        iterator = TreeIterator(root)
        next(iterator)  # Skip root

        for node in iterator:
            if  node.check():
                self.isFinalNode =True
            renderer.render(node, self.isFinalNode, self.total)

def test():
    # 定义图标族
    poker_face_icon_family = IconFamily(icon_family = "star")
    # 初始化FunnyJsonExplorer
    json_file = 'example.json'  # 替换为你的JSON文件路径
    style = 'tree'  # 可以是 'tree' 或 'rectangle'
    fje = FunnyJsonExplorer(json_file, poker_face_icon_family, style)
    # 渲染结果
    fje.render()

    style = 'rectangle'  # 可以是 'tree' 或 'rectangle'
    fje = FunnyJsonExplorer(json_file, poker_face_icon_family, style)
    fje.render()

def main():

    parser = argparse.ArgumentParser(description="Visualize JSON files as a tree or rectangle structure.")
    parser.add_argument('-f', '--file', required=True, help="Path to the JSON file")
    parser.add_argument('-s', '--style', default='tree', choices=['tree', 'rectangle'],
                        help="Visualization style (tree, rectangle)")
    parser.add_argument('-i', '--icon_family',default='default',
                        help="Icon family for nodes (e.g., 'star' 'default')")
    args = parser.parse_args()

    my_icon_family = IconFamily(args.icon_family)
    fje = FunnyJsonExplorer(args.file, my_icon_family, args.style)
    fje.render()

if __name__ == "__main__":
    #test()
    main()