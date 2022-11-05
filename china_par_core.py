
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def get_risk_score(driver,patient_data):
    '''
    :param driver:seleniumWebDriver浏览器驱动程序对象
    :param patient_data:china_par 所需的评估数据 list
    :return:risk-score-value
    '''
    driver.get(r"https://www.cvdrisk.com.cn/ASCVD/Eval")
    #数据转换
    (sex, age, region, area, waist, tc, hdlc, sbp, dbp, drug, dm, csmoke, fh_ascvd)=patient_data


    driver.find_element_by_xpath('//input[@name="sex" and @value='+str(sex)+']').send_keys(Keys.SPACE)  # value=2女 value=1 男
    driver.find_element_by_name("age").send_keys(str(age))  # 输入cnblogs
    driver.find_element_by_xpath('//input[@name="region" and @value='+str(region)+']').send_keys(Keys.SPACE)  # value=0南方 value=1 北方
    driver.find_element_by_xpath('//input[@name="area" and @value='+str(area)+']').send_keys(Keys.SPACE)  # value=0农村 value=1城市
    # 腰围
    driver.find_element_by_name("waist").send_keys(waist)  # 输入50-130
    # 总胆固醇tc
    driver.find_element_by_name("tc").send_keys(tc)  # 输入80-400
    # 高密度脂蛋白胆固醇
    driver.find_element_by_name("hdlc").send_keys(hdlc)  # 输入50-130
    # sbp
    driver.find_element_by_name("sbp").send_keys(sbp)  # 输入50-130
    # dbp
    driver.find_element_by_name("dbp").send_keys(dbp)  # 输入50-130
    # 是否服用降压药
    driver.find_element_by_xpath('//input[@name="drug" and @value='+str(drug)+']').send_keys(Keys.SPACE)  # value=0否 value=1 是
    # 是否糖尿病
    driver.find_element_by_xpath('//input[@name="dm" and @value='+str(dm)+']').send_keys(Keys.SPACE)  # value=0否 value=1 是
    # 是否吸烟
    driver.find_element_by_xpath('//input[@name="csmoke" and @value='+str(csmoke)+']').send_keys(Keys.SPACE)  # value=0否 value=1 是
    # 是否心脑血管病家族史(指父母、兄弟姐妹中有人患有心肌梗死或脑卒中)
    driver.find_element_by_xpath('//input[@name="fh_ascvd" and @value='+str(fh_ascvd)+']').send_keys(Keys.SPACE)  # value=0否 value=1 是
    # 提交
    buttons = driver.find_elements(By.XPATH, "//button")
    buttons[0].click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[-1])
    d = driver.find_elements('xpath', "//div[@class='risk-score-value']")
    return d

def mytest():

    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  # chromedriver所在路径
    d=get_risk_score(driver,[1, 55, 1, 1, 77, 100, 30, 120, 90, 0, 1, 1, 0])
    #结果分别是 10年发病风险；理想的10年发病风险；终生发病风险；理想的终生发病风险

    for item in d:
        print(item.text)
    driver.quit()

if __name__ == "__main__":
    mytest()
