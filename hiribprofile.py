from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

csv_file = open('Tileprofilesheets.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Prod_info','Image'])
l=[]
m=[]
source = requests.get('https://www.kamdhenulimited.com/kamdhenu-gold-tiles.php')
soup = BeautifulSoup(source.content, 'lxml')

prod = soup.select_one('body>div>div>div>div.brand-right')
# prod_name = prod.h1.text
# print(prod_name)
prod_info1 = prod.select_one('p').text
prod_info1 = prod_info1.replace('\n',' ')



for li in prod.find_all('li'):
    l.append(li.text)



prod_info2 = ''.join(str(e) for e in l)

prod_info = prod_info1+prod_info2
print(prod_info)

for pr_img in prod.find_all('img'):   
    pro_img = pr_img['src']
    prod_img = f'https://www.kamdhenulimited.com/{pro_img}'
    m.append(prod_img)


p_img  = ' , '.join(str(e) for e in m)
print(p_img)

csv_writer.writerow([prod_info,p_img])

