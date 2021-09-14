# ITP Week 4 Day 1 Exercise

# https://data.messari.io/api/v2/assets



import requests
import json
import openpyxl


data = requests.get('https://data.messari.io/api/v2/assets')
beautify = json.loads(data.text)

symbol = beautify['data']

roi = beautify['data'][0]['metrics']['roi_data']['percent_change_last_1_week'] 

# print(roi)
# print(symbol)

sym_counter = 0

for index in range(20):
    symbol_list = beautify['data'][sym_counter]['symbol']
    sym_counter += 1
    print(symbol_list)

roi_counter = 0
for item in range(20):
    roi_list = beautify['data'][roi_counter]['metrics']['roi_data']['percent_change_last_1_week'] 
    roi_counter += 1
    print(roi_list)





