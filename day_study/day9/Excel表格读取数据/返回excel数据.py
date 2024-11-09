import pandas as pd
"""
# 读取Excel文件
file_path = '台州丽水一年.xlsx'  # 替换为您的文件路径
df = pd.read_excel(file_path)

df['保险公司名称'] = ""
df['车牌号'] = ""

# 保存修改后的Excel文件
df.to_excel(file_path, index=False)

print("修改后的文件已保存")
"""  # 增加标题行

# 读取Excel文件
file_path = '台州丽水一年.xlsx'  # 替换为你的文件路径
df = pd.read_excel(file_path)

# 将 '保险公司名称' 列的类型转换为字符串类型
df['保险公司名称'] = df['保险公司名称'].astype(str)
df['车牌号'] = df['车牌号'].astype(str)

df.loc[0, '保险公司名称'] = "中国平安保险"
df.loc[1, '保险公司名称'] = "中国保险"

for i in range(5):
    df.loc[i, '车牌号'] = f'12{i}'

# 将修改后的 DataFrame 保存到新的 Excel 文件
df.to_excel(file_path, index=False)

print("文件已保存")
