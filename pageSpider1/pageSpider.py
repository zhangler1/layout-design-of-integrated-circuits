# This is a sample Python script.
#%%
import re
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

bs=webdriver.Chrome("chromedriver.exe")
with open("pageIndex.csv","w",encoding="utf-8")as f:

    for page in range(1,46):

        bs.get("https://www.cnipa.gov.cn/col/col164/index.html?uid=669&pageNum="+str(page))
        ul = WebDriverWait(bs, 5, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="669"]/div/ul'))
        )
        tags=ul.find_elements_by_tag_name("a")
        for tag in tags:
            if re.search("集成电路布图设计专有权公告", tag.text):
                print(tag.get_attribute("href"))
                f.write(tag.text+","+tag.get_attribute("href")+"\r")
