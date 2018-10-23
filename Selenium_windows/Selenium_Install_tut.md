# INSTALL
- yum install firefox 
- pip install selenium
- install webdriver firefox:
	+ wget: wget https://github.com/mozilla/geckodriver/releases/download/v0.22.0/geckodriver-v0.22.0-linux64.tar.gz
	+ tar -xzf geckodriver-v0.22.0-linux64.tar.gz
	+ mv geckodriver /usr/local/bin/
	+ export PATH=$PATH:/usr/local/bin/geckodriver 
    
- If want to use geckodriver in Windows: Edit system environment variable/Set user Variable for PC
    + Include in script:
        path="C:/Python/Python36/browser_driver/geckodriver.exe"
        driver = webdriver.Firefox(executable_path=path)

- Find and enable: the option forward X11 connections for X DISPLAY: localhost:0.0
	SSH/Tunneling
- Install and start xming server in remote host
	vim /etc/ssh/sshd_config
		X11Forwarding yes

# Comparasion:
- The webbrowser module has an open() method that will launch a web browser to a specifi URL, and that’s it. 
- The requests module can download fies and pages from the Web. 
- The BeautifulSoup module parses HTML. 
- Finally, the selenium module can launch and control a browser.


# USING QUICK:
- Quick using: [Selenium Python Tut](https://selenium-python.readthedocs.io/navigating.html#drag-and-drop)

- Library common usage case:
```
import os #for method os.getcwd() 
from selenium import webdriver  # for use selenium
#Chrome can not use in centos 6.X
from selenium.webdriver.support.ui import Select # for select tag
from selenium.webdriver.support.ui import WebDriverWait # for wait element to scroll into view
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys # for send special keys: enter, up, down ...

import time # use for wait time.sleep(1)
import datetime #for time Save Register control: make hold point by control OS time count

import multiprocessing  # for run parallel selenium webdriver
```

=> find the id by:
- navigate to the field: Inspect Element: RightClick: 
	+ Copy Element
		<input type="text" name="username" id="username" class="form-control input-lg" placeholder="UserId">
		=> find_element_by_id("username")
	+ Copy Outer HTML(Firefox)
		<button class="btn" type="button" id="fileSelectBtn" style="">Select </button>		
		=> find_element_by_id("fileSelectBtn")

		<a href="javascript:selectBox('1785', 'Bạch Ngọc Đường')">Bạch Ngọc Đường</a>
		=> find_element_by_partial_link_text("Bạch Ngọc Đường")

	+ Copy XPath
		/html/body/div[3]/div/div/div/div/div/div[1]/div/table/tbody/tr[2]/td[4]/button
			=> find_element_by_xpath("//tr[2]/td[4]/button")

- Upload picture by selenium + python: [Upload Picture](https://stackoverflow.com/questions/8665072/how-to-upload-file-picture-with-selenium-python)
```
    #Select Picture
    picture=driver.find_element_by_id("input-poster")
    picture.send_keys(os.getcwd()+"/horizon_poster.jpg") # is located right next to the running script in the same directory
```

- click on checkboxes based on label text: [Click on checkbox](https://stackoverflow.com/questions/45021204/how-to-click-on-checkboxes-based-on-label-text)
    + Copy the xpath:
        /html/body/div[1]/div[3]/form/div[2]/div[18]/div/div[2]/label/span
    + get the xpath then click:
        encode=driver.find_element_by_xpath("//div[2]/div[18]/div/div[2]/label/span[contains(..,'HD')]")
        encode.click()

- verify the checkbox if checked or not: 
    + first find the checkbox by xpath to scroll into view
    + Then find the checkbox by id to verify the checkbox with: is_selected()

```
    print('find by xpath firt to scroll into view to the checkbox find by id')
    AlreadyEncode=driver.find_element_by_xpath("//div[2]/div[16]/div/div/label/span")
    print('find by id')
    AlreadyEncode=driver.find_element_by_id("useEncoded")
    if AlreadyEncode.is_enabled():  # Check check box condition with find by id
        print('go to if loop 1')
        if AlreadyEncode.is_selected():
            print('go to if loop 2 recall find by xpath to click success')
            AlreadyEncode=driver.find_element_by_xpath("//div[2]/div[16]/div/div/label/span")
            AlreadyEncode.click()
            print('Checkbox AlreadyEncode unchecked');
        else:
            print('Checkbox AlreadyEncode not select')
    else:
        print('Checkbox AlreadyEncode is disabled')
```

- Control time submit/save by make a hold point check by OS time: datetime, now() library
```
future = '2018-10-15 14:34:00'
print(future); print(type(future))
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(now); print(type(now))

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

```
- Multiprocessing: parallel selenium: multiprocessing library
```
if __name__ == '__main__':
    url="http://192.168.0.126:18087/CMSAdmin"
    p1 = multiprocessing.Process(target=easy_reg, args=(url,))
    p2 = multiprocessing.Process(target=easy_reg2, args=(url,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")
```
		
- Send variable from python to xpath:
```
    x = 'SEM W880 Black'
    browser.find_element_by_xpath("//span[contains(.,'" + x + "')]")
```

# TUT:

## 1.Finding Elements on the Page
Automate-the-Boring-Stuff-with-Python: Chapter 11: Web Scraping: Controlling the Browser with the selenium Module 
table 11-3: Selenium’s WebDriver Methods for Finding Elements 

+ -------------------------------------------------- + ------------------------------------------------------- +
+                    Method name                     +             WebElement object/list returned             +
+ -------------------------------------------------- + ------------------------------------------------------- +
| browser.find_element_by_class_name(name)           |          Elements that use the CSS class name           |
| browser.find_elements_by_class_name(name)          |                                                         |
+ -------------------------------------------------- + ------------------------------------------------------- +
| browser.find_element_by_css_selector(selector)     |          Elements that match the CSS selector           |
| browser.find_element_by_css_selector(selector)     |                                                         |
+ -------------------------------------------------- + ------------------------------------------------------- +
| browser.find_element_by_id(id)                     |       Elements with a matching id attribute value       |
| browser.find_elements_by_id(id)                    |                                                         |
+ -------------------------------------------------- + ------------------------------------------------------- +
| browser.find_element_by_link_text(text)            |  <a> elements that completely match the text provided   |
| browser.find_elements_by_link_text(text)           |                                                         |
+ -------------------------------------------------- + ------------------------------------------------------- +
| browser.find_element_by_partial_link_text(text)    |       <a> elements that contain the text provided       |
| browser.find_elements_by_partial_link_text(text)   |                                                         |
+ -------------------------------------------------- + ------------------------------------------------------- +
| browser.find_element_by_name(name)                 |      Elements with a matching name attribute value      |
| browser.find_elements_by_name(name)                |                                                         |
+ -------------------------------------------------- + ------------------------------------------------------- +
| browser.find_element_by_tag_name(name)             |  Elements with a matching tag name (case insensitive;   |
| browser.find_elements_by_tag_name(name)            |       an <a> element is matched by 'a'  and 'A' )       |
+ -------------------------------------------------- + ------------------------------------------------------- +
+ -------------------------------------------------- + ------------------------------------------------------- +
| browser.find_element_by_xpath(xpath)             |  Elements that match the xpath   |
| browser.find_elements_by_xpath(xpath)            |              |
+ -------------------------------------------------- + ------------------------------------------------------- +
+ -------------------------------------------------- + ------------------------------------------------------- +
|        Except for the *_by_tag_name() methods, the arguments to all the methods are case sensitive.          |
+ -------------------------------------------------- + ------------------------------------------------------- +
| If no elements exist => selenium module raises a NoSuchElement exception                                     |
| If you do not want this exception to crash your program, add try                                             |
| and except statements to your code.                                                                          |
+ -------------------------------------------------- + ------------------------------------------------------- +

## 2.Filling Out and Submitting Forms

+ --------------- + ------------------------------------------------------- +
+   Method name   +                    Action in Webpage                    +
+ --------------- + ------------------------------------------------------- +
|   send_keys()   |     Sending keystrokes to text fields on a web page     |
|                 |      of finding the <input> or <textarea> element       |
+ --------------- + ------------------------------------------------------- +
|    submit()     | Same result as clicking the Submit button for the form  |
+ --------------- + ------------------------------------------------------- +

## 3.Clicking the Page

+ --------------- + ------------------------------------------------------- +
+   Method name   +                    Action in Webpage                    +
+ --------------- + ------------------------------------------------------- +
|     click()     |         simulates a mouse click on that element         |
+ --------------- + ------------------------------------------------------- +


## 4.Sending Special Keys

from selenium.webdriver.common.keys import Keys

Keys.DOWN, Keys.UP, Keys.LEFT,
Keys.RIGHT
Keys.ENTER, Keys.RETURN
Keys.HOME, Keys.END, Keys.PAGE_DOWN,
Keys.PAGE_UP
Keys.ESCAPE, Keys.BACK_SPACE,
Keys.DELETE
Keys.F1, Keys.F2, ..., Keys.F12
Keys.TAB The tab key

## 5.Clicking Browser Buttons
browser.back() Clicks the Back button.
browser.forward() Clicks the Forward button.
browser.refresh() Clicks the Refresh/Reload button.
browser.quit() Clicks the Close Window button.

## 6.More Information on Selenium
Selenium can do much more beyond the functions described here. It can
modify your browser’s cookies, take screenshots of web pages, and run
custom JavaScript. To learn more about these features, you can visit the
Selenium documentation at http://selenium-python.readthedocs.org/.

## 7.click option in dropdown menu which does not have “select” tag using Selenium Python?
First step would be clicking on the dropdown  
Then finding a generic locator for the values of the dropdown by keys: up, down, enter 

## 8. Select option from select tag:
from selenium.webdriver.support.ui import Select

select = Select(driver.find_element_by_id('fruitType'))
    # Now we have many different alternatives to select an option.
select.select_by_index(4)
select.select_by_visible_text("jumbo fruit 4")
select.select_by_value('4') #Pass value as string

# Example:
## Example 1: Easy Registration:
- easy_reg.py and easy_reg2.py: version 1.12

## Example 2: Parallel Save 2 selenium browser:
- parallel.py: version 1.12
- 1.8.2.parallel.py: version 1.8.2