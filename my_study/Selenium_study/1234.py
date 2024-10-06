from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pandas as pd


##############################################


#############################################
def click_syx(browse):
    # 车辆信息: 勾选商业险
    checkbox = browse.find_element(By.XPATH, "//input[@ng-model='ctrl.isCheckedComm']")
    browse.execute_script("arguments[0].scrollIntoView();", checkbox)
    checkbox.click()  # 点击复选框以勾选


def click_page(name, car_id, driver, a):
    if a == 0:

        # 行驶证车主: 名称
        input_element = driver.find_element(By.XPATH, "//input[@name='ownerDriver-name']")
        input_element.clear()
        input_element.send_keys(name)  # 填写数据

        # 行驶证车主: 身份证
        input_element = driver.find_element(By.XPATH, "//input[@name='ownerDriver-idno']")
        input_element.clear()
        input_element.send_keys(341821200204293919)  # 填写数据

        # 行驶证车主: 电话号码
        input_element = driver.find_element(By.XPATH, "//input[@name='ownerDriver-telephone']")
        input_element.clear()
        input_element.send_keys(13888888888)  # 填写数据

        # 行驶证车主: 选择指定的省份    下拉
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//select[@name="ownerDriver-province"]/option[@value="1"]'),
                '北京')
        )
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//select[@name="ownerDriver-province"]/option[@value="1"]')))
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
        input_element.clear()
        input_element.send_keys('浙B-7824X')

        # 车辆信息: 发动机号
        input_element = driver.find_element(By.XPATH, "//input[@id='engineNo']")
        input_element.clear()
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

        # 商业险
        click_syx(driver)

        # 点击报价
        button = driver.find_element(By.XPATH, "//button[@ng-click=\"quoteEvent.applyQueryAndQuote('N')\"]")
        button.click()

        ########################################################
        if WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[15]/p/span[1]'))).text == '续保检索及新能源车校验':

            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//tr[@ng-repeat='one in repeatApplyInfo']")))
            # 定位到指定的XPath元素
            xpath = '/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/div/div[1]/table/tbody/tr[2]/td[5]'
            element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element_text = element.text.strip()

            # 切换回主文档
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@class='ui_close']"))
            )
            close_button.click()
            ##############第二次叉掉
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@href='javascript:;' and @class='modalBox_closeBtn' and @title='关闭']"))
            )
            close_button.click()
            return element_text == '中国平安财产保险股份有限公司'

        # 定位到保险公司############################
        else:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//tr[@ng-repeat='one in repeatApplyInfo']")))
            # 定位到指定的XPath元素
            xpath = '/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/div/div[1]/table/tbody/tr[2]/td[5]'
            element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element_text = element.text.strip()

            # 切换回主文档
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@class='ui_close']"))
            )
            close_button.click()
            ##############第二次叉掉
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@href='javascript:;' and @class='modalBox_closeBtn' and @title='关闭']"))
            )
            close_button.click()
            return element_text == '中国平安财产保险股份有限公司'

    else:
        input_element = driver.find_element(By.XPATH, "//input[@name='ownerDriver-name']")
        input_element.clear()
        input_element.send_keys(name)  # 填写数据
        # 车架号
        input_element = driver.find_element(By.XPATH, "//input[@id='vehicleFrameNo']")
        time.sleep(0.5)
        # 清空输入框
        input_element.clear()
        input_element.send_keys(car_id)

        # 定位到保险公司############################
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//tr[@ng-repeat='one in repeatApplyInfo']")))
        # 定位到指定的XPath元素
        xpath = '/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/div/div[1]/table/tbody/tr[2]/td[5]'
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element_text = element.text.strip()

        if WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[15]/p/span[1]'))).text == '续保检索及新能源车校验':
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//tr[@ng-repeat='one in repeatApplyInfo']")))
            # 定位到指定的XPath元素
            xpath = '/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/div/div[1]/table/tbody/tr[2]/td[5]'
            element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element_text = element.text.strip()

            # 切换回主文档
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@class='ui_close']"))
            )
            close_button.click()
            ##############第二次叉掉
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@href='javascript:;' and @class='modalBox_closeBtn' and @title='关闭']"))
            )
            close_button.click()
            return element_text == '中国平安财产保险股份有限公司'

        # 定位到保险公司############################
        else:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//tr[@ng-repeat='one in repeatApplyInfo']")))
            # 定位到指定的XPath元素
            xpath = '/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/div/div[1]/table/tbody/tr[2]/td[5]'
            element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element_text = element.text.strip()

            # 切换回主文档
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@class='ui_close']"))
            )
            close_button.click()
            ##############第二次叉掉
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@href='javascript:;' and @class='modalBox_closeBtn' and @title='关闭']"))
            )
            close_button.click()
            return element_text == '中国平安财产保险股份有限公司'


# 创建 ChromeOptions 对象
chrome_options = Options()
# 添加实验性选项以连接到指定端口上的调试器
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# 初始化 WebDriver，并且将创建的 options 传递给它
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://pacz.pa18.com/cms/#/OrderCenter/Offer')
try:
    # 等待页面加载完成，并且元素可见
    wait = WebDriverWait(driver, 10)  # 最多等待10秒

    # 记录当前窗口的句柄
    original_window = driver.current_window_handle

    button1 = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                     '//*[@id="root"]/div[2]/section/section/main/div[1]/div/div/div/div/div[3]/div[1]/div[3]/div[1]/button[1]')))

    # 点击按钮
    button1.click()

    # 等待新窗口出现，并且确保有两个窗口句柄
    wait.until(EC.number_of_windows_to_be(2))

    # 循环遍历直到找到新的窗口句柄
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    # 定位iframe
    iframe = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]')))
    driver.switch_to.frame(iframe)
    # 现在可以在新窗口中执行操作
    select_location = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="agentCode"]')))

    # 创建 Select 对象
    select = Select(select_location)

    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="agentCode"]/option[@value="0"]'),
                                                '12000228 平安创展保险销售服务有限公司台州分公司'))
    # 通过值 (value) 选择
    select.select_by_value('0')

    # 点击营业
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="usageAttributeCode0"]'))).click()
    # 等待确认按钮元素可点击
    time.sleep(1)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="mainContent"]/div[2]/div[2]/form/div[2]/div/div/button[1]'))).click()
    time.sleep(3)
    # confirm_button = wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, '//*[@id="mainContent"]/div[2]/div[2]/form/div[2]/div/div/button[1]')))
    # # 使用 JavaScript 点击按钮
    # driver.execute_script("arguments[0].click();", confirm_button)
    # result = click_page('朱晓丹', 'LJD4AA194M0094034', driver)
    df = pd.read_excel('平安.xlsx')
    a = 0
    for index, row in df.iterrows():
        owner = row['车主']
        vin = row['车架号']
        result = click_page(owner, vin, driver, a)
        print(result)
        a = a + 1
        # time.sleep(10)

finally:
    # 当不再需要时关闭浏览器
    # driver.quit()  # 如果你想要继续使用该浏览器实例，请不要调用此方法
    pass
