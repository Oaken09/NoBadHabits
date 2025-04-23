import telebot
from telebot import types
from tkn import my_token

bot = telebot.TeleBot(my_token)

markup_inline = types.InlineKeyboardMarkup()

b_course = types.InlineKeyboardButton("Мой курс", callback_data="Мой курс")
b_aboutcourse = types.InlineKeyboardButton("Из чего состоит курс?", callback_data="Из чего состоит курс?")
b_other = types.InlineKeyboardButton("Дополнительные советы", callback_data="Дополнительные советы")
b_sources = types.InlineKeyboardButton("Источники", callback_data="Источники")
b_quiz = types.InlineKeyboardButton("Викторина", callback_data="Викторина")

markup_inline.add(b_course)
markup_inline.add(b_other, b_sources)
markup_inline.add(b_quiz, b_aboutcourse)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Выбери кнопку:", reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    received_data = call.data

    bot.delete_message(call.message.chat.id, call.message.message_id)

    bot.answer_callback_query(call.id)

    if received_data == "Мой курс":
        bot.send_message(call.message.chat.id, "Привет, очень хорошо, что ты осознал проблему и хочешь её решить. \nВыбери один из пунктов ниже:")
    elif received_data == "Из чего состоит курс?":
        bot.send_message(call.message.chat.id, "Текст для 'Из чего состоит курс?'")
    elif received_data == "Дополнительные советы":
        bot.send_message(call.message.chat.id, "Текст для 'Дополнительные советы'")
    elif received_data == "Источники":
        bot.send_message(call.message.chat.id, "Текст для 'Источники'")
    elif received_data == "Викторина":
         bot.send_message(call.message.chat.id, "Текст для 'Викторина'")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, f"Я получил твое сообщение: '{message.text}'. \nНажимай на кнопки под предыдущим сообщением, если хочешь выбрать пункт.")


bot.polling(none_stop=True)