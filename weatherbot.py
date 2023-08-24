import telebot
import requests
import json

bot = telebot.TeleBot('6646999433:AAGDzncpqe-h3vZBFoJONRdh0IT_F5IRsKw')
api = 'f4a8795027cd6ef2a3376afe27e3ac0d'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет!\nЭто бот для проверки погоды.</b>\n\n<b><i>Пожалуйста напиши название города.</i></b>')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city_name = message.text.strip()
    url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api}&units=metric')
    if url.status_code == 200:
        data = json.loads(url.text)
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        wind = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        bot.reply_to(message,
            f'<u><b>Погода в {city_name}</b></u>\n'
            f'<b>Температура:</b> {temp} <b>°C (Ощущается как</b> {feels_like} <b>°C)</b>\n'
            f'<b>Ветер:</b> {wind} <b>м/с</b>\n'
            f'<b>Давление:</b> {pressure} <b>мм.рт.ст</b>\n'
            f'<b>Влажность:</b> {humidity}<b>%</b>\n',
            parse_mode='html'
            )
    else:
        bot.reply_to(message, '<b>Город указан не верно!</b>')


bot.infinity_polling()
