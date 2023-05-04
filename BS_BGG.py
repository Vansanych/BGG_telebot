import requests
from bs4 import BeautifulSoup as BS
import telebot

bot = telebot.TeleBot("5043606399:AAEQjRbRlYmEpvXPhzLQu1I7_3M1eJ6-s8w", parse_mode=None)


@bot.message_handler(content_types=['text'])
def send_echo(message):
    req = requests.get('https://boardgamegeek.com/geeksearch.php?action=search&q='
                   + message.text + '&objecttype=boardgame')
    tree = BS(req.text, 'html.parser')

    tags = tree.find_all('a', attrs={'name': True})
    for tag in tags:
        name = tag.find_next(class_='primary')
        post = name.text + ': ' + tag['name']
        bot.send_message(message.chat.id, post)


bot.polling(none_stop=True)
