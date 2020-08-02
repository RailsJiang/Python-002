from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()

    browser.get("https://shimo.im/login?from=home")
    time.sleep(1)
    browser.find_element_by_name("mobileOrEmail").send_keys("123456789")
    browser.find_element_by_name("password").send_keys("test")

    time.sleep(1)
    browser.find_element_by_xpath('//button[contains(@class, "sm-button submit sc-1n784rm-0 bcuuIb")]').click()

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)
except Exception as e:
    print(e)
finally:
    browser.close()