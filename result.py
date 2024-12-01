import pandas
get_info=input()  

fails = pandas.read_excel('C:/Users/julij/Downloads/dip225-2-practical-task-julija-koniseva-main/dip225-2-practical-task-julija-koniseva-main/description.xlsx', sheet_name="LookupAREA") 
info_list = fails.values.tolist()

get_info=input()

info_list[1][0]
reg_ID=0
for row in info_list: 
    if row[1]==get_info: 
        reg_ID=row[0] 
        break 
reg_ID
if reg_ID==0:
    print(0)
    exit()

CleanData=[]
csv=open('C:/Users/julij/Downloads/dip225-2-practical-task-julija-koniseva-main/dip225-2-practical-task-julija-koniseva-main/data.csv', 'r')
for line in csv:
    CleanData.append(line.rstrip().split(','))

geo_count=[]
for line in CleanData:
    if line [1]==reg_ID:
        geo_count.append(int(line[3])) 

print(sum(geo_count))
