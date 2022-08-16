import os

def omitted_data(dataset, year):
    month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    day_28 = ['%02d' %i for i in range(1,29)]
    day_29 = ['%02d' %i for i in range(1,30)]
    day_30 = ['%02d' %i for i in range(1,31)]
    day_31 = ['%02d' %i for i in range(1,32)]
    dataset_path = f'/{dataset}/{year}' #
    day_list = []
    file_list = []
    for month in month:
            if month in ['01', '03', '05', '07', '08', '10', '12'] : day = day_31
            elif (month == '02') & (int(year)%4 == 0) : day = day_29
            elif (month == '02') & (int(year)%4 != 0) : day = day_28
            else: day = day_30
            for d in day:
                day_list.append(month+d)
    for file in os.listdir(dataset_path):
        file_list.append(file)

    for i in range(len(day_list)-1):
        if day_list[i] in file_list[i]: pass
        else: file_list.insert(i, f'{year}{day_list[i]} not exist')
    
    omitted_list = [i for i in file_list if 'not exist' in i]
    cnt = len(omitted_list)
    return omitted_list, cnt

dataset_name_list = ['AVHRR_OI_SST/v2.1', 'CMC/deg0.1', 'DMI_SST', 'GAMSSA_GDS2', 'MUR_SST', 'MW_IR_SST', 'MW_OI_SST', 'NAVO_K10_SST_GDS2', 'OSPO_SST', 'OSPO_SST_Night', 'OSTIA_SST']
dataset = 'DMI_SST'


# year option을 for문으로 추가
for year in os.listdir(dataset):
    omit_list = omitted_data(dataset, year)
    print(f'{year} 누락 일 수 : {omit_list[1]}')
    print(f'{omit_list[0]}')



## TODO 시작일, 종료일이 1월 1일, 12월 31일이 아닐 경우에 대해서 고려