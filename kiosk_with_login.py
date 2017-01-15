import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#caps = DesiredCapabilities.FIREFOX
#caps["marionette"] = True
#caps["binary"] = "/usr/bin/firefox"


#Open first tab
browser = webdriver.Firefox()
browser.get("https://www.reddit.com")
browser.implicitly_wait(20)
user = browser.find_element_by_name('user')
passw = browser.find_element_by_name('passwd')
form = browser.find_element(By.XPATH, '//button[text()="login"]')
user.send_keys('yourusername')
passw.send_keys('yourpassword')
form.submit()


#Open second tab
new_window = browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "t")
browser.switch_to.window(browser.window_handles[-1])
browser.get("http://www.google.com")


#Open third tab
new_window = browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "t")
browser.switch_to.window(browser.window_handles[-1])
browser.get("https://slashdot.org")


#browser fullscreen
new_window = browser.find_element_by_tag_name("body").send_keys(Keys.F11)


#Every 20 secs change tab
x=1
while x:
	try:
		new_window = browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + Keys.TAB)
		time.sleep(20)
	except:
		break
