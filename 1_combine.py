import pandas as pd
import os
from pathlib import Path


# returns csv name according to the sheet name eg: detail.csv
def get_csv_with_sheet_name(sheet_name):
    if 'Detail_67_' in sheet_name:
        return 'detail.csv'
    elif 'DetailVol_67_' in sheet_name:
        return 'detailVol.csv'
    else:
        return 'detailTemp.csv'


# creates a csv file if not exists else appends in the existing file
def create_csv(data, csv_name):
    file_path = Path(csv_name)
    if file_path.exists():
        data.to_csv(os.getcwd() + '/csv/' + csv_name, mode='a', header=False)
    else:
        data.to_csv(os.getcwd() + '/csv/' + csv_name, header=True)


# read excel file
def read_excel(file_name):
    xls = pd.ExcelFile(os.getcwd() + "/Data/" + file_name)
    for sheet in xls.sheet_names:
        csv_name = get_csv_with_sheet_name(sheet)
        data = pd.read_excel(xls, sheet_name=sheet)
        create_csv(data, csv_name)


read_excel('data.xlsx')
read_excel('data_1.xlsx')
