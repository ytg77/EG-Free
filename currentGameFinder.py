
import keys
import requests
from pprint import pprint
# todo remove pprint

# url = "https://free-epic-games.p.rapidapi.com/free"

# headers = {
# 	"X-RapidAPI-Key": keys.rapidAPIKey,
# 	"X-RapidAPI-Host": "free-epic-games.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)
# resJSON = response.json()

# currentName = []
# currentImage = []
# for i in resJSON['freeGames']['current']:
#     currentName.append(i['title'])
#     currentImage.append(i['keyImages'][0]['url'])
# print(currentName)
# print(currentImage)

currentName = ['First', 'Second', 'Third']
currentImage = ['https://cdn-icons-png.flaticon.com/512/334/334043.png', 'https://cdn-icons-png.flaticon.com/512/1999/1999027.png', 'https://cdn-icons-png.flaticon.com/512/1999/1999040.png']
