from selenium import webdriver
import time
import urllib
import os
import shutil
import requests
from bs4 import BeautifulSoup

#Initialize selenium with chromedriver
headers = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
        }

keyword = "Tokyo Station Building" 
num = 100 
driver = webdriver.Chrome(executable_path="/Users/kokiyahata/Desktop/imageCollector/chromedriver")

def searchImage(keyword, num):
    driver.get("https://www.google.com/imghp?hl=en")
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(keyword)
    search_box.submit()

    url = driver.current_url
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    
    path = "./images/{}".format(keyword)
    if not os.path.exists(path):
        os.makedirs(path)
    print(len(soup.find_all("img")[1:])) 
    for img in soup.find_all("img")[1:]:
        imgUrl = img.get("src")
        num_file = len([name for name in os.listdir(path)]) 
        imgPath = "img_" + str(num_file) + ".png"
        if not os.path.exists(os.path.join(path, imgPath)):
            with open(os.path.join(path, imgPath), "wb") as f:
                f.write(requests.get(imgUrl,headers=headers).content)
        if num_file == 100:
            break
    driver.quit()
searchImage(keyword, num)


