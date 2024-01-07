import telebot

from config import TOKEN
from extensions import API, ConventionEx, keys

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    bot.send_message(message.chat.id, f"Приветсвую {message.chat.username}! \n\nЧтобы начать работу введите команду для бота следующим образом: \n<имя валюты, цену которой он хочет узнать> \n <имя валюты, в которой надо узнать цену первой валюты> \n <количество первой валюты> ")


@bot.message_handler(commands=['value'])
def handle_value(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message,text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')

    try:
        if len(values) != 3:
            bot.send_message(message.chat.id, "Укажите три параметра")
            raise ConventionEx('Много параметров')

        quote, base, amoute = message.text.split(' ')
        amoute = float(amoute)

        if amoute < 0.0:
            raise ConventionEx("Перевод не возможно осуществить")

        if quote == base:
            bot.send_message(message.chat.id, 'Невозможно перевести одну и ту же валюту')
            raise ConventionEx("Невозможно перевести одну и ту же валюту")

        text_message = API.get_price(quote, base, amoute)
        bot.send_message(message.chat.id, text_message)

    except KeyError:
        bot.send_message(message.chat.id, "Валюта или Цифра не соответсвует требованиям. \n Введите вверные данные")

bot.polling(none_stop=True)