import pandas as pd
import csv 


from urllib.request import Request, urlopen

req = Request('https://www.kamdhenulimited.com/kamdhenu-circular-hollow.php', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req,timeout=10).read()


# csv_file = open('PAS1000chemicalprop.csv','w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Chemical_prop','Physical_prop'])

# Webpage url                                                                                                               
#url = ('https://www.kamdhenulimited.com/kamdhenu-pas-chemical-properties.php')

# Extract tables
pd.set_option('max_colwidth', 400) 
dfs = pd.read_html(webpage)


# Get first table 
 
pd.set_option('max_colwidth', 400)                                                                                                        
df = dfs[0]
# df1 = dfs[1]
# df2 = dfs[2]


print(df)
# print(df1)
# #print(df2)
# print(df2)

df.to_csv('Tensileproperties.csv')
# df1.to_csv('Pre-Painted Alu-Zinc Steel Sheets (Galvalume*).csv')
# df2.to_csv('Total Coating Thickness (TCT).csv')

# csv_writer.writerow([df,df1])

# Extract columns                                                                                                           
# df2 = df[['Test Prescribed in IS: 2202 (Part-I), 1999','Minimum Value for Conformity','Observed Value']]
# print(df2)