# importing python modules and some packages
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

# Driver Name and its Location
driver = webdriver.Chrome(
    executable_path="C:\Program Files (x86)\chromedriver.exe")

# Website Link Address
driver.get("https://www.thesparksfoundationsingapore.org/")

# Maximizing Window
driver.maximize_window()

try:
    driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/img').click()
    print("Inspection & Apperance of Logo is Verified")
except NoSuchElementException:
    print("Log Not Verified")
time.sleep(2)

# playing Video
video = driver.find_element_by_xpath('//*[@id="youtube-video"]')
video.click()
if(video.is_displayed()):
    print("Video Played")
else:
    print("Video is unplayed")
time.sleep(20)

# video Paused
video.click()
time.sleep(2)

# Performing Actions in Website

# AboutUs
about = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[1]/a')
about.click()
if(about.is_displayed()):
    print("About Us is Clicked")
else:
    print("About Us is not Detected")
time.sleep(2)

#Policies and Code
policies_and_code = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[2]/a')
policies_and_code.click()
if(policies_and_code.is_displayed()):
    print("policies_and_code is Clicked")
else:
    print("policies_and_code is not Detected")
time.sleep(2)

# Programs
programs = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[3]/a')
programs.click()
if(programs.is_displayed()):
    print("Programs is Clicked")
else:
    print("Programs is not Detected")
time.sleep(2)

# JoinUs
joinus = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[5]/a')
joinus.click()
if(joinus.is_displayed()):
    print("Join Us is Clicked")
else:
    print("Join Us is not Detected")
time.sleep(2)

# GRIP Page
try:
    intern = driver.get(
        'https://www.thesparksfoundationsingapore.org/join-us/internship-positions/')
    print("GRIP Internship Page is Opened")
except NoSuchElementException:
    print("GRIP is not Detected")
time.sleep(2)

# Form Filling
try:
    driver.find_element_by_link_text('Join Us').click()
    time.sleep(2)
    driver.find_element_by_link_text('Why Join Us').click()
    time.sleep(2)
    driver.find_element_by_name('Name').send_keys('Gowtham Kunjeti')
    time.sleep(2)
    driver.find_element_by_name('Email').send_keys('gowtham@gmail.com')
    time.sleep(2)
    select = Select(driver.find_element_by_class_name('form-control'))
    time.sleep(2)
    select.select_by_visible_text('Intern')
    time.sleep(2)
    print("Form Submitted")
    time.sleep(2)
except NoSuchElementException:
    print("Form Submission Aborted")
    time.sleep(2)

# Closing Website
cls = driver.close()
print("Website is Closed")