import json
# 打开 JSON 文件并读取内容
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 遍历 JSON 数据
for entry in data:
    print(entry['车辆识别代码'])


