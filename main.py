import csv
import pandas as pd

data = pd.read_csv('https://www1.nseindia.com/products/content/all_daily_reports.htm')

with open("/Users/murek/Downloads/cm09MAR2022bhav.csv") as fp:
        for line in csv.DictReader(fp):
            #print(line)
            if line['OPEN'] == line['HIGH']:
              print(line['SYMBOL']
