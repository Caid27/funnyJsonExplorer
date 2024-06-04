from abc import ABC, abstractmethod
import json
import argparse
from factory import Style, TreeStyleFactory, RectangleStyleFactory, StyleFactory
from component import Component, Composite, Leaf



class FunnyJsonExplorer:
    def __init__(self, style_factory, icon_family_name, pos = 0):
        self.style_factory = style_factory
        self.pos = pos
        self.iconFamily = None
        self.load_icons(icon_family_name)
        self.total = 0

    def count_keys(self,data_dict):
        count = len(data_dict)  # 计算当前层的键数
        for value in data_dict.values():
            if isinstance(value, dict):
                count += self.count_keys(value)  # 递归调用以计算嵌套字典的键数
        return count

    def load_icons(self, icon_family_name):
        with open('./icon.json', 'r') as file:
            icons_config = json.load(file)
        for family in icons_config['iconFamilies']:
            if family['name'] == icon_family_name:
                self.iconFamily = family['icons']
                break

    def load_json(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            self.total = self.count_keys(data)
        return self._parse_dict(data)

    def _parse_dict(self, data, parent=None):
        if parent is None:
            parent = Composite('root',self.pos, self.total, self.iconFamily[0])
            self.pos = self.pos+1
        for key, value in data.items():
            if isinstance(value, dict):
                node = self.buildComposite(parent, key)
                self._parse_dict(value, node)
            else:
                self.buildLeaf(parent, key, value)
        return parent

    def buildComposite(self, parent, key):
        node = Composite(key, self.pos, self.total, self.iconFamily[0])
        parent.add(node)
        self.pos = self.pos + 1
        return node

    def buildLeaf(self, parent, key, value):
        parent.add(Leaf(key, self.pos, self.total, self.iconFamily[1], value))
        self.pos = self.pos + 1

    def show(self, component):
        self.style_factory.show(component)

def main():
    parser = argparse.ArgumentParser(description="Visualize JSON files as a tree or rectangle structure.")
    parser.add_argument('-f', '--file', required=True, help="Path to the JSON file")
    parser.add_argument('-s', '--style', default='tree', choices=['tree', 'rectangle'],
                        help="Visualization style (tree, rectangle)")
    parser.add_argument('-i', '--icon_family',default='default',
                        help="Icon family for nodes (e.g., 'star' 'default')")
    args = parser.parse_args()

    style_factory =StyleFactory().create_style(args.style)
    explorer = FunnyJsonExplorer(style_factory, args.icon_family)
    component = explorer.load_json(args.file)

    explorer.show(component)

def test():

    tree_factory = TreeStyleFactory()
    rectangle_factory = RectangleStyleFactory()

    icon_family_name ='star'
    explorer_tree = FunnyJsonExplorer(tree_factory, icon_family_name)
    explorer_rec = FunnyJsonExplorer(rectangle_factory, icon_family_name)
    json_file = './example.json'
    component_tree = explorer_tree.load_json(json_file)
    component_rec = explorer_rec.load_json(json_file)

    print("Tree Style:")
    explorer_tree.show(component_tree)

    print("Rectangle Style:")
    explorer_rec.show(component_rec)

if __name__ == "__main__":
    #test()
    main()