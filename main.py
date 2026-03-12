import os
import zipfile
import subprocess
import telebot
from telebot import types

TOKEN = "8684846516:AAEQtSfqzTWAM5juhBqsbQhXZtR2lVIpaFc"
FOUNDER_ID = 7065049730

bot = telebot.TeleBot(8684846516:AAEQtSfqzTWAM5juhBqsbQhXZtR2lVIpaFc)

NDK_PATHS = {
    "NDK 25": "/home/ndk/25",
    "NDK 21": "/home/ndk/21",
    "NDK 16": "/home/ndk/16"
}

user_ndk = {}


# ---------- МЕНЮ ----------

def main_menu(user_id):

    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("🌐 Ресурсы проекта", callback_data="resources")
    btn2 = types.InlineKeyboardButton("📥 Скачать проект", callback_data="download")
    btn3 = types.InlineKeyboardButton("📚 Команды сервера", callback_data="commands")

    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)

    if user_id == FOUNDER_ID:
        btn4 = types.InlineKeyboardButton("🛠 JNI (только основатель)", callback_data="jni")
        markup.add(btn4)

    return markup


def back_button():

    markup = types.InlineKeyboardMarkup()

    markup.add(
        types.InlineKeyboardButton("⬅️ Назад", callback_data="back")
    )

    return markup


# ---------- START ----------

@bot.message_handler(commands=['start'])
def start(message):

    text = (
        "👋 Добро пожаловать в *VIBE RUSSIA*\n\n"
        "🤖 Официальный бот проекта\n\n"
        "Выберите раздел:"
    )

    bot.send_message(
        message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=main_menu(message.from_user.id)
    )


# ---------- КНОПКИ ----------

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "resources":

        text = (
            "🌐 *Ресурсы проекта*\n\n"
            "Наш форум — временно недоступно\n"
            "Наш сайт — временно недоступно\n"
            "Наш Telegram — временно недоступно\n"
            "Наш VK — временно недоступно"
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
            "🚧 Проект находится в разработке\n\n"
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

            "🔹 ОБЩЕЕ\n"
            "/time - узнать время\n"
            "/menu (/mm) - меню игрока\n"
            "/donat - проверить донат\n"
            "/donate - донат меню\n"
            "/gps - GPS навигатор\n"
            "/referals - приглашенные\n"
            "/help - помощь\n"
            "/members - сотрудники online\n"
            "/leaders - лидеры online\n"
            "/buy - магазин\n"
            "/leave - покинуть организацию\n"
            "/setspawn - место появления\n"
            "/charity - пожертвования\n"
            "/liclist - лицензёры online\n"
            "/adlist - адвокаты online\n"
            "/news - собеседования\n"
            "/anim - анимации\n"
            "/yes - согласиться\n"
            "/no - отказаться\n"
            "/cancel - отменить заказ\n"
            "/pay [ID] - передать деньги\n"
            "/givemet [ID] - передать материалы\n"
            "/lic [ID] - лицензии\n"
            "/pass [ID] - паспорт\n"
            "/med [ID] - медкарта\n"
            "/showvb [ID] - военный билет\n"
            "/skill [ID] - навыки силы\n"
            "/changeprop [ID] - обмен\n"
            "/bg - попрошайничать\n"
            "/ad [текст] - объявление\n"
            "/inv - инвентарь\n\n"

            "💬 ЧАТ\n"
            "/s - крикнуть\n"
            "/n - OOC чат\n"
            "/w - шептать\n"
            "/c - звонок\n"
            "/sms - SMS\n"
            "/d - департамент\n"
            "/r - гос чат IC\n"
            "/rn - гос чат OOC\n"
            "/f - нелегал чат IC\n"
            "/fn - нелегал чат OOC\n"
            "/me - действие от 1 лица\n"
            "/do - действие от 3 лица\n"
            "/try - шанс 50%\n"
            "/todo - речь + действие\n"
            "/m - мегафон"
        )

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode="Markdown",
            reply_markup=back_button()
        )


    elif call.data == "jni":

        if call.from_user.id != FOUNDER_ID:

            bot.answer_callback_query(
                call.id,
                "❌ Доступ запрещён"
            )
            return

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(
            "NDK 25",
            "NDK 21",
            "NDK 16"
        )

        bot.send_message(
            call.message.chat.id,
            "🛠 JNI компилятор\n\nВыбери версию NDK:",
            reply_markup=markup
        )


    elif call.data == "back":

        bot.edit_message_text(
            "👋 *Главное меню VIBE RUSSIA*\n\nВыберите раздел:",
            call.message.chat.id,
            call.message.message_id,
            parse_mode="Markdown",
            reply_markup=main_menu(call.from_user.id)
        )


# ---------- ВЫБОР NDK ----------

@bot.message_handler(content_types=['text'])
def handle_text(message):

    if message.text in NDK_PATHS:

        user_ndk[message.from_user.id] = message.text

        bot.send_message(
            message.chat.id,
            "✅ NDK выбран\nТеперь отправь ZIP файл."
        )


# ---------- ОБРАБОТКА ZIP ----------

@bot.message_handler(content_types=['document'])
def handle_file(message):

    ndk_version = user_ndk.get(message.from_user.id)

    if not ndk_version:

        bot.send_message(
            message.chat.id,
            "❗ Сначала выбери NDK"
        )
        return

    file_info = bot.get_file(message.document.file_id)

    downloaded_file = bot.download_file(file_info.file_path)

    os.makedirs("build", exist_ok=True)

    zip_path = "build/project.zip"

    with open(zip_path, "wb") as f:
        f.write(downloaded_file)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("build/project")

    ndk_path = NDK_PATHS[ndk_version]
    jni_path = os.path.abspath("build/project/jni")

    try:

        result = subprocess.run(
            [f"{ndk_path}/ndk-build"],
            cwd=jni_path,
            capture_output=True,
            text=True
        )

        bot.send_message(
            message.chat.id,
            "✅ Сборка завершена\n\n" + result.stdout[-3000:]
        )

    except Exception as e:

        bot.send_message(
            message.chat.id,
            f"❌ Ошибка: {e}"
        )


bot.infinity_polling()
