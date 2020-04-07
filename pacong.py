import os

import requests
import time
from bs4 import BeautifulSoup

url="https://www.woyaogexing.com/touxiang/fengjing/"


def get_all_image():
     respon = requests.get(url)
     html = respon.content.decode('utf-8')
     soup = BeautifulSoup(html, 'html.parser')
     img_list = soup.find_all('div', attrs={'id': 'main'})[0].find_all('div', attrs={'class': 'pMain'})[0].find_all('div', attrs={'class': 'txList'})
     for num in range(len(img_list)):

         img_url= 'https://www.woyaogexing.com'+img_list[0].find_all('a')[0].attrs['href']
         img_tittle=img_list[num].find_all('a')[0].attrs['title'].replace('/','').replace(':','')
         path='./data/img/'+str(img_tittle)
         if os.path.exists(path) == False:
             os.mkdir(path)
         print(img_url)
         get_one_page_iamge(img_url,path,img_tittle)


def get_one_page_iamge(url,path,tittle):

     respon = requests.get(url)
     html = respon.content.decode('utf-8')
     soup = BeautifulSoup(html, 'html.parser')
     img_list = soup.find_all('div', attrs={'id': 'main'})[0].find_all('div', attrs={'class': 'contLeftA'})[0].find_all(
         'li', attrs={'class': 'tx-img'})
     for num in range(len(img_list)):

        img_url='http:' +img_list[num].find_all('a')[0].attrs['href']
        # print(img_url)
        get_one_Image(img_url,num,path,tittle)


def get_one_Image(url,num,path,tittle):
    resp = requests.get(url)
    with open(path+'/' + str(num) + '.jpg', 'wb') as file:
        file.write(resp.content)
        print(f"主题--{tittle}-第{num}张图片下载完成！！")
        time.sleep(0.2)   #防止网站禁掉ip


get_all_image()
