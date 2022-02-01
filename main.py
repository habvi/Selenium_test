from selenium import webdriver
import chromedriver_binary

# 一旦千代田区図書館の開館or閉館情報を調べる
URL = 'https://www.library.chiyoda.tokyo.jp/'


options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome('chromedriver',
                          options=options)
driver.implicitly_wait(10)
driver.get(URL)


schedule_elm = driver.find_elements_by_xpath(
    '//li[@id="chiyoda-today-status"]/div/div/span')
print([s.text for s in schedule_elm])



e1 = driver.find_element_by_id('xxx')
# textboxに入力したい値を設定すると自動で入力
e1.send_keys('Python')
# 入力済みtextを削除
e1.clear()
# bottonならこれでclick可能
e1.click()

# dropdownの場合はimportして
from selenium.webdriver.support.ui import Select
s = Select(e1)
# 選択肢にvalueがついてるのでそれで指定
s.select_by_value('1')