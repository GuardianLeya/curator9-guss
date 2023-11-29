import telebot

name = ''
surname = ''
age = 0

bot = telebot.TeleBot("6940561724:AAEqrArQDfkqNoZfKp921XlBqgigf9xL2b8")


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Сообщение')


@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, '*БЕГИ!!!* БЕГИ!!!', parse_mode='Markdown')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'ЭТО [ССЫЛКА](https://pastebin.com/)', parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)  # следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')


def get_name(message):  # получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:  # проверяем что возраст изменился
        try:
            age = int(message.text)  # проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    bot.send_message(message.from_user.id, 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?')


bot.infinity_polling()
