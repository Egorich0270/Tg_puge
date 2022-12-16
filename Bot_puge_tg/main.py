import telebot

token = 'наш токен'
bot = telebot.TeleBot('%5903639227:AAF5waELuIAmMllklqF4j2BBD7T97eY0r-o%')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")


bot.infinity_poling()
