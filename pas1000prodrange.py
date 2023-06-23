from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

csv_file = open('KamdhenuPAS1000prodrange.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Prod_info','Prod_tech'])

source = requests.get('https://www.kamdhenulimited.com/kamdhenu-pas-product-range.php')
soup = BeautifulSoup(source.content, 'lxml')

prod = soup.select_one('body>div>div>div>div.brand-right')
# prod_name = prod.h1.text
# print(prod_name)
prod_info = prod.select_one('p').text
prod_info = prod_info.replace('\n',' ')
print(prod_info)

prod1 = prod.p.find_next('p')
prod_tech = prod1.text
prod_tech = prod_tech.replace('\n',' ')
print(prod_tech)

csv_writer.writerow([prod_info,prod_tech])
