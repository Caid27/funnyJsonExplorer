# **设计文档**



## 类图及设计模式说明

![image-20240608164039699](C:\Users\38432\AppData\Roaming\Typora\typora-user-images\image-20240608164039699.png)



1. **访问者模式**：在这段代码中，访问者模式主要体现在 `TreeRenderer` 类及其子类 `TreeStyleRenderer` 和 `RectangleStyleRenderer`。访问者模式允许在不修改对象结构的前提下，增加作用于一组对象的新操作。这里的 `TreeRenderer` 定义了一个 `render` 方法，具体的渲染操作由其子类实现，这样新增渲染方式时不需要修改树结构或节点类。
2. **迭代器模式**：迭代器模式在 `TreeIterator` 类中得到体现。迭代器模式提供了一种顺序访问集合元素的方式，不需要暴露集合的底层表示。`TreeIterator` 使用一个栈来实现对树节点的深度优先遍历，允许用户逐个访问树中的节点，而不需要知道树的具体结构。



# 扩展

1. **添加新的风格**：在`renderer.py`文件中加入新的抽象工厂类，并在`FunnyJsonExplorer`类中`render`函数加入实例创建接口。
2. **添加图标簇**：通过配置文件`icon.json`进行添加修改。使用`Json`格式。





# 使用方法

下载`fje.py`和`fje.bat`，使用`fje -f <json file> -s <style> -i <icon family>`执行`funny json explorer`。

**style**：`tree、rectangle`

**icon**：`default、pokerface、star`











