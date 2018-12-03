from selenium import webdriver
from selenium.webdriver.common.keys import Keys


print "Checking up FACEBOOK..."
browser = webdriver.Chrome()
browser.get('https://www.facebook.com/')
browser.find_element_by_id('email').send_keys("ahuvim54@gmail.com")
browser.find_element_by_id('pass').send_keys("123456")
browser.find_element_by_id('loginbutton').click()
print "Everything is OK"

browser.quit()