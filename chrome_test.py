import time
from selenium import webdriver

# Chromeが立ち上がり5秒後に検索,5秒後に閉じる
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
time.sleep(5)
search_box = driver.find_element_by_name("q")

search_word = 'ChromeDriver'
search_box.send_keys(search_word)
search_box.submit()
time.sleep(5)
driver.quit()