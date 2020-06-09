from bs4 import BeautifulSoup
import  requests
import csv




response = requests.get("http://www.sipo.gov.cn/jcdlzyqgg/index.htm")
print(response)
bs = BeautifulSoup(response.text,"lxml")

with open("context for page","w",newline='') as f:
 for a in bs.find_all("li"):
         href = a.find("a").get("href")

         # "1109054.htm"

         writer = csv.writer(f,dialect='excel')

         print([href, list(a.find("span").stripped_strings)[0]])
         writer.writerow([href, list(a.find("span").stripped_strings)[0]])

 for page in range(1,19):
  print("new---------")
  response = requests.get("http://www.sipo.gov.cn/jcdlzyqgg/index"+str(page)+".htm")
  bs = BeautifulSoup(response.text,"lxml")

  for a in bs.find_all("li"):
    href = a.find("a").get("href")

    # "1109054.htm"


    print([href,list(a.find("span").stripped_strings)[0]])
    writer = csv.writer(f,dialect='excel')

    writer.writerow([href,list(a.find("span").stripped_strings)[0]])





