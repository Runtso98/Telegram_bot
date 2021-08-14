import telebot
import random

from telebot import types

bot = telebot.TeleBot('1940652598:AAGSF_T8Mx8BjbCId8FuVLx5PGhxbeZvOI0')


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Для принятия решений")
    item2 = types.KeyboardButton("😊 Как дела?")
    item3 = types.KeyboardButton("Сконвертировать валюту")
    item4 = types.KeyboardButton("Узнать погоду")

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(
                         message.from_user, bot.get_me(), parse_mod='html'),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Для принятия решений':
            bot.send_message(message.chat.id, 'Мысленно задайте себе вопрос, нажмите, что бы узнать ответ')

            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Узнать ответ", callback0_data='yes')

            markup.add(item1)

            if random.randint(0, 1) == 0:
                bot.send_message(message.chat.id, 'Yes')
            else:
                bot.send_message(message.chat.id, 'No')

        elif message.text == '😊 Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        elif message.text == "Сконвертировать валюту":
            bot.send_message(message.chat.id, "https://myfin.by/converter")

        elif message.text == "Узнать погоду":
            bot.send_message(message.chat.id, "https://yandex.by/pogoda/minsk")

        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback0_inline(call):
    try:
        if call.message:
            if call.data == 'yes':
                if random.randint(0, 1) == 0:
                    bot.send_message(call.message.chat.id, 'Yes')
                else:
                    bot.send_message(call.message.chat.id, 'No')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="🎲 Для принятия решений",
                                  reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!")

    except Exception as a:
        print(repr(a))


def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                                  reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
