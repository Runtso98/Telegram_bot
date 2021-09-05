import telebot
import random

from telebot import types

bot = telebot.TeleBot('1940652598:AAGSF_T8Mx8BjbCId8FuVLx5PGhxbeZvOI0')


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('Zigmynd.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🎲 Для принятия решений")
    btn2 = types.KeyboardButton("😊 Как дела?")
    btn3 = types.KeyboardButton("💸 Сконвертировать валюту")
    btn4 = types.KeyboardButton("🌞 Узнать погоду")
    btn5 = types.KeyboardButton("🍕 Хочу перекусить")
    btn6 = types.KeyboardButton("😎 Кино")
    btn7 = types.KeyboardButton("🧙‍♂ Гороскоп")
    btn8 = types.KeyboardButton("🎉 Развлечения")
    btn9 = types.KeyboardButton("☎ Связаться с разработчиками")

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)

    bot.send_message(message.chat.id,
                     "Добро пожаловать! \nЯ - <b>{1.first_name}</b>, бот созданный для вашего курсового "
                     "проекта, а так же проверки ваших знаний!".format(
                         message.from_user, bot.get_me(), parse_mod='html'),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def question_request(message):
    if message.chat.type == 'private':
        if message.text == "🎲 Для принятия решений":
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Узнать ответ", callback_data='search')

            markup.add(item1)

            bot.send_message(message.chat.id,
                             'Мысленно задайте себе вопрос затем кликните по активной кнопке, что бы узнать ответ!',
                             reply_markup=markup)
        elif message.text == "😊 Как дела?":

            markup = types.InlineKeyboardMarkup(row_width=2)
            item2 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item3 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item2, item3)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)

        elif message.text == "💸 Сконвертировать валюту":
            bot.send_message(message.chat.id, "https://myfin.by/converter")

        elif message.text == "🌞 Узнать погоду":
            bot.send_message(message.chat.id, "https://yandex.by/pogoda/minsk")

        elif message.text == '🍕 Хочу перекусить':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn9 = types.KeyboardButton("🚚 Доставка")
            btn10 = types.KeyboardButton("💯 Скидки на ДР")
            btn11 = types.KeyboardButton("🥧 Заведения")
            btn12 = types.KeyboardButton("💥 Акции")
            btn13 = types.KeyboardButton("🔙 Вернуться на главную")

            markup.add(btn9, btn10, btn11, btn12, btn13)

            bot.send_message(message.chat.id,
                             'Привет фудхантер! Я подскажу тебе самые годные заведения и доставки Минска',
                             reply_markup=markup)

        elif message.text == "🔙 Вернуться на главную":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn14 = types.KeyboardButton("🎲 Для принятия решений")
            btn15 = types.KeyboardButton("😊 Как дела?")
            btn16 = types.KeyboardButton("💸 Сконвертировать валюту")
            btn17 = types.KeyboardButton("🌞 Узнать погоду")
            btn18 = types.KeyboardButton("🍕 Хочу перекусить")
            btn19 = types.KeyboardButton("😎 Кино")
            btn20 = types.KeyboardButton("🧙‍♂ Гороскоп")
            btn21 = types.KeyboardButton("🎉 Развлечения")
            btn22 = types.KeyboardButton("☎ Связаться с разработчиками")

            markup.add(btn14, btn15, btn16, btn17, btn18, btn19, btn20, btn21, btn22)

            bot.send_message(message.chat.id, "Пожалуйста😉", reply_markup=markup)


        elif message.text == "🧙‍♂ Гороскоп":

            markup = types.InlineKeyboardMarkup(row_width=12)
            item4 = types.InlineKeyboardButton("Овен", callback_data='oven')
            item5 = types.InlineKeyboardButton("Телец", callback_data='taurus')
            item6 = types.InlineKeyboardButton("Близнецы", callback_data='twins')
            item7 = types.InlineKeyboardButton("Рак", callback_data='rak')
            item8 = types.InlineKeyboardButton("Лев", callback_data='lev')
            item9 = types.InlineKeyboardButton("Дева", callback_data='deva')
            item10 = types.InlineKeyboardButton("Весы", callback_data='ves')
            item11 = types.InlineKeyboardButton("Скорпион", callback_data='scorpion')
            item12 = types.InlineKeyboardButton("Стрелец", callback_data='shooter')
            item13 = types.InlineKeyboardButton("Козерог", callback_data='goat')
            item14 = types.InlineKeyboardButton("Водолей", callback_data='aquarius')
            item15 = types.InlineKeyboardButton("Рыбы", callback_data='fish')

            markup.add(item4, item5, item6)
            markup.add(item7, item8, item9)
            markup.add(item10, item11, item12)
            markup.add(item13, item14, item15)

            bot.send_message(message.chat.id, 'Давай посмотрим что тут у тебя', reply_markup=markup)

        elif message.text == "😎 Кино":

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn22 = types.KeyboardButton("🤣 Комедии")
            btn23 = types.KeyboardButton("💕 Романтика")
            btn24 = types.KeyboardButton("👀 Ужастики")
            btn25 = types.KeyboardButton("🤷‍♀ фентэзи")
            btn26 = types.KeyboardButton("🤨 Комиксы")
            btn27 = types.KeyboardButton("😲 Фантастика")
            btn28 = types.KeyboardButton("🔙 Вернуться на главную")


            markup.add(btn22, btn23, btn24, btn25, btn26, btn27, btn28)

            bot.send_message(message.chat.id, "Отлично, выбирай", reply_markup=markup)

        elif message.text == "🎉 Развлечения":
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("театры", callback_data='theatre')
            item2 = types.InlineKeyboardButton("музыка", callback_data='music')
            item3 = types.InlineKeyboardButton("экстремальные развлечения", callback_data='extreme')

            markup.add(item1, item2)
            markup.add(item3)

            bot.send_message(message.chat.id, 'пожалуйста', reply_markup=markup)

        elif message.text == "☎ Связаться с разработчиками":
            bot.send_message(message.chat.id, "https://overone-telebot.nethouse.ru/")


        if message.text == "🚚 Доставка":
            bot.send_message(message.chat.id, "https://delivio.by")
            bot.send_message(message.chat.id, "https://www.menu.by/")
            bot.send_message(message.chat.id, "https://enot.itprofit.dev")
            bot.send_message(message.chat.id, "https://pzz.by/")

        elif message.text == "💯 Скидки на ДР":
            bot.send_message(message.chat.id, "https://paul.relax.by")
            bot.send_message(message.chat.id, "https://t.me/SourBartenderBot")
            bot.send_message(message.chat.id, "https://brovar.by")

        elif message.text == "🥧 Заведения":
            markup = types.InlineKeyboardMarkup(row_width=7)
            item16 = types.InlineKeyboardButton("💨 Кальян", callback_data='hookah')
            item17 = types.InlineKeyboardButton("🌓 24ч ", callback_data='hour')
            item18 = types.InlineKeyboardButton("🍻 Бар", callback_data='bar')
            item19 = types.InlineKeyboardButton("🍣 Суши", callback_data='susi')
            item20 = types.InlineKeyboardButton("🍕 Пицца", callback_data='pizza')
            item21 = types.InlineKeyboardButton("🍔 Бургеры", callback_data='burger')
            item22 = types.InlineKeyboardButton("🎙 Караоке", callback_data='karaoke')

            markup.row(item16, item17)
            markup.row(item18, item19)
            markup.row(item20, item21)
            markup.row(item22)

            bot.send_message(message.chat.id, 'Тут ты найдешь бары и рестораны на любой вкус!', reply_markup=markup)

        elif message.text == "💥 Акции":
            markup = types.InlineKeyboardMarkup(row_width=2)
            item23 = types.InlineKeyboardButton("По понедельникам", callback_data='monday')
            item24 = types.InlineKeyboardButton("По вторникам", callback_data='tuesday')

            markup.add(item23, item24)

            bot.send_message(message.chat.id, 'Я подобрал для тебя лучшие акции этой недели!', reply_markup=markup)

        if message.text == "🤣 Комедии":
            bot.send_message(message.chat.id, 'https://kinokrad.co/komediya-3/')
        elif message.text == "💕 Романтика":
            bot.send_message(message.chat.id, 'https://rezka.ag/collections/248-luchshie-romanticheskie-komedii/')
        elif message.text == "👀 Ужастики":
            bot.send_message(message.chat.id, 'https://kinokrad.co/uzhasy-online-3/')
        elif message.text == "🤷‍♀ фентэзи":
            bot.send_message(message.chat.id, 'https://kinokrad.co/fentezi3/')
        elif message.text == "🤨 Комиксы":
            bot.send_message(message.chat.id, 'https://rezka.ag/collections/322-ekranizacii-marvel-comics/')
        elif message.text == "😲 Фантастика":
            bot.send_message(message.chat.id, 'https://kinokrad.co/fantastika4/')
        elif message.text == "🔙 Вернуться на главную":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn29 = types.KeyboardButton("🎲 Для принятия решений")
            btn30 = types.KeyboardButton("😊 Как дела?")
            btn31 = types.KeyboardButton("💸 Сконвертировать валюту")
            btn32 = types.KeyboardButton("🌞 Узнать погоду")
            btn33 = types.KeyboardButton("🍕 Хочу перекусить")
            btn34 = types.KeyboardButton("😎 Кино")
            btn35 = types.KeyboardButton("🧙‍♂ Гороскоп")
            btn36 = types.KeyboardButton("🎉 Развлечения")
            btn37 = types.KeyboardButton("☎ Связаться с разработчиками")

            markup.add(btn29, btn30, btn31, btn32, btn33, btn34, btn35, btn36, btn37)

            bot.send_message(message.chat.id, "Пожалуйста😉", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Я не знаю чем вам помочь 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'search':
            if random.randint(0, 1) == 0:
                bot.send_message(call.message.chat.id, 'Yes')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Спасибо, что обратился!", reply_markup=None)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

            else:
                bot.send_message(call.message.chat.id, 'No')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Спасибо, что обратился!", reply_markup=None)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False)


        if call.data == 'good':
            bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Может сделаем что-то еще?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'bad':
            bot.send_message(call.message.chat.id, 'Бывает 😢')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Может сделаем что-то еще?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)


        if call.data == 'hookah':
            bot.send_message(call.message.chat.id, "https://myata-lounge.by")
            bot.send_message(call.message.chat.id, "https://hookah-place.relax.by")
            bot.send_message(call.message.chat.id, "https://chayniy-pianitsa.relax.by")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Обращайся еще!", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'hour':
            bot.send_message(call.message.chat.id, "https://goldencoffee.relax.by")
            bot.send_message(call.message.chat.id, "http://besso.by")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Обращайся еще!", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'bar':
            bot.send_message(call.message.chat.id, "https://www.instagram.com/spichki_bar/?hl=ru")
            bot.send_message(call.message.chat.id, "https://www.instagram.com/peresmeshnik_minsk/?hl=ru")
            bot.send_message(call.message.chat.id, "http://leone.by")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Обращайся еще!", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'susi':
            bot.send_message(call.message.chat.id, "https://ronin.by")
            bot.send_message(call.message.chat.id, "https://sushichefarts.by")
            bot.send_message(call.message.chat.id, "https://sushihouse.by")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Обращайся еще!", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'pizza':
            bot.send_message(call.message.chat.id, "https://dominos.by")
            bot.send_message(call.message.chat.id, "https://www.pizzatempo.by")
            bot.send_message(call.message.chat.id, "https://papajohns.by/minsk")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Обращайся еще!", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'burger':
            bot.send_message(call.message.chat.id, "https://www.instagram.com/burgerlab.by/?hl=ru")
            bot.send_message(call.message.chat.id, "https://enzo.relax.by")
            bot.send_message(call.message.chat.id, "https://www.instagram.com/cleverminsk/?hl=ru")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Обращайся еще!", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'karaoke':
            bot.send_message(call.message.chat.id, "https://polugar.bar/polugar")
            bot.send_message(call.message.chat.id, "https://www.instagram.com/angelsclubminsk/?hl=ru")
            bot.send_message(call.message.chat.id, "https://jelsa.relax.by")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Обращайся еще!", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)


        if call.data == 'monday':
            bot.send_message(call.message.chat.id, "https://papajohns.by/minsk")
            bot.send_message(call.message.chat.id, "https://www.instagram.com/cleverminsk/?hl=ru")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Чем еще могу помочь?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'tuesday':
            bot.send_message(call.message.chat.id, "https://www.dominos.by/news/723")
            bot.send_message(call.message.chat.id, "https://www.instagram.com/cleverminsk/?hl=ru")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Чем еще могу помочь?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)


        if call.data == 'oven':
            bot.send_message(call.message.chat.id, 'https://horo.mail.ru/prediction/aries/today/')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что-то еще подсказать?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'taurus':
            bot.send_message(call.message.chat.id, 'https://horo.mail.ru/prediction/taurus/today/')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что-то еще подсказать?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'twins':
            bot.send_message(call.message.chat.id, 'https://horo.mail.ru/prediction/gemini/today/')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что-то еще подсказать?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'rak':
            bot.send_message(call.message.chat.id, 'https://horo.mail.ru/prediction/cancer/today/')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что-то еще подсказать?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'lev':
            bot.send_message(call.message.chat.id, 'https://horo.mail.ru/prediction/leo/today/')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что-то еще подсказать?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'deva':
            bot.send_message(call.message.chat.id, 'https://horo.mail.ru/prediction/virgo/today/')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что-то еще подсказать?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'ves':
            bot.send_message(call.message.chat.id, 'https://horo.mail.ru/prediction/libra/today/')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что-то еще подсказать?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'scorpion':
            bot.send_message(call.message.chat.id, 'https://horo.mail.ru/prediction/scorpio/today/')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что-то еще подсказать?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'shooter':
            bot.send_message(call.message.chat.id, 'https://horo.mail.ru/prediction/sagittarius/today/')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что-то еще подсказать?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'goat':
            bot.send_message(call.message.chat.id, 'https://horo.mail.ru/prediction/capricorn/today/')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что-то еще подсказать?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'aquarius':
            bot.send_message(call.message.chat.id, 'https://horo.mail.ru/prediction/aquarius/today/')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Что-то еще подсказать?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'fish':
            bot.send_message(call.message.chat.id, 'https://horo.mail.ru/prediction/pisces/today/')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Что-то еще подсказать?", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)


        if call.data == 'theatre':
            bot.send_message(call.message.chat.id, "https://www.kvitki.by/rus/bileti/teatr/")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Надеюсь вам понравится!", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'music':
            bot.send_message(call.message.chat.id, "https://www.kvitki.by/rus/bileti/muzyka/")
            bot.send_message(call.message.chat.id, "https://music.yandex.by/home")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Мы все чаще зависим от музыки!", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

        elif call.data == 'extreme':
            bot.send_message(call.message.chat.id, "https://surprise.by/catalog/baloon_flight/")
            bot.send_message(call.message.chat.id, "https://aerotruba.by/tariffs")
            bot.send_message(call.message.chat.id, "https://justfly.by")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Отдохнем с огоньком!", reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False)


# RUN
bot.polling(none_stop=True)
