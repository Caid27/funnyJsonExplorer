# **设计文档**



## 类图及设计模式说明

![image-20240531153907020](C:\Users\38432\AppData\Roaming\Typora\typora-user-images\image-20240531153907020.png)

1. **Composite模式**：`Component` 抽象类为叶子和组合对象定义了共同接口。`Composite` 类表示具有子组件的容器，而 `Leaf` 类表示没有子组件的元素。这样，叶子和组合对象可以被一致地对待。

2. **Abstract Factory模式**：`StyleFactory` 类定义了一个接口来创建不同风格的 `Style` 对象。具体工厂类如 `TreeStyleFactory` 和 `RectangleStyleFactory` 实现了这个接口，用于创建具体的产品对象。

   对于新的风格实现，可以通过抽象工厂类便利地添加。

3. **Factory模式**：`StyleFactory` 类实际上也可以看作是工厂方法模式的实现，其中 `create_style` 方法是一个工厂方法，它返回一个 `Style` 对象的子类实例。

4. **Builder模式**：`FunnyJsonExplorer`类中的`_parse_dict`方法是builder中的结果方法，`buildComposite`方法和`buildLeaf`方法为builder中的部分方法。

5. **Template模式**：`Style` 类定义了一个操作中的算法骨架，将一些步骤推迟到子类中实现。例如，`show` 方法在 `Style` 类中定义了基本流程，而具体的显示逻辑则由子类如 `TreeStyleFactory` 和 `RectangleStyleFactory` 实现。



# 扩展

1. **添加新的风格**：在`Factory.py`文件中加入新的抽象工厂类，并在`styleFactory`类中加入实例创建接口。
2. **添加图标簇**：通过配置文件`icon.json`进行添加修改。使用`Json`格式。





# 使用方法

下载`fje.py`和`fje.bat`，使用`fje -f <json file> -s <style> -i <icon family>`执行`funny json explorer`。

**style**：`tree、rectangle`

**icon**：`default、pokerface、star`







