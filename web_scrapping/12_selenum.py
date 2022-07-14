from selenium import webdriver

browser = webdriver.Chrome("./chromedriver")

#네이버로 이ㅇ
browser.get("https://www.naver.com/")


element = browser.find_element_by_class_name("link_login")
element.click()

# browser.find_element_by_id("id").send_keys("naver_id")

# browser.find_element_by_id("pw").send_keys("naver_id")

# browser.find_elemnt_by_id("log.login").click()s


