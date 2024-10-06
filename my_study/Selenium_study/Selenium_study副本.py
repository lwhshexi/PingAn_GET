import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import threading

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
Name: USER_REDIS_COOKIE, Value: VFpBQUEtMDAwMDMxNzI3NTUxMjg2NzE0MjU4Nzk1MzU2XzE3Mjc1NTEyOTQ2MTg%3D
Name: v1LIHNTx4qTOP, Value: kF6Fvy3.C9us0YcHnBOuoVy0sGxwVjBlgLAL5pYOYqPHMrnzEgQz6Az.3Ki_fJwjdPx87jYyKlsx6g8xrkI8uj7olxwREOV1LecFuj7HqWkt7NWKK2nS91C40ljpRyy2xGBbEW_sdPUI1Q__DYV6JoQjt0a.QM.BG1XN131q6xz4G7OOYelJ5SPV4TjYPW_ErTmTUnUSygD6F3SywxIPtuUk6O6gDOo3YrCxgEyLKEenWArYqXCT3D3UPl9avUnNfAt489aCAGq_qxLW7GIybGS7gK_1BDp476olZy861cBe.FLKj19qt1cDIT8pU4ZOA.11QSWFkx40ZQvE1aS3FIDVxxdRf.c.efxDn4g8nA3
Name: BIGipServerPOOL_PACLOUD_PRDR2019112805992, Value: 437852588.33420.0000
Name: BIGipServerPOOL_PACLOUD_PRDR20230106232593, Value: 2877328343.5162.0000
Name: routeopr, Value: cca8617c0c43c123e0c300de4135f0fa
Name: PA_GREY, Value: TZAAA-00003
Name: us, Value: stable_558
Name: v1LIHNTx4qTOO, Value: 5fuOi50lg1_63TehLXCLOVp10z9zGC8xF4Ob.t5T1i1EKkATaEuSZXPlPdOZUVzb0tBKqb36R8mDJHLAdqtGWuG
Name: SESSION, Value: NjI1MmU1ZDMtN2ZlOS00ZjFmLThjOTgtZDVmYWFiNDg1Njhh
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


def click_syx(browser_index):
    # 车辆信息: 勾选商业险
    checkbox = browser_index.find_element(By.XPATH, "//input[@ng-model='ctrl.isCheckedComm']")
    browser_index.execute_script("arguments[0].scrollIntoView();", checkbox)
    time.sleep(2)
    checkbox.click()  # 点击复选框以勾选


