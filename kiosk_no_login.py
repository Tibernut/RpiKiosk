import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

#caps = DesiredCapabilities.FIREFOX
#caps["marionette"] = True
#caps["binary"] = "/usr/bin/firefox"


#Open first tab
browser = webdriver.Firefox()
browser.get("https://www.reddit.com")


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
