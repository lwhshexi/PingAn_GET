html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div
</div>
'''
from pyquery import PyQuery as pq

"""
# doc = pq(html)
# print(doc('li'))  # 第一钟传参可以是字符串

# doc = pq(url='https://cuiqingcai.com')    # 传入参数也可以是url
# print(doc('title'))

# doc = pq(html)
# print(doc('#container'))   # #代表选择的是所有id为container的标签 .代表选择的是所有class的标签
# print(type(doc('#container .list li')))

# doc = pq(html)
# a = doc('#container .list li').items()  # 调用pyquery中items方法获取其文本信息
# print(type(a))
# for a1 in a:
#     print(a1.text())
"""

"""
    # a = doc('.list')
    # print(a)
    # print(type(a))
    # items = a.find('li')    # 查找范围：为节点下的所有子孙节点
    # print(items)
    # print(type(items))
    # print(a)
    # print(a.children())
    
    # a = doc('.active')
    # print(a)
"""     # 使用pyquery库查找节点，遍历节点，获取各种关键信息

"""
    # print(doc)
    items = doc('.list')
    # print(items.parent())   # parent不会查找父节点的父节点，也就是祖父节点

    parents = items.parents()
    # print(parents)
    # print(type(parents))
    # a = parents('.wrap')
    # print(a)
"""     # 父节点

"""
    a = doc('.list .item-0.active')
    print(a.siblings())     # 寻找兄弟节点
    print(a.siblings('.active'))     # 寻找兄弟节中的一个
"""     # 寻找兄弟节点

"""
    doc = pq(html)
    a = doc('li')
    b = a.items()   # 使用items方法后在进行遍历
    for b1 in b:
        print(b1)
"""     # 遍历节点

"""

    # a = doc('.item-0.active a')
    # b = a.attr('href')
    # c = doc('.item-0.active span')
    # print(a)
    # print(type(a))
    # print(a.attr.href)
    a = doc('a')
    # b = a.attr('href')
    # print(type(a))
    c = a.items()
    # print(type(c))  # type 为<class 'generator'>可以使用遍历
    for c1 in c:
        print(c1.attr('href'))
    # print(b)

"""     # 获取属性

"""
# a = doc('.item-0.active a')
# print(a)
# print(a.text())  # 这里只返回此节点下的文本，忽略html文本
# print(a.html())  # 返回a节点内部所有html文本
li = doc('li')
print(li)
# print(li.html())    # 需要遍历才会获取所有html文本
lis = li.items()
for li1 in lis:
    print(li1.html())
print(li.text())
"""     # 获取文本

"""
li = doc('.item-0.active')
print(li)
li = li.remove_class('active')
print(li)
li = li.add_class('active')
print(li)
"""     # 动态改变class属性

"""
所以说，如果 attr 方法只传人第一个参数，即属性名，则表示获取这个属性值;
如果传入第二个参数，则可以用来修改属性值。
text和html方法如果不传参数，表示的是获取节点内的纯文本和HTML文本;如果传人参数，则表示进行赋值，
eg:
    doc = pq(html)
    li = doc('.item-0.active')
    print(li)
    li.attr('name', 'link')
    print(li)
    li.text('change item')
    print(li)
    li.html('<span>change item</span>')
    print(li)
"""     # attr, html, text

"""
# html1 =
# <div class="wrap">
#     Hello, World
#     <p>This is a paragraph.</p>
# </div>

doc = pq(html1)
wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())
"""     # 操作节点方法：remove(), append, empty, prepend
