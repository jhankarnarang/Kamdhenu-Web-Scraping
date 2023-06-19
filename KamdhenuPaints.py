from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

csv_file = open('KamdhenuPaints.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Prod_info','Ext_Img','Int_img','Des_img'])

source = requests.get('https://www.kamdhenulimited.com/decorative-paints.php')
soup = BeautifulSoup(source.content, 'lxml')

prod = soup.select_one('body>div>div>div>div.brand-right')
# prod_name = prod.h1.text
# print(prod_name)
prod_info = prod.select_one('p').text
prod_info = prod_info.replace('\n',' ')
print(prod_info)

ext_img = soup.select_one('p:nth-child(7)').img['src']
ext_img = f'https://www.kamdhenulimited.com/{ext_img}'
print(ext_img)

int_img = soup.select_one('p:nth-child(8)').img['src']
int_img = f'https://www.kamdhenulimited.com/{int_img}'
print(int_img)

des_img = soup.select_one('p:nth-child(8)').img['src']
des_img = f'https://www.kamdhenulimited.com/{des_img}'
print(des_img)

csv_writer.writerow([prod_info,ext_img,int_img,des_img])

