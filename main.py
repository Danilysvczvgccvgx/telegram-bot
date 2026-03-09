import telebot

bot = telebot.TeleBot("8671958026:AAELbiwVYNeiLi6agJRxc5qoehSC4baBi_A")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот работает!")

bot.infinity_polling()
