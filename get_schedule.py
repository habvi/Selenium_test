from selenium import webdriver
import chromedriver_binary


URL = 'https://www.library.chiyoda.tokyo.jp/'


options = webdriver.ChromeOptions()
# want to open the browser : comment out
options.add_argument('--headless')

driver = webdriver.Chrome('chromedriver',
                          options=options)
driver.implicitly_wait(10)
driver.get(URL)


# get the chiyoda-ku liblary is open or not
schedule_elm = driver.find_elements_by_xpath(
    '//li[@id="chiyoda-today-status"]/div/div/span')
print([s.text for s in schedule_elm])