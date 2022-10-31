import pandas as pd
import urllib.request
import re
from bs4 import BeautifulSoup
from openpyxl import load_workbook
import time




def Storage(url,id, ii):
    # header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59"}
    # # res = requests.get(url, headers=header, timeout=5)
    # res = requests.get(url)
    # print(res.text)
    # soup = BeautifulSoup(res.text, 'html.parser')
    # # print(soup.prettify())
    # print(soup.p)
    # # print(soup.contents)
    #
    #
    # Content = {res.text,res.status_code}
    # return res.text,
    # res = urllib.request.urlopen(url)
    # print(res.read())
    # info = res.read()
    # data =info.decode("utf-8")
    # print(data)
    # status = res.status
    # print(status)
    # soup = BeautifulSoup(data, "html5lib")
    # print(soup.prettify())
    def save_html(file_name, file_content):
        with open("web/"+file_name.replace('/', '_') + ".html", "wb") as f:
            f.write(file_content)
            f.close()
    try:
        html = urllib.request.urlopen(url, timeout=50).read()
    except:
        print("haha")
    # except:
    #     return 0
    id0 = str(ii) + "_"
    id1 = id0 + id
    save_html(id1, html)
    filename = "web/"+id1 +".html"


    # trasfer to .txt
    # soup = BeautifulSoup(open(filename), "lxml")
    # soup = BeautifulSoup(html,"lxml")
    # print(soup.prettify())
    # print(soup.text)
    # text_contene = soup.text
    # bytes1 = bytes(text_contene, encoding='utf-8')
    # print(bytes1)
    # with open("data/"+id1.replace('/', '_') + ".txt", "wb") as f1:
    #     f1.write(bytes1)
    #     f1.close()
# Storage(url,id)


def main():
    # wb1 = load_workbook('app_data.csv')
    wb1 = pd.read_csv('app_data.csv')
    # sheets = wb1.worksheets  # 获取当前所有的sheet
    # sheet1 = sheets[0]
    # rows = sheet1.rows
    # columns = sheet1.columns
    # print(rows)
    # print(columns)
    # print('')
    # print(wb1.iloc[0, 0])
    # print(wb1.iloc[2, 1])
    # print(wb1.iloc[2, 2])
    # print(wb1.iloc[2, 3])
    # print(wb1.iloc[2, 4])
    # print(wb1.iloc[2, 5])
    # print(wb1.iloc[2, 6])
    # print(wb1.iloc[2, 7])
    count = 10845


    # df = pd.read_csv('sample.csv')  # the file include pandafram
    # # send 2 means url
    # print(df.iloc[2, 1])
    # url = df.iloc[2, 2]
    # id = df.iloc[2, 1]
    # count = 10   # the count of all urls
    i = 28
    for i in range (count):
        if i <10243:
            continue
        url = wb1.iloc[i, 6]
        id = wb1.iloc[i, 1]
        try:
            Storage(url, id, i)
        except:
            continue
        print("this is the %s url",i)



if __name__== "__main__" :
       main()