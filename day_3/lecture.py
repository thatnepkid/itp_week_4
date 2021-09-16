# ITP Week 4 Day 3 Lecture

import openpyxl
import requests
import json


response = requests.get("https://pokeapi.co/api/v2/pokemon")
json_data = json.loads(response.text)
first_pokemon = json_data['results'][0]
# print(first_pokemon['name'])
all_pokemon =json_data['results']


# abilities_response = requests.get(first_pokemon['url'])
# abilities_json_data = json.loads(abilities_response.text)
# just_abilities_of_firstpokemon = abilities_json_data['abilities']
# print(just_abilities_of_firstpokemon)


# abilitystring = ""
# for eachability in just_abilities_of_firstpokemon:
#     abilitystring += eachability['ability']['name']+" "

# print(abilitystring)


wb = openpyxl.Workbook()
sheet = wb.active

row_num = 1
for each_pokemon in all_pokemon:
    abil_resp = requests.get(each_pokemon['url'])
    abil_jsondata = json.loads(abil_resp.text)
    just_abillist = abil_jsondata['abilities']
    abil_string = ""
    for each_abil in just_abillist:
        abil_string += each_abil['ability']['name']+" "
    sheet['A' + str(row_num)] = each_pokemon['name']
    sheet["B" + str(row_num)] = abil_string
    row_num += 1




# sheet['A1'] = first_pokemon['name']
# sheet['B1'] = abilitystring

wb.save("C:\\Users\\GorkhaliSquad\\Documents\\VetsInTech\\itp_week_4\\day_3\\output.xlsx")