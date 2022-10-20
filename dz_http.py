import requests

request = requests.get('https://akabab.github.io/superhero-api/api/all.json')
j = request.json()
heroes_list = ['Hulk', 'Captain America', 'Thanos']
for i in j:
    heroes_name = i['name']
    if heroes_name in heroes_list:      
        name, intelligence = (heroes_name,i['powerstats']['intelligence'])      
print(f"Самый умный : {name}, интеллект : {intelligence}")

  






