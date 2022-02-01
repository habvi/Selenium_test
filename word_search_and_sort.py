from selenium import webdriver
from selenium.webdriver.support.ui import Select
import chromedriver_binary


URL = 'https://www.library.chiyoda.tokyo.jp/'


options = webdriver.ChromeOptions()
# want to open the browser : comment out
# options.add_argument('--headless')

driver = webdriver.Chrome('chromedriver',
                          options=options)
driver.implicitly_wait(10)
driver.get(URL)


# enter the word in the search box
e1 = driver.find_element_by_name('txt_word')
search_word = 'Pythonプログラミング'
e1.send_keys(search_word)

# click the submit button
btn = driver.find_element_by_name('submit_btn_searchEasy')
btn.click()

# select value from the dropdown list
order = driver.find_element_by_id('opt_oder')
order_select = Select(order)
order_select.select_by_value('0')

# click the sort button
btn_sort = driver.find_element_by_name('submit_btn_sort')
btn_sort.click()