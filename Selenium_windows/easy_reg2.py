# -*- coding: utf-8 -*-
import os #for method os.getcwd()
from selenium import webdriver
#Chrome can not use in centos 6.X

import time
import datetime #for time Save Register control

future = '2018-10-15 14:10:00'
print(future); print(type(future))
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(now); print(type(now))

driver_2 = webdriver.Firefox()

try:
    #Access Link:
    driver_2.get("http://192.168.0.126:18087/CMSAdmin")
    time.sleep(2)

    #Login:
    username=driver_2.find_element_by_id("username")
    password=driver_2.find_element_by_id("password")

    username.send_keys("onme")
    password.send_keys("castis")
    password.submit()
    time.sleep(5)

    # Navigate "Easy Register":
    easyreg=driver_2.find_element_by_link_text('Easy Registration')
    easyreg.click()
    time.sleep(2)

    #Select Series
    series=driver_2.find_element_by_id("linkSelectBtnSeries")
    series.click()
    time.sleep(2)
    series=driver_2.find_element_by_partial_link_text("Bạch Ngọc Đường")
    series.click()
    time.sleep(3)

    #Select Movie
    movie=driver_2.find_element_by_id("fileSelectBtn")
    movie.click()
    time.sleep(3)

    movie=driver_2.find_element_by_xpath("//tr[2]/td[4]/button")
    movie.click()
    time.sleep(3)

    #Select Encoding Option
    encode_HD=driver_2.find_element_by_xpath("//div[2]/div[18]/div/div[2]/label/span[contains(..,'HD')]")
    if not encode_HD.is_selected():
       #encode.click()
       time.sleep(2)

    encode_HQ=driver_2.find_element_by_xpath("//div[2]/div[18]/div/div[3]/label/span[contains(..,'HQ')]")
    if not encode_HQ.is_selected():
       encode_HQ.click()
       time.sleep(2)

    #Select Target Service Option
    #device_STB=
    device_STB=driver_2.find_element_by_xpath("//div[2]/div[19]/div/div[1]/label/span")
    device_STB.click()

    device_STB4K=driver_2.find_element_by_xpath("//div[2]/div[19]/div/div[2]/label/span")
    device_STB4K.click()

    device_OTT=driver_2.find_element_by_xpath("//div[2]/div[19]/div/div[3]/label/span")
    device_OTT.click()

    device_CC1=driver_2.find_element_by_xpath("//div[2]/div[19]/div/div[4]/label/span")
    device_CC1.click()

    device_CC2=driver_2.find_element_by_xpath("//div[2]/div[19]/div/div[5]/label/span")
    device_CC2.click()

    #Select Picture
    picture=driver_2.find_element_by_id("input-poster")
    picture.send_keys(os.getcwd()+"/horizon_poster.jpg") # is located right next to the running script in the same directory
    time.sleep(2)

    #Save to register
    while (now < future):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(now)

    if (now > future):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(now)
        print("Modify the future")
        os.system('kill %d' % os.getpid())
    if (now == future):
        print("It's reach in time")
        save=driver_2.find_element_by_id("saveButton")
        print(save)
        save.click()

except Exception as e:
    print(e)

#driver.close()
