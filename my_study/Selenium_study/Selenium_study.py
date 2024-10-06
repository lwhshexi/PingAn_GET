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
cookie_string = 'SESSION=ZDQ0ZGFkMjYtYjBmMy00YTQzLTk2YzUtOTk1YTM5ZGQ3MzU3; PA_GREY=TZAAA-00003; BIGipServerPOOL_PACLOUD_PRDR20221226230997=1921230110.5162.0000; us=stable_348; routeopr=ef205d981392b2492ff69580a428be47; BIGipServerPOOL_PACLOUD_PRDR20230106232593=1082166231.5162.0000; v1LIHNTx4qTOO=5f7aHxy6JuyiB.a_8hJ0e__.5Ti52W6C28LPRx4zGx695kiBAj9i.sExb5gfKbEemhiy.gKsJDQ9uPo0aYL0tbq; BIGipServerPOOL_PACLOUD_PRDR2019112805992=1243783639.33420.0000; USER_REDIS_COOKIE=VFpBQUEtMDAwMDMxNzI3MzQzODYyNjI1LTU4NzE2MDcyN18xNzI3MzQzOTA1NTk2; v1LIHNTx4qTOP=RY6JTzsIgbItWS4CW9jZKIMVJQKfawutLYPEfEgM4NxoWASNTKddHuLT8Yvz80c1W0jIAJaXmUp2L7UBS2VJ674PxLnSJtEgPEVZGEUOE5mrNya0f5xSc6G4dwU_48Nvv2tZbEbP4JxeG0SigmB1KBd7htT6_aCddVzXU3dULrWBfQBIZ.8J1YfnEAraxaaC2wa3aToYKD0u_txN_.QISVTGU0fTOXmgHQtmA3bo_M8HWGSAfPwyeOK9n17pSo4SLNYL0xbbT_lFCB0aJM4AWLMSp8MChjeRYHiLzuVsIPrLUaLg5HLDmu1GT5PannwKVG4BHic_7DZ8iCld0DW_AH_JIzYPP1krq_.xUUIrmYa'

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
