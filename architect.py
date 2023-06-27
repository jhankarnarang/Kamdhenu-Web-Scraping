from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


source = requests.get('https://www.centuryply.com/plywood/architect-plywood')
soup = BeautifulSoup(source.content, 'lxml')
l=[]
t = []
s = []
main = soup.find('div',class_='product-description')
img1 = main.find('div',class_='tabcontent',id ='thumb1').span.img['src']
img2 = main.find('div',class_='tabcontent',id ='thumb2').span.img['src']
p_img1 = f'https://www.centuryply.com/{img1}'
p_img2 = f'https://www.centuryply.com/{img2}'
prod_img = f'{p_img1} , {p_img2}'
print(prod_img)

prod_name = main.find('div',class_='content').h1.text.strip()
print(prod_name)

prod_tags = main.find('div',class_='bytags').text.replace('\n','')
print(prod_tags)

prod_desc = main.find('div',class_='pr-content').br.previous_sibling.strip()
print(prod_desc)

prod_warranty = main.find('div',class_='pr-content').b.text
print(prod_warranty)

prod_size = soup.find('ul',class_='description_list inlinred').text.strip()
print(prod_size)


prod_info = soup.find('section',class_='block-usp nofaqpad')

for p_usp in prod_info.find_all('li'):
    prod_usp = p_usp.div.strong.text
    l.append(prod_usp)

prod_usps = ' , '.join(str(e) for e in l)
print(prod_usps)
    
#---------------------------------------------#
p_spec = soup.find('div',class_='faq-answer')
prod_spec = p_spec.p.text
print(prod_spec)

for p_specification in p_spec.find_all('li'):
    prod_specification = p_specification.h5.text
    t.append(prod_specification)

prod_spec_point = ' , '.join(str(e) for e in t)
print(prod_spec_point)

#-------TECHNICAL SPECIFICATION--------

p_tech = soup.find('div',class_='col-lg-6 leftsideoptions')
for prod_tech in p_tech.find_all('li'):
    prod_tech_spe = prod_tech.text.replace('\r\n','')
    prod_tech_spe = prod_tech_spe.replace('\n','')
    s.append(prod_tech_spe)

prod_tech_specification = ' , '.join(str(e) for e in s)
print(prod_tech_specification)
    
    

