import requests
import random
import telebot

from bs4 import BeautifulSoup as b

URL = 'https://miass.live/'
API_KEY = '5928949696:AAHjVy_l5MBtb4QFAU38_-XeMpqJ2XkIwpw'
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    news = soup.find_all('div', class_='title')
    return[c.text for c in news]

list_of_title = parser(URL)
random.shuffle(list_of_title)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['начать'])

def hello(message):
    bot.send_message(message.chat.id, 'Привет! Введите любую цифру: ')

@bot.message_handler(content_types=['text'])
def news(message):
    if message.text.lower()in '123456789':
        bot.send_message(message.chat.id, list_of_title[0])
        del list_of_title[0]
    else:
        bot.send_message(message.chat.id, 'Введите любую цифру: ')
bot.polling()
