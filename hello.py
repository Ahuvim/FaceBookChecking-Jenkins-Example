from selenium import webdriver
import os
import time


print "Checking up FACEBOOK..."
try:
    browser = webdriver.Chrome()
    browser.get('https://www.facebook.com/')
    browser.find_element_by_id('email').send_keys("ahuvim54@gmail.com")
    browser.find_element_by_id('pass').send_keys("123456")
    browser.find_element_by_id('loginbutton').click()
    time = time.time()
    new = r"C:\Users\Maor Ahuvim\Documents"+ "\\" + str(time)
    browser.get_screenshot_as_file(new+".png")
    print "Everything is OK"
except:
    "Not Good"
finally:
    browser.quit()
