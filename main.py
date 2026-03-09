import telebot
from telebot import types

bot = telebot.TeleBot("8671958026:AAELbiwVYNeiLi6agJRxc5qoehSC4baBi_A")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("Ресурсы", callback_data="resources")
    btn2 = types.InlineKeyboardButton("Скачать", callback_data="download")
    btn3 = types.InlineKeyboardButton("Команды для новичков", callback_data="newbie")

    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)

    bot.send_message(
        message.chat.id,
        "Приветствую, я бот проекта VIBE RUSSIA",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "resources":
        bot.send_message(
            call.message.chat.id,
            "Наш форум не кликабельно (временно)\n"
            "Наш сайт не кликабельно (временно)\n"
            "Наш телеграм не кликабельно (временно)\n"
            "Наш Vk не кликабельно (временно)"
        )

    elif call.data == "download":
        bot.send_message(
            call.message.chat.id,
            "Наш проект находится на разработке, следите за разработкой в наших соцсетях:\n\n"
            "ВКонтакте - ссылка\n"
            "Telegram - ссылка"
        )

    elif call.data == "newbie":
        bot.send_message(
            call.message.chat.id,
            "Этот раздел находится в разработке"
        )

bot.infinity_polling()
