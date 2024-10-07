import subprocess
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import threading
import Ping_An_Class
message = None


def init():
    target_url = 'https://icorepnbs.pingan.com.cn/icore_pnbs/templates/dept/212/mainCtrl.html?v=1.2024.0925.2420151728224526502&applicantPersonFlag=1&familyPrd=&bsDetailCode=2-3-Z-H&usageAttributeCode=02&ownershipAttributeCode=03&insuranceType=1&deptCodeText=212140201&deptCode=212140201&secondLevelDepartmentCode=212&employeeCodeText=2120007254&employeeCode=2120007254&channelCode=Z&productCombineList=&partnerWorknetPanel=&agentCode=12000228&worknetCode=&conferVal=1200022816002+32&agentNameLike=&agentCodeText=&brokerCode=&brokerName=&agentName=%E5%B9%B3%E5%AE%89%E5%88%9B%E5%B1%95%E4%BF%9D%E9%99%A9%E9%94%80%E5%94%AE%E6%9C%8D%E5%8A%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E5%8F%B0%E5%B7%9E%E5%88%86%E5%85%AC%E5%8F%B8&conferNo=1200022816002&subConferNo=32&dealerCode=&autoInsurance=true&propertyInsurance=false&accidentInsurance=false&rateClassFlag=20&employeeName=%E5%8F%B0%E5%B7%9E%E6%9C%AC%E7%BA%A7%E5%88%9B%E5%B1%95%E6%9C%BA%E6%9E%84&saleGroupCode=21214020159&trafficProductCode=MP01000002&commercialProductCode=MP01000001&businessMode=undefined&systemId=PACZ-CORE&applyApproach='
    subprocess.Popen([
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",  # 使用原始字符串
        '--remote-debugging-port=9223',
        '--user-data-dir=D:/EdgeDev1',  # 指定一个用户数据目录
        target_url  # 直接打开目标网页
    ])  # 使用 shell=True 来避免权限问题shell=True

    # 创建 WebDriver 实例连接到 Edge
    options = webdriver.EdgeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9223")
    driver = webdriver.Edge(options=options)


    # 添加 cookies
    cookie_string = 'SESSION=NmM4MDVhZjAtMGE5Ny00YjY1LThmYTUtM2U5ZGVkMDFmZThl; PA_GREY=TZAAA-00001; us=stable_495; routeopr=cca8617c0c43c123e0c300de4135f0fa; BIGipServerPOOL_PACLOUD_PRDR20230106232593=2155908055.5162.0000; v1LIHNTx4qTOO=59gw35J.d6jAoV_M5ReeEPWTjAuT4kzvR5kE8dkkOnqMz.7Ny8KRz.fgiX_FAf1IIe8ocD1Dpp2vcjY4wz7iGbq; BIGipServerPOOL_PACLOUD_PRDR2019112805992=1227006423.33420.0000; USER_REDIS_COOKIE=VFpBQUEtMDAwMDExNzI4Mjg3Njk4NjE5Nzk4MDEzNTY2XzE3MjgyODg4MjE1Mzg%3D; v1LIHNTx4qTOP=iTXPUbCQEQWtjungASwqpTm6HY7uUhlz8SbqgX9b2V279h.qUZNIRrpSZjYVPbLDwpgQi98DTbKYCxBO1koaPR3DiAW6kNweRVAvB7pM13pneBSZMdHKduxIigvuQJ_L79KzYYq2NVws.LhuWXMsjhICh_hutfCy9qnQGG80QsnUkHEKPIdmSlQI8yzMU6tpSSgszYXC8dIE5nUcJfxwFSFQH34FuzkooeG2aNu76ujjee4FQbx6719qTEAp1R1k_jmxbDqhVtygvdGouqxnLUceJjOEX5P2iSrbmqn5DN_9vjJqqndh0lG74LfLuUBOKgZTN2XaHxDhIsBJ0bUvJ8h6tQwczSVXphrrwpgB2r2vLl5t87JemYrkR6jImIHE78yZvxzw3ReDtFnNdpigrOcqvM2uBcFa_qhLvmc.AkL'

    # 将 cookie_string 按 ';' 分割为列表
    cookie_list = cookie_string.split(";")

    # 遍历每个 cookie，将它们添加到 Selenium 的 WebDriver 中
    for cookie in cookie_list:
        cookie = cookie.strip()  # 去掉空格
        if '=' in cookie:
            name, value = cookie.split('=', 1)  # 分割 cookie 名称和值
            # 添加 cookie 到 Selenium WebDriver
            driver.add_cookie({'name': name, 'value': value})

    driver.refresh()

    time.sleep(1000)
    return driver

"""
cookie添加方式1
    cookies_text = 
Name: v1LIHNTx4qTOP, Value: WCcJNgWIWwEm5QJ.ad2tPwyWii.RGwL9mPPJq9PArIlTszey3ozUIVOg_E8SiBayNlaTZgIBNnIg1EIw0mnj2CWhAQ0GZ_db2l7aPMLxDNP.BRRze2Cw.u7vyMtv_5haojETfQx4W4uCu0HLV2sMjZ9dbR_yXZCGjwusmTLe_YXAA7knLLgPhdaAHnoRUPJu54ayZnv.aJNM8O2lf0iih4qftdelR6f7v_9Qy.fcKSYHygxV70YctwG52EYq53KiFMMAt2RfNZ_lMXRQat1fFmnzF3k.UCzqlbJrfgO5_6ctrLUVzWmsfFU5Ia99xZFo5uRM4T1BkxjpgbOCS3HOJoacNbefIwXZ6QxDExgGkj9
Name: USER_REDIS_COOKIE, Value: VFpBQUEtMDAwMDMxNzI3NjM2NTMzNjAzLTEwODE4MTI4OTZfMTcyNzYzNjU0NDEyNg%3D%3D
Name: BIGipServerPOOL_PACLOUD_PRDR2019112805992, Value: 454629804.33420.0000
Name: v1LIHNTx4qTOO, Value: 5vJwDXk.LFIstyax7BjxhNBD8RFHL8of3q1cKndvWaTrFEtzJO47jO0fEINfY5wZiH55yNlBXSjR.3EemLOMUZA
Name: BIGipServerPOOL_PACLOUD_PRDR20230106232593, Value: 2072218583.5162.0000
Name: routeopr, Value: b9fb5b58505ec2342db5a7078db52e68
Name: PA_GREY, Value: TZAAA-00003
Name: us, Value: stable_562
Name: SESSION, Value: NDA0YTAxNmQtNjM2MS00NjE1LTljODAtN2YwOTdiNzcwYjZj


    # 解析 cookies 文本
    cookies = []
    for line in cookies_text.strip().split("\n"):
        name_value = line.split(", Value: ")
        if len(name_value) == 2:
            cookies.append({"name": name_value[0].replace("Name: ", "").strip(), "value": name_value[1].strip()})

    # 添加 cookies
    for cookie in cookies:
        browser_name.add_cookie(cookie)
"""  # cookie添加方式2

# 创建 WebDriver 实例连接到 Edge
options = webdriver.EdgeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9223")
driver = webdriver.Edge(options=options)

a = Ping_An_Class.ClickPage('龚为红', 'LGXCE4CC7P0694582', driver)
a.input_owner_driver_idno()
