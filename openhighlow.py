import csv
import pandas as pd

#data = pd.read_csv('https://www1.nseindia.com/products/content/all_daily_reports.htm')
BUY = []
SELL = []

with open("/Users/murek/Downloads/cm09MAR2022bhav.csv") as fp:
        for line in csv.DictReader(fp):
            #print(line)
            if line['OPEN'] == line['HIGH']:
              BUY.append(line['SYMBOL'])
              #print('Trigger BUY',line['SYMBOL'])
            elif line['OPEN'] == line['LOW']:
              #print('Trigger SELL',line['SYMBOL'])
              SELL.append(line['SYMBOL'])

print("buy the following stocks",BUY)
print("sell the following stocks",SELL)
