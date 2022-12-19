import telebot
import random
from config import token

bot = telebot.TeleBot(token)

anecdoteList = ['Когда ты умер, ты об этом не знаешь, только тяжело твоим близким. То же самое, когда ты тупой... '
                'anekdotov.net',
                '— Продайте мне собаку. — Суку? — Не, с@ку не надо, давайте нормальную. — Сука — это пол собаки. — '
                'А зачем мне пол собаки? Давайте целую. anekdotov.net',
                'Если исключить из моего меню те продукты, которые не рекомендуют гастроэнтеролог, кардиолог, '
                'невролог, эндокринолог и уролог, то питаться мне можно только водой, и то — кипяченой. anekdotov.net',
                'Психиатр поздравляет своего пациента с прогрессом в лечении. — И это вы называете прогрессом??? Шесть '
                'месяцев назад я был Наполеоном, а сейчас — никто... anekdotov.net',
                'У вождя племени людоедов берут интервью. Журналисты задают массу вопросов. Вождь охотно отвечает, расс'
                'казывает... — Ну, а теперь последний вопрос: скажите, как Вы относитесь к евреям? — Вы знаете, я '
                'считаю антисемитизм глупейшим предрассудком. Евреи абсолютно такие же люди, как и все другие! Я и '
                'племени своему это постоянно объясняю. Но не едят! anekdotov.net']

photoList = ['https://sun9-north.userapi.com/sun9-80/s/v1/ig2/1pkl0zP17N4glp-aY9uW2Hucj75-cqnwbPC6mpMPIWLxV-y-0v'
             'O1podDOIpLBLRZzPijto2oQHIp7XDhUZirR87F.jpg?size=928x928&quality=96&type=album',
             'https://sun9-west.userapi.com/sun9-54/s/v1/ig2/S2jRxfZTfUAXbP3Ym8d2eZJb4jDHg6wQPhs5-cTZVWRNn_Q_1tC'
             '54Pp_4EpQst9Q7h7NnaSb7oueVLjuLhvev1wC.jpg?size=480x318&quality=96&type=album',
             'https://sun9-east.userapi.com/sun9-59/s/v1/ig2/pYYM5TEGIVxHljyssbrof9zND48eDLSzb1YeJGHgKuPFALJuvv7'
             '7qgJvlJAKeGCQvqwa5SlA5hM78N7K3pOkRTV1.jpg?size=1200x675&quality=96&type=album',
             'https://sun9-east.userapi.com/sun9-43/s/v1/ig2/Hh29S4XVTYg7SVHPT1q4-zrN0prmUQiueuQ26KdE-Gjwob7LdFq'
             'OW0J8ZVX6YEwOL72jHVoP1G8tSRIXVLfZPQZi.jpg?size=1024x812&quality=96&type=album',
             'https://sun9-west.userapi.com/sun9-8/s/v1/ig2/NWJ8ZiO3MIJeyHikVmzk6WMfByqlyFqnAFiZfhgEzhGsVQd9KcfL'
             '8AYlmi6Ew0f54IWtu6I6HRwDfTA8xN9AnDQQ.jpg?size=604x604&quality=96&type=album']

"""Команда СТАРТ"""
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('У меня плохое настроение')
    item2 = telebot.types.KeyboardButton('У меня хорошее настроение')
    item3 = telebot.types.KeyboardButton('Посчитай два числа')
    item4 = telebot.types.KeyboardButton('Пришли картинку')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Дарова', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def sendText(message):


    example: str = message.text

    if message.text == 'У меня плохое настроение':
        bot.send_message(message.chat.id, str(random.choice(anecdoteList)))
    elif message.text == 'У меня хорошее настроение':
        bot.send_message(message.chat.id, 'Всю жизнь тебе писать на питоне!')
    elif message.text == 'Посчитай два числа':
        bot.send_message(message.chat.id, 'Введите пример в виде "a+b" без кавычек')
    elif example.__contains__('*'):
        result = parseExample('*', example)
        bot.send_message(message.chat.id, f'Вот результат = {result}')
    elif example.__contains__('+'):
        result = parseExample('+', example)
        bot.send_message(message.chat.id, f'Вот результат = {result}')
    elif example.__contains__('-'):
        result = parseExample('-', example)
        print(result)
        bot.send_message(message.chat.id, f'Вот результат = {result}')
    elif example.__contains__('/'):
        result = parseExample('/', example)
        bot.send_message(message.chat.id, f'Вот результат = {result}')
    elif message.text == 'Пришли картинку':
        bot.send_photo(message.chat.id, random.choice(photoList))
    else:
        bot.send_message(message.chat.id, 'Ошибка')

def parseExample(symbol, example):
    firstNumber = example.split(symbol)[0]
    secondNumber = example.split(symbol)[1]
    return getResult(symbol, int(firstNumber), int(secondNumber))

def getResult(symbol, a, b):
    if symbol == '+':
        return summ(a, b)
    elif symbol == '-':
        return diff(a, b)
    elif symbol == '*':
        return mult(a, b)
    elif symbol == '/':
        return div(a, b)

def summ(a, b):
    return a + b

def diff(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

bot.polling(none_stop=True)