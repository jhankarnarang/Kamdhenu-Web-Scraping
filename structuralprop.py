from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from sympy import S

csv_file = open('StructuralSteelProperties.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['chem_comp','Mech_Prop','Dimensional_tolerance'])

source = requests.get('https://www.kamdhenulimited.com/structural-steel-properties.php')
soup = BeautifulSoup(source.content, 'lxml')

prod = soup.select_one('body>div>div>div>div.brand-right')

st_chem = prod.p.span.next_sibling
st_chem1 = st_chem.next_sibling.replace('\n','')
print(st_chem1)


st_mech = soup.select_one('p:nth-child(6)').span.next_sibling
st_mech1 = st_mech.next_sibling.replace('\n','')
print(st_mech1)

st_dimensional  = st_mech = soup.select_one('p:nth-child(8)').span.next_sibling
st_dime = st_dimensional.next_sibling.replace('\n','')
print(st_dime)

csv_writer.writerow([st_chem1,st_mech1,st_dime])