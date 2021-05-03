import pandas as pd


def down_sample(file_name):
    df = pd.read_csv('/csv/'+file_name, parse_dates=['Realtime'])
    new_file_name = file_name.split('.')[0] + 'Downsampled.csv'
    df.resample('1min').to_csv(new_file_name)


down_sample('detail.csv')
down_sample('detailVol.csv')
down_sample('detailTemp.csv')