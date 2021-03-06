# Import module
#  csv -- fileIO operation
import csv
# collections -- for OrderedDict
import collections

# Read cwb weather data
cwb_filename = '108061233.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)

# Retrive all data points which station id are "C0A880", "C0F9A0", "C0G640", "C0R190", "C0X260" as a list.
target_data = list(filter(lambda item: item['station_id'] == 'C0A880' or item['station_id'] == 'C0F9A0' or 
                                 item['station_id'] == 'C0G640' or item['station_id'] == 'C0R190' or item['station_id'] == 'C0X260', data))

#record the order we have done
index_0 = 0
index_1 = 0
index_2 = 0
index_3 = 0
index_4 = 0

# find the data and the maximum and minimum of the data
for i in target_data:
   # for data 'C0A880'
   if (i['station_id'] == 'C0A880'):
      # remove '-99.000' and '-999.000' data
      if (i['WDSD'] != '-99.000' and i['WDSD'] != '-999.000'):
         # the first data we retrive
         if (index_0 == 0):
            max_0 = float(i['WDSD'])
            min_0 = float(i['WDSD'])
         # temp for temporarily store the data
         else:
            temp = float(i['WDSD'])
            # if temp is larger than max, then change the max number with temp number
            if (temp > max_0):
               max_0 = temp
            # if temp is smaller than min, then change the min number with temp number   
            elif(temp < min_0):
               min_0 = temp
         # the order increases      
         index_0+=1
   # for data 'C0F9A0' 
   elif (i['station_id'] == 'C0F9A0'):
      if (i['WDSD'] != '-99.000' and i['WDSD'] != '-999.000'):
         if (index_1 == 0):
            max_1 = float(i['WDSD'])
            min_1 = float(i['WDSD'])
         else:
            temp = float(i['WDSD'])
            if (temp > max_1):
               max_1 = temp
            elif(temp < min_1):
               min_1 = temp
         index_1+=1
   # for data 'C0G640'      
   elif (i['station_id'] == 'C0G640'):
      if (i['WDSD'] != '-99.000' and i['WDSD'] != '-999.000'):
         if (index_2 == 0):
            max_2 = float(i['WDSD'])
            min_2 = float(i['WDSD'])
         else:
            temp = float(i['WDSD'])
            if (temp > max_2):
               max_2 = temp
            elif(temp < min_2):
               min_2 = temp
         index_2+=1
   # for data 'C0R190'     
   elif (i['station_id'] == 'C0R190'):
      if (i['WDSD'] != '-99.000' and i['WDSD'] != '-999.000'):
         if (index_3 == 0):
            max_3 = float(i['WDSD'])
            min_3 = float(i['WDSD'])
         else:
            temp = float(i['WDSD'])
            if (temp > max_3):
               max_3 = temp
            elif(temp < min_3):
               min_3 = temp
         index_3+=1
   # for data 'C0X260'      
   elif (i['station_id'] == 'C0X260'):
      if (i['WDSD'] != '-99.000' and i['WDSD'] != '-999.000'):
         if (index_4 == 0):
            max_4 = float(i['WDSD'])
            min_4 = float(i['WDSD'])
         else:
            temp = float(i['WDSD'])
            if (temp > max_4):
               max_4 = temp
            elif(temp < min_4):
               min_4 = temp
         index_4+=1

# if we just find 0 or 1 data, then print none, otherwise we print the maximun range
# result_0 for 'C0A880'
if (index_0 == 0 or index_0 == 1):
   result_0 = 'None'
else:
   result_0 = str(max_0 - min_0)
# result_1 for 'C0F9A0'
if (index_1 == 0 or index_1 == 1):
   result_1 = 'None'
else:
   result_1 = str(max_1 - min_1)
# result_2 for 'C0G640'
if (index_2 == 0 or index_2 == 1):
   result_2 = 'None'
else:
   result_2 = str(max_2 - min_2)
# result_3 for 'C0R190'
if (index_3 == 0 or index_3 == 1):
   result_3 = 'None'
else:
   result_3 = str(max_3 - min_3)
# result_4 for 'C0X260'
if (index_4 == 0 or index_4 == 1):
   result_4 = 'None'
else:
   result_4 = str(max_4 - min_4)

# Print result with OrderedDict
output = collections.OrderedDict()
output['C0A880'] = result_0
output['C0F9A0'] = result_1
output['C0G640'] = result_2
output['C0R190'] = result_3
output['C0X260'] = result_4
print(output)
