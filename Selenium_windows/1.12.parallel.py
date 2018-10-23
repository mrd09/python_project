# -*- coding: utf-8 -*-
import multiprocessing
import os #for method os.getcwd()
from selenium import webdriver
#Chrome can not use in centos 6.X
import time
import datetime

future = '2018-10-15 14:34:00'
print(future); print(type(future))
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(now); print(type(now))

def easy_reg(url):
    driver = webdriver.Firefox()
    global now
    try:
        #Access Link:
        driver.get(url)
        time.sleep(3)
    
        #Login:
        username=driver.find_element_by_id("username")
        password=driver.find_element_by_id("password")
    
        username.send_keys("onme")
        password.send_keys("castis")
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
        series=driver.find_element_by_partial_link_text("Bạch Ngọc Đường")
        series.click()
        time.sleep(3)
    
        #Select Movie
        movie=driver.find_element_by_id("fileSelectBtn")
        movie.click()
        time.sleep(3)
    
        movie=driver.find_element_by_xpath("//tr[1]/td[4]/button")
        movie.click()
        time.sleep(3)
    
        #Select Encoding Option
        encode_HD=driver.find_element_by_xpath("//div[2]/div[18]/div/div[2]/label/span[contains(..,'HD')]")
        if not encode_HD.is_selected():
           #encode.click()
           time.sleep(2)
    
        encode_HQ=driver.find_element_by_xpath("//div[2]/div[18]/div/div[3]/label/span[contains(..,'HQ')]")
        if not encode_HQ.is_selected():
           encode_HQ.click()
           time.sleep(2)
    
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
    
        #Select Picture
        picture=driver.find_element_by_id("input-poster")
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
            save=driver.find_element_by_id("saveButton")
            print(save)
            save.click()

    except Exception as e:
        print(e)

def easy_reg2(url):
    driver = webdriver.Firefox()
    global now
    
    try:
        #Access Link:
        driver.get(url)
        time.sleep(3)
    
        #Login:
        username=driver.find_element_by_id("username")
        password=driver.find_element_by_id("password")
    
        username.send_keys("onme")
        password.send_keys("castis")
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
        series=driver.find_element_by_partial_link_text("Bạch Ngọc Đường")
        series.click()
        time.sleep(3)
    
        #Select Movie
        movie=driver.find_element_by_id("fileSelectBtn")
        movie.click()
        time.sleep(3)
    
        movie=driver.find_element_by_xpath("//tr[2]/td[4]/button")
        movie.click()
        time.sleep(3)
    
        #Select Encoding Option
        encode_HD=driver.find_element_by_xpath("//div[2]/div[18]/div/div[2]/label/span[contains(..,'HD')]")
        if not encode_HD.is_selected():
           #encode.click()
           time.sleep(2)
    
        encode_HQ=driver.find_element_by_xpath("//div[2]/div[18]/div/div[3]/label/span[contains(..,'HQ')]")
        if not encode_HQ.is_selected():
           encode_HQ.click()
           time.sleep(2)
    
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
    
        #Select Picture
        picture=driver.find_element_by_id("input-poster")
        picture.send_keys(os.getcwd()+"/horizon_poster.jpg") # is located right next to the running script in the same directory
        time.sleep(2)
    
        #Save to register
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
            save=driver.find_element_by_id("saveButton")
            print(save)
            save.click()

    except Exception as e:
        print(e)

if __name__ == '__main__':
    url="http://192.168.0.126:18087/CMSAdmin"
    p1 = multiprocessing.Process(target=easy_reg, args=(url,))
    p2 = multiprocessing.Process(target=easy_reg2, args=(url,))
    p1.start()
    p2.start() 

    p1.join()
    p2.join()

    print("Done")

#driver.close()
