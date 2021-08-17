from selenium import webdriver
import time
import urllib.parse
import os
#Initialize selenium with chromedriver
driver = webdriver.Chrome(executable_path="/Users/kokiyahata/Desktop/imageCollector/chromedriver")

def searchImage(keyword, num):
    os.mkdir("/Users/kokiyahata/Desktop/imageCollector/images/" + keyword) 
    driver.get("https://www.google.com/imghp?hl=EN")
    time.sleep(2)
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(keyword)
    search_box.submit()

    for i in range(1, num):
        try:
            driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot("/Users/kokiyahata/Desktop/imageCollector/images/" + keyword + "/" + keyword + str(i) + ".png")
        except:
            pass

searchImage("Tokyo Tower", 100)
