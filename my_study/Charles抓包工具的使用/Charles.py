import requests

url = 'https://app1.scrape.center/api/movie/?offset=0&limit=100'
res = requests.get(url, verify=False)   # verify=False绕过签名认证
print(res.json())
