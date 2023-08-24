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
  url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}')
