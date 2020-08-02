"""
读取xml数据
有dom方式，有etree方式，sax方式等
这是一个使用 xml.etree.ElementTree （简称 ET ）的简短教程。目标是演示模块的一些构建块和基本概念。

XML树和元素
XML是一种固有的分层数据格式，最自然的表示方法是使用树。为此， ET 有两个类： ElementTree 将整个XML文档表示为一个树， Element
表示该树中的单个节点。与整个文档的交互（读写文件）通常在 ElementTree 级别完成。与单个XML元素及其子元素的交互是在 Element 级别完成的。
"""
import xml.etree.ElementTree as ET
import os
path = os.path.abspath("config")
tree = ET.parse(path+'\\config.xml')
root =  tree.getroot()
# print(root.attrib)
# for child in root:
#     print(child.tag, child.attrib)
# print(root[0][2].text)
#
# for neighbor in root.iter("neighbor"):
#     print(neighbor.attrib)
# 可以用 Element.text 访问元素的文本内容。 Element.get 访问元素的属性
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(rank, name)
