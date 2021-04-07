"""
Run the code and you’ll see that a Firefox browser opens and directs you to the Instagram login page. Here’s a line-by-line breakdown of the code:

Lines 1 and 2 import sleep and webdriver.
Line 4 initializes the Firefox driver and sets it to browser.
Line 6 types https://www.instagram.com/ on the address bar and hits Enter.
Line 8 waits for five seconds so you can see the result. Otherwise, it would close the browser instantly.
Line 10 closes the browser.

"""

from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://www.instagram.com/')

sleep(5)

browser.close()