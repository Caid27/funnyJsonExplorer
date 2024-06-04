from  component import Component, Composite, Leaf
from abc import ABC, abstractmethod

class StyleFactory:
    def create_style(self, style_type):
        if style_type == 'tree':
            return TreeStyleFactory()
        elif style_type == 'rectangle':
            return RectangleStyleFactory()
        else:
            raise ValueError("Unknown style type")

class Style(ABC):
    @abstractmethod
    def show(self, component):
        pass

class TreeStyleFactory(Style):
    def show(self, component):
        self._display_rect(component)

    def _display_rect(self, component, depth=0, is_last = False, prefix =""):
        if isinstance(component, Composite):
            if depth > 0:
                connector = "└─ " if is_last else "├─ "
                print(f"{prefix}{connector}{component.icon}{component.name}")
                prefix += "    " if is_last else "│  "
        elif isinstance(component, Leaf):
            connector = "└─ " if is_last else "├─ "
            if depth > 0:
                print(f"{prefix}{connector}{component.icon}{component.name}" + (f": {component.value}" if component.value else ""))
            else:
                print(component.name)

        if isinstance(component, Composite):
            for i, child in enumerate(component.children):
                self._display_rect(child, depth + 1, i == len(component.children) - 1, prefix)

class RectangleStyleFactory(Style):
    def show(self, component):
        self._display_rect(component)

    def _display_rect(self, component, depth=0, is_last=False, prefix=""):
        if depth>0:
            # 确定连接器和剩余边长

            value_str = component.value if isinstance(component, Leaf) else ""
            if component.pos == 1:
                connector = "┌─"
                str_len = len(f"{prefix}{connector}{component.icon}{component.name}{': ' + value_str if value_str else ''}")
                resside = '─' * (40 - str_len) if not isinstance(component, Leaf) else '─' * (39 - str_len)
                resside = resside + "┐"
            elif component.pos == component.total:
                prefix = "└──"
                connector = "┴─"
                str_len = len(f"{prefix}{connector}{component.icon} {component.name}{': ' + value_str if value_str else ''}")
                resside = '─' * (40 - str_len) if not isinstance(component, Leaf) else '─' * (39 - str_len)
                resside = resside + "─┘"
            else:
                connector = "├─"
                str_len = len(f"{prefix}{connector}{component.icon} {component.name}{': ' + value_str if value_str else ''}")
                resside = '─' * (40 - str_len) if not isinstance(component, Leaf) else '─' * (39 - str_len)
                resside = resside + "─┤"
            # 打印组件及其连接器和边长
            if isinstance(component, Composite):
                print(f"{prefix}{connector} {component.icon} {component.name} {resside}")
            elif isinstance(component, Leaf):
                print(f"{prefix}{connector} {component.icon} {component.name} {': ' + value_str if value_str else ''} {resside}")

            # 更新子组件的前缀
            prefix += "│  "

        # 递归显示子组件
        if isinstance(component, Composite):
            for i, child in enumerate(component.children):
                self._display_rect(child, depth + 1, i == len(component.children) - 1, prefix)