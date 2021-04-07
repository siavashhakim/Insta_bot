"""
Line 5 sets five seconds of waiting time. If Selenium can’t find an element, then it waits for five seconds to allow everything to load and tries again.
Line 9 finds the element <a> whose text is equal to Log in. It does this using XPath, but there are a few other methods you could use.
Line 10 clicks on the found element <a> for the login link.

"""

from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')


login_link = browser.find_element_by_xpath("//a[text()='Log in']")
login_link.click()

sleep(5)

browser.close()