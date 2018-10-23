# -*- coding: utf-8 -*-
import multiprocessing
import os #for method os.getcwd()
from selenium import webdriver
#Chrome can not use in centos 6.X
import time
import datetime
from selenium.webdriver.common.keys import Keys

future = '2018-10-17 14:39:00'
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
    
        username.send_keys("onme_datviet1")
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

        #Select term target HD+HQ
        encoding=driver.find_element_by_id("s2id_autogen4")
        encoding.click()
        encoding.send_keys("HD+HQ")
        encoding.send_keys(Keys.DOWN)
        encoding.send_keys(Keys.ENTER)
        time.sleep(2)

        #Select Movie
        movie=driver.find_element_by_id("fileSelectBtn")
        movie.click()
        time.sleep(3)
    
        movie=driver.find_element_by_xpath("//tr[1]/td[3]/button")
        movie.click()
        time.sleep(3)
    
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
    
        username.send_keys("vt_onme")
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

        #Select term target HD+HQ
        encoding=driver.find_element_by_id("s2id_autogen4")
        encoding.click()
        encoding.send_keys("HD+HQ")
        encoding.send_keys(Keys.DOWN)
        encoding.send_keys(Keys.ENTER)
        time.sleep(2)

        #Select Movie
        movie=driver.find_element_by_id("fileSelectBtn")
        movie.click()
        time.sleep(3)
    
        movie=driver.find_element_by_xpath("//tr[2]/td[3]/button")
        movie.click()
        time.sleep(3)

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
    url="http://192.168.0.126:18089/CMSAdmin"
    p1 = multiprocessing.Process(target=easy_reg, args=(url,))
    p2 = multiprocessing.Process(target=easy_reg2, args=(url,))
    p1.start()
    p2.start() 

    p1.join()
    p2.join()

    print("Done")

#driver.close()
