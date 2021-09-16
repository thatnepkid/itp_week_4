# ITP Week 4 Day 2 Exercise
#Today we will pull information from the Pokemon api, put it into a dictionary, and then put that info into a new Excel file.  We will write the pseudocode as a group in class.  Be sure to follow the pseudocode, break your problems down into smaller pieces, and consult the documentation whenever you get stuck: https://pokeapi.co/api/v2/pokemon
#PSEUDO-CODE:
#GET NAME AND ABILITY FROM API
#PUT INFO IN DICTIONARY
#ADD THE DICTIONARY TO A NEW EXCEL WORKBOOK
#imports:
#json
#openpyxl
import json
import openpyxl
import requests
#Input
    #json file from pokemon api
    #workbook
#Assign response to variable
#pokemon_api = requests.get("https://pokeapi.co/api/v2/pokemon")
#print(pokemon_api)
#Create workbook
    #get workbook from openpy
    #load workbook
    #assign workbook to variable
wb = openpyxl.load_workbook("C:\\Users\\GorkhaliSquad\\Documents\\VetsInTech\\itp_week_4\\day_2\\output.xlsx")
#print(type(wb))
#Create Worksheet
    #assign sheet to variable
sheet = wb["Sheet1"]
#Create a dictionary, assign to variable
# pokemon = {
#     bulbasour : {
#         "name": "pokemon_name",
#         "abilities": ["ability1", "ability2"]
#     },
#     pikachu : {
#         "name": "pokemon_name",
#         "abilities": ["ability1", "ability2"]
#     }
# }
#print(pokemon)
#forms name
#FUNCTION BODY
    #Convert response to json file
        #clean data(response)
            #json.loads(response.text)
# def get_data():
#     clean_data = json.loads(pokemon_api.text)
#     result = clean_data["results"]
# #print(result)
#     return result
def get_data(url):
    pokemon_api = requests.get(url)
    clean_data = json.loads(pokemon_api)
    result = clean_data["results"]
#print(result)
    return result
#pokemon_name = result[0]["name"]
#print(pokemon_name)
#Iterate over response
    #for each pokemon in response
       #variable key = pokemon.name
            #variable value = pokemon.abilites
            #append {key/value} pair to dictionary
pokemon_data = get_data("https://pokeapi.co/api/v2/pokemon")
row = 1
#print(pokemon_data)
for item in pokemon_data:
    sheet['A' + str(row)] = item['name']
    row+=1
    #pname = item["name"]
    #print(pname)
wb.save("C:\\Users\\GorkhaliSquad\\Documents\\VetsInTech\\itp_week_4\\day_2\\output.xlsx")
    #Iterate over dictionary
        #for each item in dictionary
            #assign dictionary values to rows & cols
                #Write Name to Cell
                #Write Abilities to Cell
#Output
    #Workbook