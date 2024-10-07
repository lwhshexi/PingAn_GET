"""
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from lxml import etree

url = 'https://icorepnbs.pingan.com.cn/icore_pnbs/templates/dept/212/mainCtrl.html?v=1.2024.0904.416221727175734873&applicantPersonFlag=1&familyPrd=&bsDetailCode=2-3-Z-H&usageAttributeCode=01&ownershipAttributeCode=03&insuranceType=1&deptCodeText=212140201&deptCode=212140201&secondLevelDepartmentCode=212&employeeCodeText=2120007254&employeeCode=2120007254&channelCode=Z&productCombineList=&partnerWorknetPanel=&agentCode=12000228&worknetCode=&conferVal=1200022816002+32&agentNameLike=&agentCodeText=&brokerCode=&brokerName=&agentName=%E5%B9%B3%E5%AE%89%E5%88%9B%E5%B1%95%E4%BF%9D%E9%99%A9%E9%94%80%E5%94%AE%E6%9C%8D%E5%8A%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E5%8F%B0%E5%B7%9E%E5%88%86%E5%85%AC%E5%8F%B8&conferNo=1200022816002&subConferNo=32&dealerCode=&autoInsurance=true&propertyInsurance=false&accidentInsurance=false&rateClassFlag=20&employeeName=%E5%8F%B0%E5%B7%9E%E6%9C%AC%E7%BA%A7%E5%88%9B%E5%B1%95%E6%9C%BA%E6%9E%84&saleGroupCode=21214020159&trafficProductCode=MP01000002&commercialProductCode=MP01000001&businessMode=undefined&systemId=PACZ-CORE&applyApproach='

# 设置 User-Agent 和 Referer
options = Options()
options.add_argument("user-agent=Your User-Agent Here")
options.add_argument("referer=Your Referer Here")

browser = webdriver.Edge()  # 定义Edge浏览器，默认会加载当前Python虚拟环境目录下的Scripts目录下的msedgedriver.exe，也可以通过executable_path参数指定路径
browser.maximize_window()  # 最大化窗口
browser.get(url)


# 添加 cookies
cookie_string = 'SESSION=YzVkY2VhNjctM2E3ZC00MTcxLWFjZjEtOWQ2OGZjY2RmOGYz; PA_GREY=TZAAA-00003; BIGipServerPOOL_PACLOUD_PRDR20221226230997=1921230110.5162.0000; routeopr=b9fb5b58505ec2342db5a7078db52e68; us=stable_450; BIGipServerPOOL_PACLOUD_PRDR20230106232593=914459607.5162.0000; v1LIHNTx4qTOO=5gJ6fcNWTusBBCciSKy19epVUDhUCS3ls.DPFhSb9pKvLA70DAQg_lcKvNEfio7IWkxhD6rov49Eu_4I3DDXc7G; BIGipServerPOOL_PACLOUD_PRDR2019112805992=471407020.33420.0000; USER_REDIS_COOKIE=VFpBQUEtMDAwMDMxNzI3MzQxODkxMDQ4MTQ0NTg1MTE2OF8xNzI3MzQzNjAwODcy; v1LIHNTx4qTOP=JVdJJlYjIVtxB6onk4Offv78URSxNle5s945VI8cxPU2g.z5brXRunKofaLQAzWpWZJVB3VTzl_3R9cje8xDPaqTL1RLMquVlvOnotMz8J2J_XoBEe.PpJ7_GNhG4LhisF66Q.heYGCK.OxHlyyyLm1KP2AxZP86S4ODC77xd5fWOMEoDa7WR5lD4DiE7IY6V.1Hlz5ofDt18Jaa3lZo19YiHigCGZqNPZI_to7YGXfPOfy9Yb2r8ELUPfioMRZfklw3agCLvh5yvIP_3J.3qHncNQ87MgFN3k59A_F9rObgNIND._QRpXRwrY3khbQ.lLH3v4lhKJ7AxbQ0foDJV4Ai1CYuNqMmlD6bfRHzq8pKMUj5VrH5w0ozNUNLx.d.gnKKHxdK.FUUWuwc3NiieOCcsOmqANINXhqN5n72wv0'
# 将 cookie 字符串解析为字典列表
cookies = {}
for cookie in cookie_string.split(';'):
    name, value = cookie.strip().split('=', 1)
    cookies[name] = value

for name, value in cookies.items():
    browser.add_cookie({'name': name, 'value': value})

browser.refresh()  # 刷新以应用 cookies
time.sleep(100)
"""

