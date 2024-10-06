import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import threading
import Excel操作

message = None


def init():
    url = 'https://icorepnbs.pingan.com.cn/icore_pnbs/templates/dept/212/mainCtrl.html?v=1.2024.0904.416221727175734873&applicantPersonFlag=1&familyPrd=&bsDetailCode=2-3-Z-H&usageAttributeCode=01&ownershipAttributeCode=03&insuranceType=1&deptCodeText=212140201&deptCode=212140201&secondLevelDepartmentCode=212&employeeCodeText=2120007254&employeeCode=212000725254&channelCode=Z&productCombineList=&partnerWorknetPanel=&agentCode=12000228&worknetCode=&conferVal=1200022816002+32&agentNameLike=&agentCodeText=&brokerCode=&brokerName=&agentName=%E5%B9%B3%E5%AE%89%E5%88%9B%E5%B1%95%E4%BF%9D%E9%99%A9%E9%94%80%E5%94%AE%E6%9C%8D%E5%8A%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E5%8F%B0%E5%B7%9E%E5%88%86%E5%85%AC%E5%8F%B8&conferNo=1200022816002&subConferNo=32&dealerCode=&autoInsurance=true&propertyInsurance=false&accidentInsurance=false&rateClassFlag=20&employeeName=%E5%8F%B0%E5%B7%9E%E6%9C%AC%E7%BA%A7%E5%88%9B%E5%B1%95%E6%9C%BA%E6%9E%84&saleGroupCode=21214020159&trafficProductCode=MP01000002&commercialProductCode=MP01000001&businessMode=undefined&systemId=PACZ-CORE&applyApproach='

    # 设置 User-Agent 和 Referer
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0")
    # options.add_argument("referer=Your Referer Here")

    # 启动 Edge 浏览器
    browser_name = webdriver.Edge(options=options)
    browser_name.maximize_window()  # 最大化窗口
    browser_name.get(url)

    # 添加 cookies
    cookies_text = """
Name: v1LIHNTx4qTOP, Value: WCcJNgWIWwEm5QJ.ad2tPwyWii.RGwL9mPPJq9PArIlTszey3ozUIVOg_E8SiBayNlaTZgIBNnIg1EIw0mnj2CWhAQ0GZ_db2l7aPMLxDNP.BRRze2Cw.u7vyMtv_5haojETfQx4W4uCu0HLV2sMjZ9dbR_yXZCGjwusmTLe_YXAA7knLLgPhdaAHnoRUPJu54ayZnv.aJNM8O2lf0iih4qftdelR6f7v_9Qy.fcKSYHygxV70YctwG52EYq53KiFMMAt2RfNZ_lMXRQat1fFmnzF3k.UCzqlbJrfgO5_6ctrLUVzWmsfFU5Ia99xZFo5uRM4T1BkxjpgbOCS3HOJoacNbefIwXZ6QxDExgGkj9
Name: USER_REDIS_COOKIE, Value: VFpBQUEtMDAwMDMxNzI3NjM2NTMzNjAzLTEwODE4MTI4OTZfMTcyNzYzNjU0NDEyNg%3D%3D
Name: BIGipServerPOOL_PACLOUD_PRDR2019112805992, Value: 454629804.33420.0000
Name: v1LIHNTx4qTOO, Value: 5vJwDXk.LFIstyax7BjxhNBD8RFHL8of3q1cKndvWaTrFEtzJO47jO0fEINfY5wZiH55yNlBXSjR.3EemLOMUZA
Name: BIGipServerPOOL_PACLOUD_PRDR20230106232593, Value: 2072218583.5162.0000
Name: routeopr, Value: b9fb5b58505ec2342db5a7078db52e68
Name: PA_GREY, Value: TZAAA-00003
Name: us, Value: stable_562
Name: SESSION, Value: NDA0YTAxNmQtNjM2MS00NjE1LTljODAtN2YwOTdiNzcwYjZj
"""

    # 解析 cookies 文本
    cookies = []
    for line in cookies_text.strip().split("\n"):
        name_value = line.split(", Value: ")
        if len(name_value) == 2:
            cookies.append({"name": name_value[0].replace("Name: ", "").strip(), "value": name_value[1].strip()})

    # 添加 cookies
    for cookie in cookies:
        browser_name.add_cookie(cookie)

    browser_name.refresh()  # 刷新以应用 cookies
    return browser_name


# 检查元素函数返回值
def check_element_exists(ys_id, browser_index):
    try:
        browser_index.find_element(By.XPATH, ys_id)
        return True
    except NoSuchElementException:
        return False


def click_syx(driver):
    # 车辆信息: 勾选商业险
    checkbox = driver.find_element(By.XPATH, "//input[@ng-model='ctrl.isCheckedComm']")
    driver.execute_script("arguments[0].scrollIntoView();", checkbox)
    time.sleep(2)
    checkbox.click()  # 点击复选框以勾选


