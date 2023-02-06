import os
import re
from datetime import datetime, timedelta

def omitted_data(dataset):
    dataset_path = f'F:\\{dataset}\\'
    years = ['%s' %year for year in os.listdir(dataset_path)]
    omitted_list = []
        
    for year in years:
        file_list = []
        for file in os.listdir(f'{dataset_path}\\{year}'):
            file_list.append(file)
        start_date_fn = file_list[0]
        end_date_fn = file_list[-1]
        match_s = re.search(r'\d{4}\d{2}\d{2}', start_date_fn)
        match_e= re.search(r'\d{4}\d{2}\d{2}', end_date_fn)
        start_date = datetime.strptime(match_s.group(), '%Y%m%d').date()
        end_date = datetime.strptime(match_e.group(), '%Y%m%d').date()
        date_range = [(start_date + timedelta(days=i)).strftime("%Y%m%d") for i in range((end_date - start_date).days+1)]

        for i in range(len(date_range)):
            j_day = datetime.strptime(date_range[i], '%Y%m%d')
            j_day = j_day.strftime('%j')
            if date_range[i] in file_list[i]: pass
            else: file_list.insert(i, f'{date_range[i]}, {j_day} not exists.')
        omitted_list += [i for i in file_list if 'not exists' in i]
    cnt = len(omitted_list)

    return omitted_list, cnt

dataset_name = ['AVHRR_OI_SST/v2.1', 'CMC/deg0.1', 'DMI_SST', 'GAMSSA_GDS2', 'MUR_SST', 'MW_IR_SST', 'MW_OI_SST', 'NAVO_K10_SST_GDS2', 'OSPO_SST', 'OSPO_SST_Night', 'OSTIA_SST']

for dataset in dataset_name:
    result = omitted_data(dataset)
    print(f'\n[{dataset}] 누락일 : {result[1]}')
    for day in result[0]:
        print(day)
