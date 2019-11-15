import csv
from datetime import datetime
import itertools
from operator import itemgetter
import operator
import math

# the test output is not exactly matching.
# python built-in function round() has an exception: if both side of rounding is same, even is returned
# so I build a round function
def round_half_up(x):
    y = x*10%10
    if y>=5:
      return math.ceil(x)
    else:      
      return math.floor(x)
           
# load data from csv 
with open('../insight_testsuite/temp/input/Border_Crossing_Entry_Data.csv','r') as input:
        reader = csv.DictReader(input)
        data = list(reader)
        header = reader.fieldnames

        # # check the first line
        # print(data[0])

        # # check number of rows
        # print(len(data))

        # convert data types

        (lambda v: str(v))
        for line in data:
        #    line['Date'] = datetime.strptime(line['Date'],'%m/%d/%Y %I:%M:%S %p')
            line['Value'] = int(line['Value'])
            
        ### EAD ###
        # # check border
        # border = set()
        # for line in data:
        #     border.add(line['Border'])
        # print(border)

        # # check date range
        # date_range = [line['Date'] for line in data]
        # print(min(date_range))
        # print(max(date_range))

        ### calculate the total number ###
        
        # sort the data before itertools groupby
        data = sorted(data,key=itemgetter('Border','Measure','Date'))
        
        # calculate total
        result = []
        mygroup = itertools.groupby(data,itemgetter('Border','Measure','Date'))
        for key, group in mygroup:
            temp_dict = dict(zip(['Border','Measure','Date'],key))
            temp_dict['Value'] = sum(line['Value'] for line in group)
            result.append(temp_dict)


        ### calculate running monthly average
        newgroup = itertools.groupby(result,itemgetter('Border','Measure'))

        groups = []

        for key, group in newgroup:


          temp_result = list(group)
          temp_value_list = []
          temp_value_list = [item['Value'] for item in temp_result]

         # calculate cumulative total
          temp_value_list = list(itertools.accumulate(temp_value_list, operator.add))

          # calculate average
          for index, item in enumerate(list(temp_result)):
            if index == 0:
                item['Average'] = 0
                continue
            else:
                item['Average'] = round_half_up((temp_value_list[index]-item['Value'])/index)
          groups.append(temp_result);
        # print(groups)

        # flatten list
        final_list = [item for sublist in groups for item in sublist]
       # print(final_list)

        # sort by date, value, measure, border, descending
        final_list.sort(reverse=True,key=itemgetter('Date','Value','Measure','Border'))
       # print(final_list)

        # write into csv
        with open ('../insight_testsuite/temp/output/report.csv','w') as output:
            fieldnames = ['Border','Date','Measure','Value','Average']
            writer = csv.DictWriter(output, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(final_list)

