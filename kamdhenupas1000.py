from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

csv_file = open('colourmaxcoatedsheets.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Prod_info','Prod_tech'])

source = requests.get('https://www.kamdhenulimited.com/colourmax-color-coated-sheets.php')
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

prod2 = prod1.find_next('p').text.replace('\n\n\n','')
prod2 = prod2.replace('\n\n','')
prod2 = prod2.replace('\n','')
print(prod2)

prod_tech1 = prod_tech+prod2

csv_writer.writerow([prod_info,prod_tech1])

