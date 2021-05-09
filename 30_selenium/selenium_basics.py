from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/sarsatis/Desktop/MyLaptop/Learnings/PythonLearnings/HundredDaysOfCode/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Sarthak")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Mahaveer")
email = driver.find_element_by_name("email")
email.send_keys("sarthak@gmail.com")

submit = driver.find_element_by_css_selector("form button")
submit.click()


driver.get("https://en.wikipedia.org/wiki/Main_Page")
search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.close()