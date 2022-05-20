import pandas as pd
from regional_destinations import reg_des

parquet_file = r"D:\Стажировка Пулково\клики по 48 странам\clicks_par.parquet"
data = pd.read_parquet(parquet_file, engine='auto', columns=['origin', 'destination','destination_country1'])

data1 = data[(data['origin'] == 'LED')] #выбираем маршруты из СПБ

writer = pd.ExcelWriter('название_файла.xlsx')
for b in reg_des:
    data2 = data1[(data1['destination'] == b)] #выбираем данные по аэропорту
    data2.to_excel(writer, b) #записываем данные в эксель, где каждый лист назван кодом аэропорта
    writer.save()




