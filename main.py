from selenium import webdriver

# 一旦千代田区図書館の開館or閉館情報を調べる
URL = 'https://www.library.chiyoda.tokyo.jp/'

driver = webdriver.Chrome('chromedriver')

# 暗黙的な待機時間を設定(second)
driver.implicitly_wait(10)
driver.get(URL)


# HTMLタグから色々取得できる
# WebElementオブジェクト(class, id, name..)
e1 = driver.find_element_by_class_name('class_name')
e1 = driver.find_element_by_id('id_name')

# 子要素を取得するのに便利
# //親要素[属性(なくてもok)]/子要素[属性(なくてもok)]
# 孫要素は更に/をつけて続ける
e1 = driver.find_element_by_xpath(
    '//div[@id="xxx"]/span')

# タグ内のテキスト
e1.text

# aタグ内のURLなど
e1.get_attribute('href')

# elementは全て複数形もあり,listが返る
e1 = driver.find_elements_by_id('id_name')