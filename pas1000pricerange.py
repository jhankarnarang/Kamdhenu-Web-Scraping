from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

csv_file = open('PAS1000pricerange.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Prod_price_list'])

source = requests.get('https://www.kamdhenulimited.com/kamdhenu-rcp-pas10000.php')
soup = BeautifulSoup(source.content, 'lxml')

prod = soup.select_one('body>div>div>div>div.brand-right')
img = prod.find('div',class_='rcp-img')
prod_img = img.img['src']
prod_img = f'https://www.kamdhenulimited.com/{prod_img}'
print(prod_img)

csv_writer.writerow([prod_img])