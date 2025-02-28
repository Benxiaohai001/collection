from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# 启动一个新的chrome浏览器实例
driver = webdriver.Chrome()
# 访问一个页面
driver.get("http://www.selenium.dev/selenium/web/web-form.html")
# 获取网页的title 
title = driver.title
print(title)

# 设置粘滞超时
driver.implicitly_wait(10)

sleep(5)
text_box = driver.find_element(by=By.NAME, value="my-text")
password_box = driver.find_element(by=By.NAME, value="my-password")
test_area_box = driver.find_element(by=By.NAME, value="my-textarea")

submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
password_box.send_keys("Passwod")
test_area_box.send_keys("This is a test area")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text
print(text)
sleep(20)
# 退出浏览器
driver.quit()