def click_page(name, car_id, browser_index):
    global message
    a = 0
    time.sleep(6)
    # 检查元素是否存在
    if check_element_exists("//input[@id='vehicleLicenseCodeId']", browser_index):
        print("元素存在！")
        # 行驶证车主: 名称
        input_element = browser_index.find_element(By.XPATH, "//input[@name='ownerDriver-name']")
        input_element.send_keys(name)  # 填写数据

        # 行驶证车主: 身份证
        input_element = browser_index.find_element(By.XPATH, "//input[@name='ownerDriver-idno']")
        input_element.send_keys(341821200204293919)  # 填写数据

        # 行驶证车主: 电话号码
        input_element = browser_index.find_element(By.XPATH, "//input[@name='ownerDriver-telephone']")
        input_element.send_keys(13888888888)  # 填写数据

        # 行驶证车主: 选择指定的省份    下拉
        WebDriverWait(browser_index, 10).until(
            EC.visibility_of_element_located((By.NAME, "ownerDriver-province"))
        )
        select_element = Select(browser_index.find_element(By.NAME, "ownerDriver-province"))
        select_element.select_by_visible_text('北京市')

        time.sleep(2)
        # 行驶证车主: 选择指定的市   下拉
        WebDriverWait(browser_index, 10).until(
            EC.visibility_of_element_located((By.NAME, "ownerDriver-city"))
        )
        select_element = Select(browser_index.find_element(By.NAME, "ownerDriver-city"))
        select_element.select_by_visible_text('北京市')

        time.sleep(2)
        # 行驶证车主: 选择指定的区     下拉
        WebDriverWait(browser_index, 10).until(
            EC.visibility_of_element_located((By.NAME, "ownerDriver-county"))
        )
        select_element = Select(browser_index.find_element(By.NAME, "ownerDriver-county"))
        select_element.select_by_visible_text('东城区')

        # 车辆信息: 车牌号
        input_element = browser_index.find_element(By.XPATH, "//input[@id='vehicleLicenseCodeId']")
        input_element.send_keys('浙B-7824X')

        # 车辆信息: 发动机号
        input_element = browser_index.find_element(By.XPATH, "//input[@id='engineNo']")
        input_element.send_keys('EW328177')

        time.sleep(0.5)
        # 车辆信息: 车架号
        input_element = browser_index.find_element(By.XPATH, "//input[@id='vehicleFrameNo']")
        # 清空输入框
        input_element.clear()
        input_element.send_keys(car_id)

        # 点击车型校验
        button_element = WebDriverWait(browser_index, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@ng-click='vehicleTypeQueryFn()']"))
        )
        button_element.click()
        print("按钮已点击！")

        # 设置延时
        time.sleep(2)

        # 车辆信息: 使用性质划分  下拉
        WebDriverWait(browser_index, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//select[@ng-model='veh.usageAttributeDetailCode']"))
        )
        select_element = Select(browser_index.find_element(By.XPATH, "//select[@ng-model='veh.usageAttributeDetailCode']"))
        select_element.select_by_visible_text('出租租赁')

        # 车辆信息: 初次登记日期
        input_element = browser_index.find_element(By.XPATH, "//input[@ng-model='veh.firstRegisterDate']")
        # 清空输入框
        input_element.clear()
        time.sleep(1)
        input_element.send_keys('2024-09-13')

        # #  点击页面位置
        # time.sleep(2)
        # pyautogui.click(2, 432)

        if a == 0:
            click_syx(browser_index)

        # 点击报价
        button = browser_index.find_element(By.XPATH, "//button[@ng-click=\"quoteEvent.applyQueryAndQuote('N')\"]")
        button.click()
        time.sleep(4)  # 设置报价延时

        # 等待并获取 保险公司 元素
        tr_element = WebDriverWait(browser_index, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//tr[@ng-repeat='one in repeatApplyInfo']"))
        )
        # 获取所有 <td> 元素
        td_elements = tr_element.find_elements(By.TAG_NAME, "td")
        # 提取特定的文本（比如第5个 <td>）
        target_text = td_elements[4].text  # 索引从0开始

        # 获取文本
        message = target_text
        print("找到")

        # 关闭完成一次信息抓取
        close_button = WebDriverWait(browser_index, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='ui_close']"))
        )
        close_button.click()

        # 判断是否出现报价错误
        for i in range(100):
            try:
                # 查找包含错误信息的 <div>
                modal_box = browser_index.find_elements(By.XPATH, "//div[@class='modalBox' and .//span[text()='申请报价出现错误！']]")
                # 判断元素是否存在
                if modal_box:
                    # 查找关闭按钮并点击
                    close_button = modal_box[0].find_element(By.XPATH, ".//a[@class='modalBox_closeBtn']")
                    close_button.click()
            except Exception as e:
                print(f"发生错误: {e}")  # 可选：处理异常
                time.sleep(0.5)

        # 滚动到页面顶部
        browser_index.execute_script("window.scrollTo(0, 0);")
        a += 1
    else:
        print("元素不存在！")


t1 = threading.Thread(target=click_page, args=('胡英明', 'L6T7752Z5NE020453', init()))
# t2 = threading.Thread(target=click_page, args=('陈红委', 'LE4ZG8DB3PL880661', init()))
# browser1 = init()
# click_page('胡英明', 'L6T7752Z5NE020453', browser1)
t1.start()
# t2.start()
t1.join()
# t2.join()
print(message)
print('over')
time.sleep(1000)
