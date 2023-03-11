import requests
from bs4 import BeautifulSoup as BS
import telebot

bot = telebot.TeleBot("5043606399:AAEQjRbRlYmEpvXPhzLQu1I7_3M1eJ6-s8w", parse_mode=None)


@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, "идет обработка запроса")

    req = requests.get('https://boardgamegeek.com/geeksearch.php?action=search&q='
                   + message.text + '&objecttype=boardgame')
    tree = BS(req.text, 'html.parser')

    tags = tree.find_all('a')
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
        if int(ranks[i]) < 3000:
            post = names[i] + ': ' + ranks[i]
            bot.send_message(message.chat.id, post)
    bot.send_message(message.chat.id, "конец")


bot.polling(none_stop=True)
