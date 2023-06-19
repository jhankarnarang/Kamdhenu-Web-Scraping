from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

csv_file = open('Kamdhenu_pipes.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Prod_info','Prod_img'])
l = []
m=[]
source = requests.get('https://www.kamdhenulimited.com/kamdhenu-pipes.php')
soup = BeautifulSoup(source.content, 'lxml')

prod = soup.select_one('body>div>div>div>div.brand-right')
# prod_info = prod.select_one('p').text.strip()
# prod_info = prod_info.replace('\n',' ')
# print(prod_info)
# prod_info2 = prod.select_one('p:nth-child(5)').text
# prod_info2 = prod_info2.replace('\n\n\n\n',' ')
# prod_info2 = prod_info2.replace('\n',' ')
# print(prod_info2)

for info in prod.find_all('p'):
    info = info.text.strip()
    m.append(info)

prod_info = ' , '.join(str(e) for e in m)
print(prod_info)


for img in prod.find_all('img'):
    p_img = img['src']
    p_img = f'https://www.kamdhenulimited.com/{p_img}'
    l.append(p_img)


prod_img = ' , '.join(str(e) for e in l)
print(prod_img)


# prod_tech1 = prod_tech+prod2

csv_writer.writerow([prod_info,prod_img])

