import subprocess
from selenium import webdriver

# file = subprocess.Popen("C:\\Users\\biswa\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
file = subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "www.facebook.com"])

driver = webdriver.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

username = driver.find_element_by_id("email")
username.send_keys("biswassagar927@gmail.com")