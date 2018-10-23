# -*- coding: utf-8 -*-
import os #for method os.getcwd()
from selenium import webdriver
#Chrome can not use in centos 6.X
#path=os.getcwd()+r'\geckodriver.exe'

import time
import datetime #for time Save Register control

# future = '2018-10-15 14:10:00'
# print(future); print(type(future))
# now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(now); print(type(now))

path="C:/Python/Python36/browser_driver/geckodriver.exe"  #Path for Windows

driver = webdriver.Firefox(executable_path=path)

# Input infor:

url="http://192.168.0.126:18087/CMSAdmin"

#url="http://10.60.70.200:18082/CMSAdmin"

# User login
user="onme"
passw="castis"

# Select movie + preview
number=2

movie_position="//tr[%s]/td[4]/button" % (number)

number +=1
preview_position="//tr[%s]/td[4]/button" % (number)

# Select series
series_name="Bạch Ngọc Đường"

#series_name="Series_ONME"

# Input Title
title_text="_Viettel_EasyReg_CleanAll_EncodeSub_Preview"

# Select subtitle
subtitle_name=r'\test.srt'

# Select picture
picture_name=r'\horizon_poster.jpg'

try:
    #Access Link:
    driver.get(url)
    time.sleep(2)

    #Login:
    username=driver.find_element_by_id("username")
    password=driver.find_element_by_id("password")

    username.send_keys(user)
    password.send_keys(passw)
    password.submit()
    time.sleep(5)

    # Navigate "Easy Register":
    easyreg=driver.find_element_by_link_text('Easy Registration')
    easyreg.click()
    time.sleep(2)

    #Select Series
    series=driver.find_element_by_id("linkSelectBtnSeries")
    series.click()
    time.sleep(2)
    series=driver.find_element_by_partial_link_text(series_name)
    series.click()
    time.sleep(3)

    #In put Title
    title=driver.find_element_by_id("offer.title")
    title.send_keys(title_text)

    #Select Movie
    movie=driver.find_element_by_id("fileSelectBtn")
    movie.click()
    time.sleep(2)

    #movie=driver.find_element_by_xpath("//tr[2]/td[4]/button")
    movie=driver.find_element_by_xpath(movie_position)
    movie.click()
    time.sleep(2)

    #Select Subtitle File
    subtitle=driver.find_element_by_id("input-subtitle")
    #picture.send_keys(os.getcwd()+"\\test.srt") # is located right next to the running script in the same directory
    subtitle.send_keys(os.getcwd()+subtitle_name)
    time.sleep(2)

    # *** If encode with subtitle will disable Already Encoded, Already Encrypted
    # => If select the subtitle autodisable Already Encoded, Already Encrypted

    # AlreadyEncode=driver.find_element_by_xpath("//div[2]/div[16]/div/div/label/span")
    # + first find the checkbox by xpath to scroll into view
    # + Then find the checkbox by id to verify the checkbox with: is_selected()
#    AlreadyEncode=driver.find_element_by_xpath("//div[2]/div[16]/div/div/label/span")
#    AlreadyEncode=driver.find_element_by_id("useEncoded")
#    if AlreadyEncode.is_enabled():  # Check check box condition with find by id
#        if AlreadyEncode.is_selected():
#            AlreadyEncode=driver.find_element_by_xpath("//div[2]/div[16]/div/div/label/span")
#            AlreadyEncode.click()
#            print('Checkbox AlreadyEncode unchecked');
#        else:
#            print('Checkbox AlreadyEncode not select')
#    else:
#        print('Checkbox AlreadyEncode is disabled')

    encode_SD=driver.find_element_by_id("encodingOptionHD")
    if encode_SD.is_enabled():
        if encode_SD.is_selected():
            print('Checkbox encode_SD already selected');
        else:
            encode_SD.click()
            print('Checkbox encode_SD selected')
    else:
        print('Checkbox encode_SD is disabled')

    #Select Encoding Option
    # encode_HD=driver.find_element_by_xpath("//div[2]/div[18]/div/div[2]/label/span[contains(..,'HD')]")
    encode_HD=driver.find_element_by_id("encodingOptionHD")
    if encode_HD.is_enabled():
        if encode_HD.is_selected():
            print('Checkbox encode_HD already selected');
        else:
            encode_HD.click()
            print('Checkbox encode_HD selected')
    else:
        print('Checkbox encode_HD is disabled')

    # Can not do any method to scroll in view with checkbox element encodingOptionHQ: do not know the reason
    encode_HQ=driver.find_element_by_xpath("//div[2]/div[18]/div/div[3]/label/span[contains(..,'HQ')]")
    encode_HQ.click()
   
    #Select Target Service Option
    #device_STB=
    device_STB=driver.find_element_by_xpath("//div[2]/div[19]/div/div[1]/label/span")
    device_STB.click()

    device_STB4K=driver.find_element_by_xpath("//div[2]/div[19]/div/div[2]/label/span")
    device_STB4K.click()

    device_OTT=driver.find_element_by_xpath("//div[2]/div[19]/div/div[3]/label/span")
    device_OTT.click()

    device_CC1=driver.find_element_by_xpath("//div[2]/div[19]/div/div[4]/label/span")
    device_CC1.click()

    device_CC2=driver.find_element_by_xpath("//div[2]/div[19]/div/div[5]/label/span")
    device_CC2.click()

    #Select Preview
    preview=driver.find_element_by_id("fileSelectBtn3")
    preview.click()
    time.sleep(2)


    preview=driver.find_element_by_xpath(preview_position)
    preview.click()
    time.sleep(2)   

    #Select Picture
    picture=driver.find_element_by_id("input-poster")
    picture.send_keys(os.getcwd()+picture_name) # is located right next to the running script in the same directory
    time.sleep(2)

#   #Save to register
#   while (now < future):
#       now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#       print(now)

#   if (now > future):
#       now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#       print(now)
#       print("Modify the future")
#       os.system('kill %d' % os.getpid())
#   if (now == future):
#       print("It's reach in time")
#       save=driver.find_element_by_id("saveButton")
#       print(save)
#       save.click()

except Exception as e:
    print(e)

#driver.close()
