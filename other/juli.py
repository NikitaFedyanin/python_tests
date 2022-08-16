import requests
import json

user = 'kbeckmann'  # olderzeus
repo = 'game-and-watch-retro-go'
link = 'https://api.github.com/repos/{}/{}/forks?per_page=100'.format(user, repo)

request = requests.get(link)
if request:
    lst = json.loads(request.content)
    full_name_list = [i["full_name"] for i in lst]
    print('\n'.join(full_name_list))
