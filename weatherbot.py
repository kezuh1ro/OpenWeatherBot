import telebot
import requests
import json

bot = telebot.TeleBot('6646999433:AAGDzncpqe-h3vZBFoJONRdh0IT_F5IRsKw')
api = 'f4a8795027cd6ef2a3376afe27e3ac0d'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!\nЭто бот для проверки погоды.\nПожалуйста напиши название города.')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city_name = message.text.strip().lower()
    url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api}&units=metric')
    if url.status_code == 200:
        data = json.loads(url.text)
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        wind = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        bot.reply_to(message,
            f'Погода в {city_name}'
            f'Температура: {temp}°C (Ощущается как {feels_like}°C'
            f'Ветер: {wind}м/с'
            f'Давление: {pressure}мм.рт.ст'
            f'Влажность: {humidity}%',
            parse_mode='html'
            )
    else:
        bot.reply_to(message, 'Город указан не верно')


bot.infinity_polling()
