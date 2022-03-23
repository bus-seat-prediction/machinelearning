'''
버스 데이터 전처리 파일
'''

import pandas as pd

# 일단 2021년 데이터로만 해볼 예정
bus_2021_df = pd.read_csv('./data/2021_bus.csv')

print(bus_2021_df.dtypes)