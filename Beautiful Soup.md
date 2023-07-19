# Beautiful Soup

Beautiful Soup是一个灵活又方便的**网页解析库**，处理高效，支持多种解析器。利用它不用编写正则表达式即可方便的实现网页信息的提取。

## Catalog

1. [Beautiful Soup的安装](#1)
2. [Beautiful 详解](#2)
   1. [解析库](#2-1)
   2. [基本使用](#2-2)
   3. [标签选择器](#2-3)
   4. [标准选择器](#2-4)
   5. [CSS选择器](#2-5)
3. [总结](#3)

## I. Beautiful Soup的安装 <a id="1"></a>

安装方式：```pip3 install beautifulsoup4```

## II. BeautifulSoup详解 <a id="2"></a>

#### i. 解析库 <a id="2-1"></a>

| 解析器          | 使用方法                             | 优势                                                      | 劣势                                     |
| --------------- | ------------------------------------ | --------------------------------------------------------- | ---------------------------------------- |
| Python标准库    | BeautifulSoup(markup, “html.parser”) | Python的内置标准库、执行速度适中、文档容错能力强          | Python2.7.3或3.2.2前的版本中文容错能力差 |
| lxml HTML解析器 | BeautifulSoup(markup,“lxml”)         | 速度快、文档容错力强                                      | 需要安装C语言库                          |
| lxml XML解析器  | BeautifulSoup(markup,“xml”)          | 速度快、唯一支持xml的解析器                               | 需要安装C语言库                          |
| html5lib        | BeautifulSoup(markup,“html5lib”)     | 最好的容错性、以浏览器的方式解析文档、生成HTML5格式的文档 | 速度慢、不依赖外部扩展                   |

#### ii. 基本使用 <a id="2-2"></a>

```
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html, 'lxml')
# 用来格式化代码，自动补全不完整的HTML代码
print(soup.prettify())
# 获取title标签
print(soup.title)
# title标签的名字
print(soup.title.name)
# title标签的内容
print(soup.title.string)
```

#### iii. 标签选择器 <a id="2-3"></a>

**（1）选择元素**

```
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
# 声明soup对象
soup = BeautifulSoup(html, 'lxml')
# 获取title标签
print(soup.title)
# title标签类型
print(type(soup.title))
# 获取head标签
print(soup.head)
# 获取p标签，只输出第一个匹配结果
print(soup.p)
```

**（2）获取名称**

```
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
# 声明soup对象
soup = BeautifulSoup(html, 'lxml')
# 获取名称
print(soup.title.name)
```

**（3）获取属性**

```
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="demo"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
# 声明soup对象
soup = BeautifulSoup(html, 'lxml')
# 获取属性1
print(soup.p.attrs['name'])
# 获取属性2
print(soup.p['name'])
```

**（4）获取内容**

```
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="demo"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
# 声明soup对象
soup = BeautifulSoup(html, 'lxml')
# 获取内容:获取p标签的内容，第一个匹配到的
print(soup.p.string)
```

**（5）嵌套选择**

```
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="demo"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
# 声明soup对象
soup = BeautifulSoup(html, 'lxml')
# 嵌套选择:获取head标签内的title标签的内容
print(soup.head.title.string)
```

**（6）子节点和子孙节点**

```
from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html,'lxml')
# 获得p标签的所有子节点，以列表的方式输出
print(soup.p.contents)
# children 也可以返回子节点，与contents不同的是它相当于一个迭代器
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)
# 获取子孙节点descendants
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)
```

**（7）父节点和祖先节点**

```
from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html,'lxml')
# 获取a标签(第一个a标签)的所有父节点
# print(soup.a.parent)
# 获取a标签所有祖先节点
print(list(enumerate(soup.a.parents)))
```

**（8）兄弟节点**

```
from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html,'lxml')
# 获取a标签(第一个a标签)的所有后面的兄弟节点
print(list(enumerate(soup.a.next_siblings)))
# 获取a标签(第一个a标签)的所有前面的兄弟节点
print(list(enumerate(soup.a.previous_siblings)))
```

#### iv. 标准选择器 <a id="2-4"></a>

- ```find_all(name, attrs, recursive, text, **kwargs)```
- 可根据标签名、属性、内容查找文档，返回所有元素

name 属性

```
//name属性

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# 查找所有name为ul的标签
print(soup.find_all('ul'))
# 输出第一个ul标签的类型
print(type(soup.find_all('ul')[0]))
# 从ul中循环遍历取出所有的li标签
for ul in soup.find_all('ul'):
    print(ul.find_all('li'))
```

attrs 属性

```
from bs4 import BeautifulSoup

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
# attrs传递的是字典形式
print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))
print(soup.find_all(id="list-1"))
# 因为class是Python中的一个关键字，所以不能直接用它来传数据
print(soup.find_all(class_="element"))
```

text 属性

```
from bs4 import BeautifulSoup

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
# 根据文本内容选择
print(soup.find_all(text='Foo'))
```

- ```find(name, attrs, recursive, text, **kwargs)```
- find返回单个元素，即匹配到的第一个结果。

```
from bs4 import BeautifulSoup

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.find('ul'))
print(type(soup.find('ul')))
print(soup.find('page'))
```

- 其他方法
  - find_parents() VS find_patent()
    - find_parents() ——返回所有祖先节点
    - find_patent() ——返回直接父节点
  - find_next_siblings() VS find_next_sibling()
    - find_next_siblings() ——返回后面所有兄弟节点
    - find_next_sibling() ——返回后面第一个兄弟节点
  - find_previous_siblings() VS find_previous_sibling()
    - find_previous_siblings() ——返回前面所有兄弟节点
    - find_previous_sibling() ——返回前面第一个兄弟节点
  - find_all_next() VS find_next()
    - find_all_next() ——返回节点后所有符合条件的节点
    - find_next() ——返回第一个符合条件的节点
  - find_all_previous() VS find_previous()
    find_all_previous() —— 返回节点前所有符合条件的节点
    find_previous() —— 返回节点前第一个符合条件的节点

#### v. CSS选择器 <a id="2-5"></a>

通过select()直接传入CSS选择器即可完成选择。

```
from bs4 import BeautifulSoup

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
# 选择class属性，用空格分隔
print(soup.select('.panel .panel-heading'))
# 选择ul标签中的li标签
print(soup.select('ul li'))
# 选择 ID 中的class为element的标签
print(soup.select('#list-2 .element'))
# 输出第一个ul标签的类型
print(type(soup.select('ul')[0]))
```

**（1）获取属性**

```
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
```

**（2）获取内容**

```
from bs4 import BeautifulSoup

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
for li in soup.select('li'):
    # get_text获取内容
    print(li.get_text())
```

## III. 总结 <a id="3"></a>

1、推荐使用lxml解析库，必要时使用html.parser
2、标签选择筛选功能弱但是速度快
3、建议使用find()、find_all()查询匹配单个结果或者多个结果
4、如果对CSS选择器熟悉的建议使用select()方法
5、记住常用的获取属性和文本值得方法
