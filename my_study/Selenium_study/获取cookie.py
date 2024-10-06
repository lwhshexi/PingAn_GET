import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


def get_cookie():
    target_url = 'https://pacz.pa18.com/cms/#/mainPage/center'
    subprocess.Popen([
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",  # 使用原始字符串
        '--remote-debugging-port=9222',
        '--user-data-dir=D:/EdgeDev',  # 指定一个用户数据目录
        target_url  # 直接打开目标网页
    ])  # 使用 shell=True 来避免权限问题shell=True

    # 创建 WebDriver 实例连接到 Edge
    options = webdriver.EdgeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Edge(options=options)

    try:
        # 等待特定节点出现，最多等待 10 秒
        li_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.antd-pro-pages-main-page-center-ul li[data-tracking="click"]'))
        )
        # 点击元素
        li_element.click()
        print("已找到并点击 '业务管理' 节点。")
    except Exception as e:
        print("未找到 '业务管理' 节点:", e)
        print(driver.title)

    try:
        # 等待鼠标悬停的标签出现，最多等待10秒
        hover_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.ant-menu-submenu-title'))
        )
        # 创建 ActionChains 实例
        actions = ActionChains(driver)
        # 悬停到目标标签
        actions.move_to_element(hover_element).perform()

        # 等待要点击的节点出现，最多等待10秒
        link_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//li[@data-tracking="menu"]//a[contains(@href, "#/OrderCenter/Offer")]//span[text()="报价出单"]'))
        )
        # 使用JavaScript点击，绕过被覆盖问题
        driver.execute_script("arguments[0].click();", link_element)
        print("已找到并点击目标节点。")

    except Exception as e:
        print("未找到目标节点:", e)

    # 点击车险
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="button" and contains(@class, "ant-btn-primary")]//span[text()="IBCS/CACS车险"]'))
    )
    # 使用 JavaScript 进行点击
    driver.execute_script("arguments[0].click();", button)

    # 获取当前所有的窗口句柄
    window_handles = driver.window_handles
    # 切换到最新打开的标签页（通常是最后一个）
    # driver.switch_to.window(window_handles[-1])
    # 等待新窗口出现，并且确保有两个窗口句柄
    wait = WebDriverWait(driver, 10)  # 最多等待10秒
    wait.until(EC.number_of_windows_to_be(2))
    # 循环检查新标签是否出现
    while True:
        current_window_handles = driver.window_handles
        if len(current_window_handles) > len(window_handles):
            print("新标签页已打开。")
            # 切换到最新打开的标签页（通常是最后一个）
            driver.switch_to.window(current_window_handles[-1])
            break  # 找到新标签后退出循环
    print("+++++++++++", driver.title)

    # 定位iframe
    iframe = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]')))
    driver.switch_to.frame(iframe)
    # 现在可以在新窗口中执行操作
    select_location = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="agentCode"]')))
    # 创建 Select 对象
    select = Select(select_location)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="agentCode"]/option[@value="0"]'), '0'))

    # 通过值 (value) 选择
    select.select_by_value('0')
    # 点击营业
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="usageAttributeCode0"]'))).click()
    # time.sleep(0.5)

    # 等待确认按钮元素可点击
    confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="mainContent"]/div[2]/div[2]/form/div[2]/div/div/button[1]')))
    # 使用 JavaScript 点击按钮
    time.sleep(0.1)
    driver.execute_script("arguments[0].click();", confirm_button)

    wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@class, 'control-label') and contains(., '地址：')]")))  # 替换为实际的动态元素
    # 获取当前加载的 cookies 值

    # 1. 打开新的标签页
    driver.execute_script("window.open('');")  # 新打开一个空标签页

    # 2. 切换到新打开的标签页
    driver.switch_to.window(driver.window_handles[-1])  # 切换到最后一个标签页

    # 3. 在新标签页中输入目标网址并访问
    url = "https://icorepnbs.pingan.com.cn/icore_pnbs/templates/dept/212/mainCtrl.html?v=1.2024.0904.416221727175734873&applicantPersonFlag=1&familyPrd=&bsDetailCode=2-3-Z-H&usageAttributeCode=01&ownershipAttributeCode=03&insuranceType=1&deptCodeText=212&deptCode=212140201&secondLevelDepartmentCode=212&employeeCodeText=212000725254&channelCode=Z&productCombineList=&partnerWorknetPanel=&agentCode=12000228&worknetCode=&conferVal=1200022816002+32&agentNameLike=&agentCodeText=&brokerCode=&brokerName=&agentName=%E5%B9%B3%E5%AE%89%E5%88%9B%E5%B1%95%E4%BF%9D%E9%99%A9%E9%94%80%E5%94%AE%E6%9C%8D%E5%8A%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E5%8F%B0%E5%B7%9E%E5%88%86%E5%85%AC%E5%8F%B8&conferNo=1200022816002&subConferNo=32&dealerCode=&autoInsurance=true&propertyInsurance=false&accidentInsurance=false&rateClassFlag=20&employeeName=%E5%8F%B0%E5%B7%9E%E6%9C%AC%E7%BA%A7%E5%88%9B%E5%B1%95%E6%9C%BA%E6%9E%84&saleGroupCode=21214020159&trafficProductCode=MP01000002&commercialProductCode=MP01000001&businessMode=undefined&systemId=PACZ-CORE&applyApproach="
    driver.get(url)  # 访问目标 URL

    # 4. 等待页面加载完成（可根据实际情况调整）
    time.sleep(1)
    # wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]')))  # 等待特定元素出现

    # 5. 获取当前页面的 cookies
    cookies = driver.get_cookies()

    # 打印 cookies
    for cookie in cookies:
        print(f"Name: {cookie['name']}, Value: {cookie['value']}")


get_cookie()
