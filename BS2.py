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
# print(tree)


tags = tree.find_all('a', attrs={'name': True})
# print('tags', tags)
for tag in tags:
    print(tag)

tags67 = tree.find('a', attrs={'name': True})
print('76', tags67)


def has_name(tag):
    return tag.has_attr('name')


tags = tree.find_all(has_name)
# print(tags)
# tags_draft = tree.find_all(name=None, attrs={'name': 16})
# print(tags_draft)

ranks = []
for tag in tags:
    try:
        rank = tag['name']
        ranks.append(rank)
    except:
        pass

tags2 = tree.find_all(class_='primary')
names = []
for tag2 in tags2:
    name = tag2.text
    names.append(name)

for i in range(len(ranks)):
    try:
        if int(ranks[i]) < 3000:
            post = names[i] + ': ' + ranks[i]
            print(post)
    except:
        pass

end = datetime.now()
print(end - start)
