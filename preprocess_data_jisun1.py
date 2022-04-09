'''
버스 데이터 전처리 파일
'''

import pandas as pd


#이거 필요없을듯?
# bus_num =[100, 101, 102, 103, 104, 105, 106, 107, 109, 110, 110, 111, 120, 121, 130, 140, 141, 142, 143, 144, 145, 146, 147, 148, 150, 151, 152, 153, 160, 162, 171, 172, 173, 201, 202, 240, 241, 242, 260, 261, 262, 270, 271, 272, 273]

data_1 = pd.read_csv('./data/지선1,2,3,4_UTF8_(0305-0319)/지선1/노선·정류장 지표(노선별 차내 재차인원)_20220305.csv')
data_2 = pd.read_csv('./data/지선1,2,3,4_UTF8_(0305-0319)/지선1/노선·정류장 지표(노선별 차내 재차인원)_20220306.csv')
data_3 = pd.read_csv('./data/지선1,2,3,4_UTF8_(0305-0319)/지선1/노선·정류장 지표(노선별 차내 재차인원)_20220307.csv')
data_4 = pd.read_csv('./data/지선1,2,3,4_UTF8_(0305-0319)/지선1/노선·정류장 지표(노선별 차내 재차인원)_20220308.csv')
data_5 = pd.read_csv('./data/지선1,2,3,4_UTF8_(0305-0319)/지선1/노선·정류장 지표(노선별 차내 재차인원)_20220309.csv')
data_6 = pd.read_csv('./data/지선1,2,3,4_UTF8_(0305-0319)/지선1/노선·정류장 지표(노선별 차내 재차인원)_20220310.csv')
data_7 = pd.read_csv('./data/지선1,2,3,4_UTF8_(0305-0319)/지선1/노선·정류장 지표(노선별 차내 재차인원)_20220311.csv')
data_8 = pd.read_csv('./data/지선1,2,3,4_UTF8_(0305-0319)/지선1/노선·정류장 지표(노선별 차내 재차인원)_20220312.csv')
data_9 = pd.read_csv('./data/지선1,2,3,4_UTF8_(0305-0319)/지선1/노선·정류장 지표(노선별 차내 재차인원)_20220313.csv')
data_a = pd.read_csv('./data/지선1,2,3,4_UTF8_(0305-0319)/지선1/노선·정류장 지표(노선별 차내 재차인원)_20220314.csv')
data_b = pd.read_csv('./data/지선1,2,3,4_UTF8_(0305-0319)/지선1/노선·정류장 지표(노선별 차내 재차인원)_20220315.csv')
data_c = pd.read_csv('./data/지선1,2,3,4_UTF8_(0305-0319)/지선1/노선·정류장 지표(노선별 차내 재차인원)_20220316.csv')
data_d = pd.read_csv('./data/지선1,2,3,4_UTF8_(0305-0319)/지선1/노선·정류장 지표(노선별 차내 재차인원)_20220317.csv')
data_e = pd.read_csv('./data/지선1,2,3,4_UTF8_(0305-0319)/지선1/노선·정류장 지표(노선별 차내 재차인원)_20220318.csv')

#노선 번호 가져오기
bus_num = data_1[data_1.columns.tolist()[0]].unique()

date = '20220305'
last_date = str(int(date)+13)

def preprocess_data(data, n):

    #엑셀 맨뒤에 쉼표 있어서 이렇게 인식되는거 수정
    if('Unnamed: 28' in list(data.columns)):
        data = data.drop(['Unnamed: 28'], axis=1)

    data['노선']=data['노선'].astype(str)
    #버스번호 선택
    tmp_data = data[data['노선']==str(n)]
    
    cols = ['정류장순번','정류장명']

    #정류장 순번 + 정류장 명 합친 새로운 컬럼 생성
    tmp_data['정류장순번_정류장명'] =tmp_data[cols].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)

    #정류장순번 + 정류장 명으로 인덱스 설정
    tmp_data.set_index('정류장순번_정류장명', inplace=True)
    preprocessed_bus_df=tmp_data.drop(['기종점', '정류장명','노선','정류장순번'],axis=1)
    transposed_bus_df=preprocessed_bus_df.transpose()
    #데이터타입 int로 변경
    transposed_bus_df = transposed_bus_df.astype('int')

    return transposed_bus_df

for n in bus_num:
    prepro_data_1 = preprocess_data(data_1, n)
    prepro_data_2 = preprocess_data(data_2, n)
    prepro_data_3 = preprocess_data(data_3, n)
    prepro_data_4 = preprocess_data(data_4, n)
    prepro_data_5 = preprocess_data(data_5, n)
    prepro_data_6 = preprocess_data(data_6, n)
    prepro_data_7 = preprocess_data(data_7, n)
    prepro_data_8 = preprocess_data(data_8, n)
    prepro_data_9 = preprocess_data(data_9, n)
    prepro_data_a = preprocess_data(data_a, n)
    prepro_data_b = preprocess_data(data_b, n)
    prepro_data_c = preprocess_data(data_c, n)
    prepro_data_d = preprocess_data(data_d, n)
    prepro_data_e = preprocess_data(data_e, n)

    result_df = pd.concat([prepro_data_1, prepro_data_2])
    result_df = pd.concat([result_df, prepro_data_3])
    result_df = pd.concat([result_df, prepro_data_4])
    result_df = pd.concat([result_df, prepro_data_5])
    result_df = pd.concat([result_df, prepro_data_6])
    result_df = pd.concat([result_df, prepro_data_7])
    result_df = pd.concat([result_df, prepro_data_8])
    result_df = pd.concat([result_df, prepro_data_9])
    result_df = pd.concat([result_df, prepro_data_a])
    result_df = pd.concat([result_df, prepro_data_b])
    result_df = pd.concat([result_df, prepro_data_c])
    result_df = pd.concat([result_df, prepro_data_d])
    result_df = pd.concat([result_df, prepro_data_e])
    
    #임시 date 생성
    tmp_hour = pd.date_range("2022-03-05 04:00:00", periods=336, freq="H")
    result_df.index=pd.DatetimeIndex(tmp_hour)
    result_df.to_csv('{}.csv'.format(date+"_"+last_date+"_"+str(n)))
