import pandas as pd
from openpyxl import load_workbook
import os
def do_actual_work():
    df = pd.read_html('Report from Static analyzer tool.html')
    shared_df = df[0][df[0]['Usage'] == 'shared']
    shared_df = shared_df[['Variables','Tasks (Write)','Tasks (Read)','Detailed Type','Nb Read','Nb Write']]
    shared_df.rename(columns={"Tasks (Write)": "W.T","Tasks (Read)": "R.T",},inplace=True)
    shared_df.to_excel('data.xlsx',index=False)
    workbook = load_workbook('data.xlsx')
    sheet = workbook.active
    length = len(sheet['A'])
    for i in range(2, length+1):
        ch = 'A' + str(i)
        sheet[ch] = sheet[ch].value.split('.')[-1]
    return os.path.dirname(os.path.realpath('data.xlsx'))+"/data.xlsx"
   
do_actual_work()