def click_page(name, car_id, driver):
    try:
        a = 0
        time.sleep(4)
        # 行驶证车主: 名称
        input_element = driver.find_element(By.XPATH, "//input[@name='ownerDriver-name']")
        input_element.clear()
        input_element.send_keys(name)  # 填写数据

        # 行驶证车主: 身份证
        input_element = driver.find_element(By.XPATH, "//input[@name='ownerDriver-idno']")
        input_element.send_keys(341821200204293919)  # 填写数据

        # 行驶证车主: 电话号码
        input_element = driver.find_element(By.XPATH, "//input[@name='ownerDriver-telephone']")
        input_element.send_keys(13888888888)  # 填写数据

        # 行驶证车主: 选择指定的省份    下拉
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//select[@name="ownerDriver-province"]/option[@value="1"]'),
                                             '北京')
        )
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//select[@name="ownerDriver-province"]/option[@value="1"]')))
        select_element = Select(driver.find_element(By.NAME, "ownerDriver-province"))
        select_element.select_by_value('1')

        # 行驶证车主: 选择指定的市   下拉
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="ownerDriverInfoDiv"]/div[2]/div/div/select['
                                                        '3]/option[@value="1"]'), '北京市')
        )
        select_element = Select(driver.find_element(By.NAME, "ownerDriver-city"))
        select_element.select_by_value('1')

        # 行驶证车主: 选择指定的区 拉
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="ownerDriverInfoDiv"]/div[2]/div/div/select['
                                                        '4]/option[@value="1"]'), '东城区')
        )
        select_element = Select(driver.find_element(By.NAME, "ownerDriver-county"))
        select_element.select_by_value('1')

        # 车辆信息: 车牌号
        input_element = driver.find_element(By.XPATH, "//input[@id='vehicleLicenseCodeId']")
        input_element.send_keys('浙B-7824X')

        # 车辆信息: 发动机号
        input_element = driver.find_element(By.XPATH, "//input[@id='engineNo']")
        input_element.send_keys('EW328177')

        # 车辆信息: 车架号

        input_element = driver.find_element(By.XPATH, "//input[@id='vehicleFrameNo']")
        time.sleep(0.5)
        # 清空输入框
        input_element.clear()
        input_element.send_keys(car_id)
        # 点击车型校验
        button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@ng-click='vehicleTypeQueryFn()']"))
        )
        button_element.click()
        # 设置延时
        # 车辆信息: 使用性质划分  下拉
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//select[@ng-model='veh.usageAttributeDetailCode']"))
        )
        select_element = Select(driver.find_element(By.XPATH, "//select[@ng-model='veh.usageAttributeDetailCode']"))
        select_element.select_by_visible_text('出租租赁')


        # 车辆信息: 初次登记日期
        input_element = driver.find_element(By.XPATH, "//input[@ng-model='veh.firstRegisterDate']")
        # 清空输入框
        input_element.clear()
        time.sleep(0.5)
        input_element.send_keys('2024-09-23')

        if a == 0:
            click_syx(driver)
        time.sleep(0.5)
        # 点击报价
        button = driver.find_element(By.XPATH, "//button[@ng-click=\"quoteEvent.applyQueryAndQuote('N')\"]")
        button.click()
        time.sleep(3)
        # 设置报价延时
        ########################################################
        # 定位iframe

        # 切换到iframe并等待按钮出现
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe"))
        )

        # 等待并点击按钮
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/button'))
        )
        button.click()

                # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//tr[@ng-repeat='one in repeatApplyInfo']")))
                # # 定位到指定的XPath元素
                # xpath = '/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/div/div[1]/table/tbody/tr[2]/td[5]'
                # element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                # # 获取元素文本内容
                # element_text = element.text.strip()
        # 切换回主文档

        # 等待按钮加载，最多等待 10 秒
                    # 使用 JavaScript 模拟点击
                    # time.sleep(3)
                    # script = 'document.querySelector("button.btn.btn-blue[ng-click=\'closeRepeat()\']").click();'
                    # driver.execute_script(script)
                    # print("按钮已被点击")
        # 等待并获取 保险公司 元素
        tr_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//tr[@ng-repeat='one in repeatApplyInfo']"))
        )
        # 获取所有 <td> 元素
        td_elements = tr_element.find_elements(By.TAG_NAME, "td")
        # 提取特定的文本（比如第5个 <td>）
        target_text = td_elements[4].text  # 索引从0开始

        # 获取文本
        message = target_text
        print("找到", message)
        #  第二个确定
        time.sleep(2)
        # 等待按钮可点击
        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="确定"]'))
        )
        confirm_button.click()

        time.sleep(5)

        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='javascript:;' and @class='modalBox_closeBtn' and @title='关闭']"))
        )
        close_button.click()
        # 检查元素文本是否是中国平安财产保险股份有限公司
        return element_text == '中国平安财产保险股份有限公司'
    except NoSuchElementException:
        # 如果找不到该元素，则返回False
        return False


name, car_id, data = Excel操作.send_data('data1')
# for i in range(len(data)):
# print(name[i])
# print(car_id[i])
# print("----------------------")
t1 = threading.Thread(target=click_page, args=('徐凯威', 'LVHFE1669P6012063', init()))
# result = click_page(, , driver)
# result = click_page(driver)
# print(result)
# t2 = threading.Thread(target=click_page, args=('陈红委', 'LE4ZG8DB3PL880661', init()))
# browser1 = init()
# click_page('胡英明', 'L6T7752Z5NE020453', browser1)
t1.start()
# t2.start()
t1.join()
# t2.join()
print(message)
print('over！')
time.sleep(1000)
