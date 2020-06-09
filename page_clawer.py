from bs4 import BeautifulSoup
import requests
import csv
import json


# 爬取一个页面
def layoutdesigninfor(suffix):
 import re
 res = requests.get("http://www.sipo.gov.cn/jcdlzyqgg/"+suffix)
 res.encoding=res.apparent_encoding
 # 先变成2进制 再解码，通过Unicode作为映射表
 bs = BeautifulSoup(res.text,"lxml")
 # 布图设计登记号：BS.185559220
 # id_regex = re.compile(r"[布图设计登记号|布图登记号]\s*[:|：]\s*(\w+\.?\w+)")
 id_regex = re.compile(r"[布图设计登记号|布图登记号]\s*[:|：]\s*(.+)")
 total_information={}
 for p in bs.find_all("div"):
     indivdual={}
     bs_attribute=list(p.stripped_strings)
     for atr in bs_attribute :
      reg =  re.search(id_regex,atr)
      if  reg is None :
          continue

      else :
         id = reg.group(1)
         for term in bs_attribute:
          terms = (re.split("：|:",term))
          if len(terms)>=2:
           indivdual.update({terms[0]:terms[1]})
          # else:print(str(terms)+"错误")
          total_information.update({id: indivdual})
         break
         # 跳出外层循环

 for p in bs.find_all("p"):
     indivdual = {}
     bs_attribute = list(p.stripped_strings)
     for atr in bs_attribute:
         reg = re.search(id_regex, atr)
         if reg is None:
             continue

         else:
             id = reg.group(1)
             for term in bs_attribute:
                 terms = (re.split("：|:", term))
                 if len(terms) >= 2:
                     indivdual.update({terms[0]: terms[1]})
                 # else:
                     # print(str(terms) + "错误")
                 total_information.update({id: indivdual})
             break








 return total_information







# with open("context for page","r") as f:
with open("context for page", "r") as f:
 reader = csv.reader(f,"excel")
 for row in reader:
  print(row)
  itemid=row[0]
  date=row[1]
  js = json.dumps(layoutdesigninfor(itemid), indent=4, ensure_ascii=False)
  print(js)
  with open("data/data"+date,"w") as wf :
   wf.write(js)