"""
2. 通过 XPath 定位
如果你更熟悉 XPath，你也可以在搜索栏中使用 XPath。输入格式为 // 开头的路径：

xpath
复制代码
//span[@class="count" and @data-v-e99584b8]
//span: 查找所有 <span> 标签。
[@class="count"]: 过滤 class 属性为 count 的 <span>。
[@data-v-e99584b8]: 进一步过滤出 data-v-e99584b8 属性存在的元素。
这会返回页面上所有符合条件的 <span> 元素。
"""