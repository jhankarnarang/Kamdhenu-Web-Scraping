from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


def scrape(sections, file_names):
    for i in range(len(sections)):
        with open(file_names[i], 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Links','name', 'img','Feature'])

            print(f'> {sections[i]}')
            
            
            url = f'{sections[i]}'
            source = requests.get(url)
            soup = BeautifulSoup(source.content, 'lxml')

            img = soup.find('div',class_='wpb_column vc_column_container vc_col-sm-4 mpc-column')
            prod_img = img.figure.div.img['src']
            print(prod_img)

            p_info = soup.find('div',class_='wpb_column vc_column_container vc_col-sm-8 mpc-column')
            prod_name = p_info.h2.text
            print(prod_name)
            p_feature = p_info.ul.text.replace('\n\n\n\n\n','')
            print(p_feature)
            
            try:
                dfs = pd.read_html(url)                                                                                                         
                df = dfs[0]
                print(df)
                df.to_csv(f'{table_names[i]}')
                
            except:
                print('')
            csv_writer.writerow([sections[i],prod_name,prod_img,p_feature])



            

if __name__ == '__main__':

    '''
    usage:
    -> install requirements
    -> verify:
        - all site sections are listed in `sections`
        - all sites have a corresponding csv file `file_names`
        - all paths to the csv file are correct
    -> run
    '''

    sections = [
        'https://swadeshplywoods.com/swadesh-platinum-plywood/',
        'https://swadeshplywoods.com/swadesh-gold-bwp-grade-plywood/',
        'https://swadeshplywoods.com/swadesh-mr-grade-plywood/',
        'https://swadeshplywoods.com/swadesh-block-board/',
        'https://swadeshplywoods.com/swadesh-flush-doors/',
        'https://swadeshplywoods.com/swadesh-flexi-plywood/',
        'https://swadeshplywoods.com/swadesh-membrane-doors/',
        'https://swadeshplywoods.com/swadesh-densified-film-face-plywood/',
        'https://swadeshplywoods.com/sonnet-platinum-plywood/',
        'https://swadeshplywoods.com/sonnet-mr-grade-plywood/',
        'https://swadeshplywoods.com/sonnet-bwp-grade-plywood/',
        'https://swadeshplywoods.com/sonnet-block-board/',
        'https://swadeshplywoods.com/sonnet-flush-doors/',
        'https://swadeshplywoods.com/sonnet-flexi-plywood/'
           ]

    file_names = [
        './data/swadesh/platinum-plywoods.csv',
        './data/swadesh/gold-bwp-grade-plywood.csv',
        './data/swadesh/mr-grade-plywood.csv',
        './data/swadesh/block-board.csv',
        './data/swadesh/flush-doors.csv',
        './data/swadesh/flexi-plywoods.csv',
        './data/swadesh/membrane-doors.csv',
        './data/swadesh/densified-film-face-plywoods.csv',
        './data/sonnet/platinum-plywoods.csv',
        './data/sonnet/mr-grade-plywood.csv',
        './data/sonnet/bwp-grade-plywood.csv',
        './data/sonnet/block-board.csv',
        './data/sonnet/flush_doors.csv',
        './data/sonnet/flexi_plywood.csv',
    ]

    table_names = [
        './data/swadesh/platinum_plywoods-table.csv',
        './data/swadesh/gold-bwp-grade-plywood-table.csv',
        './data/swadesh/mr-grade-plywood-table.csv',
        './data/swadesh/block-board-table.csv',
        './data/swadesh/flush-doors-table.csv',
        './data/swadesh/flexi-plywoods-table.csv',
        './data/swadesh/membrane-doors-table.csv',
        './data/swadesh/densified-film-face-plywoods-table.csv',
        './data/sonnet/platinum-plywoods-table.csv',
        './data/sonnet/mr-grade-plywood-table.csv',
        './data/sonnet/bwp-grade-plywood-table.csv',
        './data/sonnet/block-board-table.csv',
        './data/sonnet/flush_doors-table.csv',
        './data/sonnet/flexi_plywood-table.csv',
    ]

    scrape(sections, file_names)