import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from lxml import etree
import Ping_An_Class

url = 'https://icorepnbs.pingan.com.cn/icore_pnbs/templates/dept/212/mainCtrl.html?v=1.2024.0904.416221727175734873&applicantPersonFlag=1&familyPrd=&bsDetailCode=2-3-Z-H&usageAttributeCode=01&ownershipAttributeCode=03&insuranceType=1&deptCodeText=212140201&deptCode=212140201&secondLevelDepartmentCode=212&employeeCodeText=2120007254&employeeCode=212000725254&channelCode=Z&productCombineList=&partnerWorknetPanel=&agentCode=12000228&worknetCode=&conferVal=1200022816002+32&agentNameLike=&agentCodeText=&brokerCode=&brokerName=&agentName=%E5%B9%B3%E5%AE%89%E5%88%9B%E5%B1%95%E4%BF%9D%E9%99%A9%E9%94%80%E5%94%AE%E6%9C%8D%E5%8A%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E5%8F%B0%E5%B7%9E%E5%88%86%E5%85%AC%E5%8F%B8&conferNo=1200022816002&subConferNo=32&dealerCode=&autoInsurance=true&propertyInsurance=false&accidentInsurance=false&rateClassFlag=20&employeeName=%E5%8F%B0%E5%B7%9E%E6%9C%AC%E7%BA%A7%E5%88%9B%E5%B1%95%E6%9C%BA%E6%9E%84&saleGroupCode=21214020159&trafficProductCode=MP01000002&commercialProductCode=MP01000001&businessMode=undefined&systemId=PACZ-CORE&applyApproach='

# 设置 User-Agent 和 Referer
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0")
# options.add_argument("referer=Your Referer Here")

# 启动 Edge 浏览器
browser = webdriver.Edge(options=options)
browser.maximize_window()  # 最大化窗口
browser.get(url)

# 添加 cookies
cookie_string = 'enable_undefined=true; SESSION=OTgxMzBjMWItMzg0Yy00YzViLThhYjktMzVmYjQ1M2VlZjhk; us=stable_562; routeopr=b9fb5b58505ec2342db5a7078db52e68; BIGipServerPOOL_PACLOUD_PRDR20230106232593=914459607.5162.0000; BIGipServerPOOL_PACLOUD_PRDR2019112805992=454629804.33420.0000; PA_GREY=TZAAA-00003; v1LIHNTx4qTOO=5uIbbM47ZbYqgsVwZvd.Z1DSI8rlmJbX8oIfrp2_Q_MPHTgtJcZtf38O88xfCRch5e.k6.mabhU8QaNXxo7fOaA; USER_REDIS_COOKIE=VFpBQUEtMDAwMDMxNzI4Mjg5MDUxODgyLTY5NzYwNjQzM18xNzI4Mjg5MDkyMjU4; v1LIHNTx4qTOP=GOIt7lMHiwcYMN_PAP9HEGErxZrAAdx5DciuWzATyQa5CB7kHjgZlVF7S2fqf2n4_UNt32CdeSz7eZuZLNE_F2KMOZB4M9aF5_xquRShWhVGiIqBu_ZDBI6_pF6HPqlBSdKqEUiGKOkMT_8xFiUJMDbwghONXnsrW2sPk9HEI6xIOTzRay6Fvt4EAIIefdr112WqZEtr6sBqpNX1mllPbCY2wc8SLjSfAOuEDqsE.09HYWIbYvzeMQgjH9FI5PRFS32Xe9X7r_no6JcFnyqXwryvYe1tE.5kPESP_1_B75l47_3aGGNUMlERSaqCIYrJiwQ6cZLQcaiBMrDW1jUNaYePCFnnkzpEODON0bIJ9jE'

# 将 cookie 字符串解析为字典列表
cookies = {}
for cookie in cookie_string.split(';'):
    name, value = cookie.strip().split('=', 1)
    cookies[name] = value

for name, value in cookies.items():
    browser.add_cookie({'name': name, 'value': value})

browser.refresh()  # 刷新以应用 cookies

# 获取页面 HTML
page_html = browser.page_source
with open('平安填取界面.html', 'w', encoding='utf-8')as f:
    f.write(page_html)
print('over!')
time.sleep(100)


def click_page(page_html):
    # 利用Xpath定位找到节点位置
    html = etree.HTML(page_html)
    result = html.xpath('//li[@class="item-0"]')  # 查找属性匹配对应的节点
    print(result)
