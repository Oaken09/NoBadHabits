import telebot
from telebot import types
from tkn import my_token

bot = telebot.TeleBot(my_token)

keyboard = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton(text='Мой курс', callback_data='course')
keyboard.add(button1)
button2 = types.InlineKeyboardButton(text='Из чего состоит курс?', callback_data='aboutcourse')
keyboard.add(button2)
button3 = types.InlineKeyboardButton(text='Дополнительные советы', callback_data='other')
keyboard.add(button3)
button4 = types.InlineKeyboardButton(text='Источники', callback_data='sources')
keyboard.add(button4)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, очень хорошо, что ты осознал проблему и хочешь её решить. \nВыбери один из пунктов ниже:", reply_markup=keyboard)

    else:
        bot.send_message(message.from_user.id, "Напиши /start")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "course":
        msg = "Выбери от чего ты хочешь избавиться:"
        button5 = types.InlineKeyboardButton(text='Сигареты', callback_data='smoking')
        keyboard.add(button5)
        button6 = types.InlineKeyboardButton(text='Вейп', callback_data='vaping')
        keyboard.add(button6)
        button7 = types.InlineKeyboardButton(text='Алкоголь', callback_data='alcohol')
        keyboard.add(button7)
        button8 = types.InlineKeyboardButton(text='"Энергетики', callback_data='enrgy')
        keyboard.add(button8)
        button9 = types.InlineKeyboardButton(text='На главную', callback_data='first')
        keyboard.add(button9)

        keyboard = types.InlineKeyboardMarkup()
        key_PrKv_Pr = types.InlineKeyboardButton(text='ПРЯМОУГОЛЬНИК', callback_data='Rectangle')
        keyboard.add(key_PrKv_Pr)
        key_PrKv_Kv = types.InlineKeyboardButton(text='КВАДРАТ', callback_data='Square')
        keyboard.add(key_PrKv_Kv)

        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, "Выбери нужную фигуру:", reply_markup=keyboard)

    elif call.data == "Rectangle":
        bot.send_message(call.message.chat.id, "Это информация о прямоугольнике...")
    elif call.data == "Square":
        bot.send_message(call.message.chat.id, "Это информация о квадрате...")
    elif call.data == "triangle":
        msg = "Сейчас я ОЛЕГ покажу, что я знаю о треугольниках."

        keyboard = types.InlineKeyboardMarkup()
        key_Tri_Pr = types.InlineKeyboardButton(text='ПРЯМОУГОЛЬНЫЙ ТРЕУГОЛЬНИК', callback_data='triangle PR')
        keyboard.add(key_Tri_Pr)
        key_Tri_Or = types.InlineKeyboardButton(text='ОСТРОУГОЛЬНЫЙ ТРЕУГОЛЬНИК', callback_data='triangle OS')
        keyboard.add(key_Tri_Or)
        key_Tri_Ty = types.InlineKeyboardButton(text='ТУПОУГОЛЬНЫЙ ТРЕУГОЛЬНИК', callback_data='triangle TY')
        keyboard.add(key_Tri_Ty)

        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, "Выбери тип треугольника:", reply_markup=keyboard)

    elif call.data == "triangle PR":
        bot.send_message(call.message.chat.id, "Это информация о прямоугольном треугольнике...")
    elif call.data == "triangle OS":
        bot.send_message(call.message.chat.id, "Это информация об остроугольном треугольнике...")
    elif call.data == "triangle TY":
        bot.send_message(call.message.chat.id, "Это информация о тупоугольном треугольнике...")


# Запускаем бота
bot.polling(none_stop=True)