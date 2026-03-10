import telebot
from telebot import types

bot = telebot.TeleBot("8684846516:AAEQtSfqzTWAM5juhBqsbQhXZtR2lVIpaFc")


# Главное меню
def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)

    resources = types.InlineKeyboardButton("🌐 Ресурсы проекта", callback_data="resources")
    download = types.InlineKeyboardButton("📥 Скачать проект", callback_data="download")
    commands = types.InlineKeyboardButton("📚 Команды сервера", callback_data="commands")

    markup.add(resources, download, commands)
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
        "👋 *Добро пожаловать в VIBE RUSSIA*\n\n"
        "🤖 Официальный бот проекта.\n"
        "Здесь вы найдете полезную информацию о сервере.\n\n"
        "👇 Выберите нужный раздел:"
    )

    bot.send_message(
        message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=main_menu()
    )


@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "resources":

        text = (
            "🌐 *Ресурсы проекта*\n\n"
            "Форум — временно недоступно\n"
            "Сайт — временно недоступно\n"
            "Telegram — временно недоступно\n"
            "VK — временно недоступно"
        )

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode="Markdown",
            reply_markup=back_button()
        )


    elif call.data == "download":

        text = (
            "📥 *Скачивание проекта*\n\n"
            "🚧 Проект находится в разработке.\n\n"
            "Следите за новостями:\n"
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


    elif call.data == "commands":

        text = (
            "📚 *Команды сервера*\n\n"

            "🔹 *ОБЩЕЕ*\n"
            "/time — узнать точное время\n"
            "/menu (/mm) — меню игрока\n"
            "/donat — проверить донат\n"
            "/donate — донат меню\n"
            "/gps — GPS навигатор\n"
            "/referals — приглашенные игроки\n"
            "/help — помощь\n"
            "/members — сотрудники online\n"
            "/leaders — лидеры online\n"
            "/buy — магазин\n"
            "/leave — покинуть организацию\n"
            "/setspawn — место появления\n"
            "/charity — пожертвования\n"
            "/liclist — лицензёры online\n"
            "/adlist — адвокаты online\n"
            "/news — собеседования\n"
            "/anim — список анимаций\n"
            "/yes — согласиться\n"
            "/no — отказаться\n"
            "/cancel — отменить заказ\n"
            "/pay [ID] — передать деньги\n"
            "/givemet [ID] — передать материалы\n"
            "/lic [ID] — показать лицензии\n"
            "/pass [ID] — показать паспорт\n"
            "/med [ID] — медкарта\n"
            "/showvb [ID] — военный билет\n"
            "/skill [ID] — навыки силы\n"
            "/changeprop [ID] — обмен\n"
            "/bg — попрошайничать\n"
            "/ad [текст] — объявление\n"
            "/inv — инвентарь\n\n"

            "💬 *ЧАТ*\n"
            "/s — крикнуть\n"
            "/n — OOC чат\n"
            "/w — шептать\n"
            "/c — позвонить\n"
            "/sms — SMS\n"
            "/d — департамент\n"
            "/r — гос чат IC\n"
            "/rn — гос чат OOC\n"
            "/f — нелегал чат IC\n"
            "/fn — нелегал чат OOC\n"
            "/me — действие от 1 лица\n"
            "/do — действие от 3 лица\n"
            "/try — шанс 50%\n"
            "/todo — речь + действие\n"
            "/m — мегафон"
        )

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode="Markdown",
            reply_markup=back_button()
        )


    elif call.data == "back":

        bot.edit_message_text(
            "👋 *Главное меню VIBE RUSSIA*\n\nВыберите раздел:",
            call.message.chat.id,
            call.message.message_id,
            parse_mode="Markdown",
            reply_markup=main_menu()
        )


bot.infinity_polling()
