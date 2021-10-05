# import subprocess
from selenium import webdriver

# file = subprocess.Popen("C:\\Users\\biswa\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
file = subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "www.facebook.com"])

driver = webdriver.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

userid = input("Enter Your User ID: ")
userpassword = input("Enter Your Password: ")

username = driver.find_element_by_id("email")
username.send_keys(userid)

password = driver.find_element_by_id("password")
password.send_keys(userpassword)
