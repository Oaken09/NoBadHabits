import telebot
from telebot import types
from tkn import my_token


bot = telebot.TeleBot(my_token)

# Основные кнопки
markup_inline = types.InlineKeyboardMarkup()
b_course = types.InlineKeyboardButton("Мой курс", callback_data="my_course")
b_aboutcourse = types.InlineKeyboardButton("Из чего состоит курс?", callback_data="about_course")
b_other = types.InlineKeyboardButton("Дополнительные советы", callback_data="additional_tips")
b_sources = types.InlineKeyboardButton("Источники", callback_data="sources")
b_quiz = types.InlineKeyboardButton("Викторина", callback_data="quiz")
markup_inline.add(b_course)
markup_inline.add(b_other, b_sources)
markup_inline.add(b_quiz, b_aboutcourse)

# Кнопки при выборе "Мой курс"
markup_course_options = types.InlineKeyboardMarkup()
b_resume = types.InlineKeyboardButton("Продолжить", callback_data="resume")
b_addcourse = types.InlineKeyboardButton("Добавить курс", callback_data="add_course")
b_back = types.InlineKeyboardButton("На главную", callback_data="На главную")
markup_course_options.add(b_resume)
markup_course_options.add(b_addcourse)
markup_course_options.add(b_back)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Выбери кнопку:", reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    received_data = call.data

    bot.delete_message(call.message.chat.id, call.message.message_id)

    bot.answer_callback_query(call.id)

    if received_data == "my_course":
        bot.send_message(call.message.chat.id, "Привет, очень хорошо, что ты осознал проблему и хочешь её решить. \nВыбери один из пунктов ниже:", reply_markup=markup_course_options)
    elif received_data == "about_course":
        bot.send_message(call.message.chat.id, "Текст для 'Из чего состоит курс?'")
    elif received_data == "additional_tips":
        bot.send_message(call.message.chat.id, "Текст для 'Дополнительные советы'")
    elif received_data == "sources":
        bot.send_message(call.message.chat.id, "Текст для 'Источники'")
    elif received_data == "quiz":
        bot.send_message(call.message.chat.id, "Текст для 'Викторина'")
    elif received_data == "resume":
        bot.send_message(call.message.chat.id, "Вы выбрали продолжить курс!")
    elif received_data == "add_course":
        bot.send_message(call.message.chat.id, "Вы выбрали добавить курс!")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, f"Я получил твое сообщение. \nЕсли хочешь чтобы я помог, нажимай на кнопки под предыдущим сообщением.")

bot.polling(none_stop=True)