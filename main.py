"""
# Instagram bot

In this work, I make an insta bot with python

What do SocialCaptain, Kicksta, Instavast, and many other companies have in common?
They all help you reach a greater audience, gain more followers, and get more likes on Instagram while
you hardly lift a finger. They do it all through automation, and people pay them a good deal of money for it.
But you can do the same thing—for free—using InstaPy!

How Instagram bots work
How to automate a browser with Selenium
How to use the Page Object Pattern for better readability and testability
How to build an Instagram bot with InstaPy

By Siavash Hakim Elahi

"""
from selenium import webdriver
from helper_function import HomePage

browser = webdriver.Firefox()
browser.implicitly_wait(5)

home_page = HomePage(browser)
login_page = home_page.go_to_login_page()
login_page.login("<your username>", "<your password>")

browser.close()



