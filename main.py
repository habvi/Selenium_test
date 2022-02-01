from selenium import webdriver
import chromedriver_binary

# 一旦千代田区図書館の開館or閉館情報を調べる
URL = 'https://www.library.chiyoda.tokyo.jp/'

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(10)
driver.get(URL)

# only chiyoda
schedule_elm = driver.find_elements_by_xpath(
    '//li[@id="chiyoda-today-status"]/div/div/span')

print([s.text for s in schedule_elm])