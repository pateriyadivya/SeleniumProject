from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#Give path to the browser driver
service_obj = Service("C:/Users/divya/Downloads/chromedriver_win32/chromedriver.exe")

#If the browser closes automatically, below is how to sustain
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#DriverObj is intermediation bw our system and chrome
driver = webdriver.Chrome(service=service_obj)

#Get to the URL
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Selenium supports locators: ID, Xpath, name, classname, CSSSelector, linkText
#Lets find the email locator to enter the address
driver.find_element(By.NAME, "email").send_keys("pateriya@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

#When ID, Name etc is unavailable and you have to create your own attribute
#Custom Xpath Syntax://tagname[@attribute='value'] --> //input[@type='submit']
# CSSSelector: tagname[attribute='value'] --> input[type='submit'] OR #ID's value OR .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Divya Pateriya")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#==========Static dropdowns============

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#dropdown.select_by_index(1) # indices start from 0
dropdown.select_by_visible_text("Female")
# dropdown.select_by_value("stud") # if there is a value attribute

driver.find_element(By.XPATH, "//input[@type='submit']").click()

#To make sure certain message show up on screen after a click ie submit in this case
# In class, there are many classes separated by spaces (when you inspect on the desired popup msg)
msg = driver.find_element(By.CLASS_NAME, "alert-success").text # text property only retrieves the text associated with class
print(msg)

#check if we see "success" in message
assert "Success" in msg

# ============== NOTE =================
# There is a chrome plugin to validate the CSSSelector and Xpath if its unique or not
# plugin = Selectorshub: Just add to chrome, when you inspect on it, write your own Xpath/CSSSelector
# and see if its unique for the attribute you want

# If you write an Xpath and there are multiple items matching, then enclose the Xpath in ()[n]
# Say if 3 elements identified with type = submit, but you mean the third place (input[type='submit'])[3]
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello there")

#In order to ignore the 2 way binding happening in the text box
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()