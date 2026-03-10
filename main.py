import telebot
from telebot import types

bot = telebot.TeleBot("8671958026:AAELbiwVYNeiLi6agJRxc5qoehSC4baBi_A")

# Главное меню
def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)

    resources = types.InlineKeyboardButton("🌐 Ресурсы проекта", callback_data="resources")
    download = types.InlineKeyboardButton("📥 Скачать проект", callback_data="download")
    newbie = types.InlineKeyboardButton("📚 Команды для новичков", callback_data="newbie")

    markup.add(resources, download, newbie)
    return markup


# Кнопка назад
def back_button():
    markup = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton("⬅️ Назад", callback_data="back")
    markup.add(back)
    return markup


@bot.message_handler(commands=['start'])
def start(message):

    text = (
        "👋 *Приветствую!*\n\n"
        "🤖 Я официальный бот проекта *VIBE RUSSIA*\n\n"
        "🎮 Здесь ты можешь найти:\n"
        "• полезные ресурсы проекта\n"
        "• информацию о скачивании\n"
        "• команды для новичков\n\n"
        "👇 Выбери нужный раздел:"
    )

    bot.send_message(
        message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=main_menu()
    )


@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    # Ресурсы
    if call.data == "resources":

        text = (
            "🌐 *Ресурсы проекта VIBE RUSSIA*\n\n"
            "💬 Наш форум — не кликабельно (временно)\n"
            "🌍 Наш сайт — не кликабельно (временно)\n"
            "📢 Наш Telegram — не кликабельно (временно)\n"
            "📱 Наш VK — не кликабельно (временно)\n\n"
            "⚙️ Скоро ссылки будут доступны."
        )

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode="Markdown",
            reply_markup=back_button()
        )

    # Скачать
    elif call.data == "download":

        text = (
            "📥 *Скачивание проекта*\n\n"
            "🚧 Наш проект находится в разработке.\n\n"
            "📢 Следите за новостями в наших соцсетях:\n\n"
            "📱 ВКонтакте — ссылка\n"
            "💬 Telegram — ссылка"
        )

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode="Markdown",
            reply_markup=back_button()
        )

    # Команды для новичков
    elif call.data == "newbie":

        text = (
            "📚 *Команды для новичков*\n\n"
            "🚧 Этот раздел находится в разработке.\n\n"
            "Скоро здесь появятся:\n"
            "• список команд\n"
            "• гайды по серверу\n"
            "• помощь новичкам"
        )

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode="Markdown",
            reply_markup=back_button()
        )

    # Назад
    elif call.data == "back":

        text = (
            "👋 *Главное меню VIBE RUSSIA*\n\n"
            "Выберите нужный раздел:"
        )

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode="Markdown",
            reply_markup=main_menu()
        )


bot.infinity_polling()
