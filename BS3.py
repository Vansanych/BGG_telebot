import requests
from bs4 import BeautifulSoup as BS
from datetime import datetime

message = 'wingspan'
start = datetime.now()

req = requests.get('https://boardgamegeek.com/geeksearch.php?action=search&q='
                   + message + '&objecttype=boardgame')
start2 = datetime.now()
tree = BS(req.text, 'html.parser')
print(start2 - start)

tags = tree.find_all('a', attrs={'name': True})
for tag in tags:
    name = tag.find_next(class_='primary')
    print(name.text + ':', tag['name'])

end = datetime.now()
print(end - start)
