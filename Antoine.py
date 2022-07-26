# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

chem = ['water','methane','ethane','propane',
        'methanol','ethanol','propanol']

site = 'https://webbook.nist.gov/cgi/cbook.cgi?Name={0}&Mask=4'



def get_html_table(page):
    html = BeautifulSoup(page, 'lxml')
    table = html.find('table',attrs={"aria-label": "Antoine Equation Parameters"})
    tableRows = table.find_all('tr')
    tableInfo = []
    try:
        tableHeader = table.find_all('th')
        row = [i.text for i in tableHeader]
        tableInfo.append(row)
    except:
        pass
    for tr in tableRows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        if len(row)>0:
            tableInfo.append(row)
    return(tableInfo)

with open('output.txt','w+') as output:
    for chemical in chem:
        active_page = requests.get(site.format(chemical)).text
        table = get_html_table(active_page)
        antoine = pd.DataFrame(table[1:][1:],columns=table[:][0])
        writer = pd.ExcelWriter(f'../data/{chemical}.xlsx', engine='xlsxwriter')
        antoine.to_excel(writer,sheet_name = 'antoine', index=False)
        writer.save() 
        
        