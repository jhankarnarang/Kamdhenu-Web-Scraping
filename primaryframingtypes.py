from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

csv_file = open('primaryframingtype.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Image'])

l=[]
source = requests.get('https://www.kamdhenulimited.com/Primary-framing-types.php')
soup = BeautifulSoup(source.content, 'lxml')
prod = soup.select_one('body>div>div>div>div.brand-right')

for img in prod.find_all('img'):
    p_img = img['src']
    prod_img = f'https://www.kamdhenulimited.com/{p_img}'
    l.append(prod_img)




prod_info2 = ' , '.join(str(e) for e in l)
print(prod_info2)

csv_writer.writerow([prod_info2])


