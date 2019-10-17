import csv
import math
import sys

if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python3.7 ./src/border_analytics.py ./input/Border_Crossing_Entry_data.csv ./output/report.csv")
    sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

final_dict = {}
date_list = []

#Loading data as a nested dictionary in the format (Border, Measure):Date:Value
with open(input_file, 'r') as file:
    data = csv.reader(file, delimiter=',')
    next(data)
    for row in data:   
        border = row[3]
        measure = row[5]
        date = row[4]
        value = row[6]
     
        final_dict.setdefault((border,measure),{}).setdefault(int(date.split('/')[0])+int(date.split('/')[2][:4])*12,[]).append(int(value))
        if(date not in date_list):
            date_list.append(date)

#Calculating the sum of values for each month
for border, date in final_dict.items():
    for month in date:
        date[month] = sum(date[month])
      
      
#Calculating running monthly average of total number of crossings for that type of crossing and border.     
average_dict = {}
for types,date in final_dict.items():
	temp = 0
 	keyList = sorted(date.keys())
	for i,v in enumerate(keyList):
        temp = 0
        tot_month = 0
        for j in range(0,i):
            temp += date[v-(j+1)]
            tot_month += 1
        if tot_month != 0:
            temp = math.ceil(temp/tot_month)
        average_dict[date[v]] = temp

#Sorting the datelist    
date_list.sort(reverse=True)   

#Creating a list from the final_dict dictionary
final_dict_copy = final_dict
temp_list=[]
for k, v in final_dict_copy.items():
    if len(v.keys()) > 1:
        for _k, _v in v.items():
            temp_list.append([k[0],k[1],_k,_v])
    else:
        temp_list.append([k[0],k[1],list(v.keys())[0],list(v.values())[0]])

temp_list.sort(key=lambda x:x[2],reverse=True) 

#Converting average_dict to a list
dictlist = []
for key, value in average_dict.items():
    temp = [key,value]
    dictlist.append(temp)
dictlist.sort()

#Appending calculated running average to the respective values
avg_list = []
for i in range(0,len(temp_list)):
    for j in range(0,len(dictlist)):
        if dictlist[j][0] == temp_list[i][3]:
            avg_list.append(dictlist[j][1])

#Creating the final output list
ans_list = []
j = 0
for i in range(0,len(temp_list)):
    if(temp_list[i][2] == int(date_list[j].split('/')[0])+int(date_list[j].split('/')[2][:4])*12):
        ans_list.append([temp_list[i][0], date_list[j], temp_list[i][1], temp_list[i][3], avg_list[i]])
    elif(j + 1 < len(date_list)):
        j += 1
        ans_list.append([temp_list[i][0], date_list[j], temp_list[i][1], temp_list[i][3], avg_list[i]])

#Sorting the list as required
ans_list.sort(key=lambda x:[x[1],x[3],x[2],x[0]],reverse=True)

#Writing results to the report.csv file
with open(output_file,'w') as resultFile:
    wr = csv.writer(resultFile)
    wr.writerow(['Border','Date','Measure','Value','Average'])
    for row in ans_list:
    	wr.writerow(row)




