from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

csv_file = open('KamdhenuNxt.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Prod_info','Prod_process', 'Prod_material','Prod_application','Prod_feature'])

source = requests.get('https://www.kamdhenulimited.com/kamdhenu-nxt-tmt-bars.php')
soup = BeautifulSoup(source.content, 'lxml')

prod = soup.select_one('body>div>div>div')
prod_info = prod.select_one('p:nth-child(8)').text
prod_info1 = prod.select_one('p:nth-child(9)').text
prod_info_main = prod_info+prod_info1
print(prod_info_main)

prod_process = prod.select_one('p:nth-child(11)').text
print(prod_process)

prod_material = prod.select_one('p:nth-child(13)').text
print(prod_material)

prod_application = prod.select_one('p:nth-child(15)').text
print(prod_application)

prod_feature = prod.select_one('p:nth-child(17)').text

p_l1 = prod.select('div.brand-right>ul>li')
prod_feature_list= ' '.join(map(str, p_l1)).replace('<li>','')
prod_feature_list = prod_feature_list.replace('</li>','. ')
prod_feature_main  = prod_feature + prod_feature_list
print(prod_feature_main)


csv_writer.writerow([prod_info_main,prod_process,prod_material,prod_application,prod_feature_main])


