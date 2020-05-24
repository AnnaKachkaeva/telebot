import telebot
import time
import random
import requests
import json

bot = telebot.TeleBot("1244754721:AAFt9cUux1RoHsleq6CT5_aH8vvF-JgcWvE")
MY_ID = 287201315
APPID = 'd2bc6bbc1f57282f357618ad18ed3f6e' #for weather


def CreateKeyboard(ArrayOfButtons):
    keyboard = json.dumps({"keyboard": ArrayOfButtons})
    return keyboard


Main_Keyboard = CreateKeyboard([
    ['WEATHER'],
    ['calculator'],
])


@bot.message_handler(commands=['start'])
def start_message(message):
    print('chat id: ', message.chat.id)
    bot.send_message(message.chat.id,'wooah *потягушки*')
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAALcfl7IJyamc6E_vzBONbVsTsjnjDgeAAL1AQACQq9pAAHh8YvNyNZ2pRkE')
    bot.send_message(message.chat.id, 'Привет, ты разбудил меня, нажав /start')#, reply_markup=Main_Keyboard)
    bot.send_message(message.chat.id,'В каком городе узнать погоду?')

@bot.message_handler(content_types=['text'])
def finding_weather(message):
        city = message.text
        try:
            url = 'https://api.openweathermap.org/data/2.5/weather?q={}&APPID=d2bc6bbc1f57282f357618ad18ed3f6e'.format(city)
            response = requests.get(url=url)
            text = response.json()
            weather = {
                'name':(text['name']),
                'temperature': round(int(text['main']['temp']) - 273.15),
                'feels': round(int(text['main']['feels_like']) - 273.15),
                'minimal': round(int(text['main']['temp_min']) - 273.15),        
                'maximal': round(int(text['main']['temp_max']) - 273.15),
            }
            
            print(message.chat.username, message.chat.id,' : ', str(weather['name']))
            ans = 'Сегодня температура в [ ' + (str(weather['name'])) + ' ]:\n\nСредняя: ' + str(weather['temperature']) + '°C\nОщущается как: ' + str(weather['feels']) + '°C\nМинимальная: ' + str(weather['minimal']) + '°C\nМаксимальная: ' + str(weather['maximal']) + '°C'
            bot.send_message(message.chat.id, ans)
            bot.send_sticker(message.chat.id,'CAACAgIAAxkBAALcgl7ILDfWSs3aY9-1KxQn8kIuwDkrAALnAQACQq9pAAGoFM6fqASRbxkE')
        except Exception:
            print(message.chat.username, message.chat.id,'\terror:', str(text['message']),'\terror:', city)
            bot.send_message(message.chat.id, "grhgrgr..gr...")
            bot.send_message(message.chat.id, "where...где ж этот город...")
            bot.send_sticker(message.chat.id,'CAACAgIAAxkBAALcgF7IK11yWORs6Gal6LmRAkrDrSN-AAL_AQACQq9pAAEkHKbbx-8otRkE')
            bot.send_message(message.chat.id, "ничего не понял")
            bot.send_message(message.chat.id,'Повтори-ка\nВ каком городе узнать погоду?')


'''def  send_text(message):
    if message.text == 'WEATHER':
        finding_weather(message)
        bot.send_message(message.chat.id, reply_markup=Main_Keyboard)
    if message.text == 'calculator':
        #calculator
        bot.send_message(message.chat.id, reply_markup=Main_Keyboard)
    else :
        bot.send_message(message.chat.id, reply_markup=Main_Keyboard)
        bot.send_message(message.chat.id, 'ну я так не умею')'''


bot.polling(none_stop=True)