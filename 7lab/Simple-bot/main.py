import telebot
from telebot import types
import psycopg2
from psycopg2 import Error
import datetime
import calendar

def findDay(date):  
    born = datetime.datetime.strptime(date, '%Y %m %d').weekday()
    return (calendar.day_name[born])

def findParityToday():
    today = str(datetime.date.today())
    a = ''
    y = ''
    d = ''
    m = ''
    b = 0
    for element in today:
        if element.isdigit():
            if b < 4:
                y = y + element
            if b > 4 and b < 6:
                m = m + element
            if b > 6:
                d = d + element        
            a = a + element
            b += 1
        else:
            a = a + ' '
    # print(a)
    weeknumb = datetime.date(int(y), int(m), int(d)).isocalendar().week
    # print(weeknumb)
    if weeknumb % 2 == 1:#!!!!!!!!!!
        return ('четная')
    else:
        return ('нечетная')

# findParityToday()


token = '6108061509:AAGCA-l22QyG2shAUlzTVAvHxrtPB9_TDd8'
bot = telebot.TeleBot(token)

def db_req(a):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="manta2",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="timetable")
        cursor = connection.cursor()
        cursor.execute(a)
        record = list(cursor.fetchall())
        return record

    except (Exception, Error) as error:
        return print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help", "/timetable", "/week", "/mtuci", "/tech_support")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать своё расписание на сегодня?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message1(message):
    bot.send_message(message.chat.id, 
'Цель данного бота - быстрый доступ к расписанию.\n\nЕго можно увидеть с помощью команды /timetable, выбрав нужный день или неделю\n\nКоманда /week покажет, какая сейчас неделя.\n\nКоманда /mtuci вывеведет вас на родной сайт\n\nКоманда /tell даст боту сказать вам пару слов, но её нужно ещё разблокировать. Вперёд!\n\nСуществует секретная команда формата /"логин создателя"father)')

@bot.message_handler(commands=['mtuci'])
def start_message2(message):
    bot.send_message(message.chat.id, 'Официальный сайт вуза - https://mtuci.ru/')

@bot.message_handler(commands=['emojiFM'])
def secret_message1(message):
    bot.send_message(message.chat.id, '😘')

@bot.message_handler(commands=['creator'])
def secret_message2(message):
    bot.send_photo(message.chat.id, photo=open('photo.jpg', 'rb'))
    bot.send_message(message.chat.id, 'CREATOR')

@bot.message_handler(commands=['og'])
def secret_message3(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEI1VhkUdca2dX4_AffLNz-64VqZ-6uEgACByQAAkQwqUmOZiRotrhbzC8E')
    bot.send_message(message.chat.id, 'He inspired the CREATOR')

@bot.message_handler(commands=['week'])
def start_message3(message):
    keyboard = types.ReplyKeyboardMarkup()
    texts = findParityToday()
    if texts == 'четная':
        bot.send_message(message.chat.id, 'Сейчас чётная неделя!', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, 'Сейчас нечётная неделя!', reply_markup=keyboard)

@bot.message_handler(commands=['tech_support'])
def start_message4(message):
        bot.send_message(message.chat.id, 'Связаться с создателем - https://t.me/ttemuchin4')

@bot.message_handler(commands=['ttemuchin4father'])
def secret(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help", "/timetable", "/week", "/mtuci", "/tech_support")
    keyboard.row("/og", "/creator", "/emojiFM", "/upgradebuttons", "/tell")
    bot.send_message(message.chat.id, 'Вы ввели секретную команду! Теперь у вас есть привилегии в этом чате, поздравляю.', reply_markup=keyboard)

@bot.message_handler(commands=['timetable'])
def start_timetable(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    but1 = types.InlineKeyboardButton('Понедельник', callback_data='day1')
    but2 = types.InlineKeyboardButton('Вторник', callback_data='day2')
    but3 = types.InlineKeyboardButton('Среда', callback_data='day3')
    but4 = types.InlineKeyboardButton('Четверг', callback_data='day4')
    but5 = types.InlineKeyboardButton('Пятница', callback_data='day5')
    but6 = types.InlineKeyboardButton('Суббота', callback_data='day6')
    but7 = types.InlineKeyboardButton('Расписание на эту неделю', callback_data='thisweek')
    but8 = types.InlineKeyboardButton('Расписание на следующую неделю', callback_data='nextweek')

    keyboard.add(but1, but2, but3, but4, but5, but6, but7, but8)

    bot.send_message(message.chat.id, 'Выбрать день расписания', reply_markup=keyboard)

@bot.message_handler(commands=['tell'])
def secret_message4(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    but1 = types.InlineKeyboardButton('Всё хорошо', callback_data='good')
    but2 = types.InlineKeyboardButton('Сегодня я стал счастливее', callback_data='happier')
    but3 = types.InlineKeyboardButton('Сегодня я преодолел себя', callback_data='overcome')
    but4 = types.InlineKeyboardButton('Я ничего не понимаю', callback_data='worried')
    but5 = types.InlineKeyboardButton('Очень устал', callback_data='tired')
    but6 = types.InlineKeyboardButton('Всё плохо', callback_data='bad')

    keyboard.add(but1, but2, but3, but4, but5, but6)

    bot.send_message(message.chat.id, 'Как твой день, брат?', reply_markup=keyboard)

@bot.message_handler(commands=['upgradebuttons'])
def secret_message_timetable(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    but1 = types.InlineKeyboardButton('🚀Понедельник🚀', callback_data='day1')
    but2 = types.InlineKeyboardButton('😡Вторник😡', callback_data='day2')
    but3 = types.InlineKeyboardButton('✊Среда✊', callback_data='day3')
    but4 = types.InlineKeyboardButton('😊Четверг😊', callback_data='day4')
    but5 = types.InlineKeyboardButton('❌Пятница❌', callback_data='day5')
    but6 = types.InlineKeyboardButton('😉Суббота😉', callback_data='day6')
    but7 = types.InlineKeyboardButton('📅Расписание на эту неделю📅', callback_data='thisweek')
    but8 = types.InlineKeyboardButton('📅Расписание на следующую неделю📅', callback_data='nextweek')

    keyboard.add(but1, but2, but3, but4, but5, but6, but7, but8)

    bot.send_message(message.chat.id, 'Выбрать день расписания', reply_markup=keyboard)    

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда ты обратился по адресу')
    elif message.text.lower() == "его никто не знает":
        bot.send_message(message.chat.id, 'Ха!\nА вот и нет. Мы знаем, и тебе скажем обязательно.. Чтобы ты знал куда и когда идти за знаниями')
    elif message.text.lower() == "не хочу" or message.text.lower() == "нет":
        bot.send_message(message.chat.id, 'Ну значит в следующем семестре мы с вами не увидимся.')
    else:
        bot.send_message(message.chat.id, 'Прошу прощения, не понял вас.')



@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:#tell
        if call.data == 'good':
            bot.send_message(call.message.chat.id, 'text good')
        if call.data == 'happier':
            bot.send_message(call.message.chat.id, 'text happier')
        if call.data == 'overcome':
            bot.send_message(call.message.chat.id, 'text overcome')
        if call.data == 'worried':
            bot.send_message(call.message.chat.id, 'text worried')
        if call.data == 'tired':
            bot.send_message(call.message.chat.id, 'text tired')
        if call.data == 'bad':
            bot.send_message(call.message.chat.id, 'text bad')

        parity = findParityToday()
        print(parity)
        if parity == 'нечетная':
            if call.data == 'day5':
                texts = db_req("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Пятница' AND timetable.parity = 1 ORDER BY start_time;")
                bot.send_message(call.message.chat.id, 'Пятница (нечёт)\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s\n' % (texts[0][0], 
    texts[0][1], texts[0][2], texts[0][3], texts[1][0], texts[1][1], texts[1][2], texts[1][3], texts[2][0], texts[2][1], texts[2][2], texts[2][3], texts[3][0], texts[3][1], texts[3][2], texts[3][3]) )
                # bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.id, text= 'Ваше расписание на понедельник')
            if call.data == 'day1':
                texts = db_req("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Понедельник' AND timetable.parity = 1 ORDER BY start_time;")
                bot.send_message(call.message.chat.id, 'Понедельник (нечёт)\n\n%s | %s | %s | %s\n%s | %s | %s | %s' % (texts[0][0],
    texts[0][1], texts[0][2], texts[0][3], texts[1][0], texts[1][1], texts[1][2], texts[1][3]))
            if call.data == 'day2':
                texts = db_req("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Вторник' AND timetable.parity = 1 ORDER BY start_time;")
                bot.send_message(call.message.chat.id, 'Вторник (нечёт)\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s' % (texts[0][0],
    texts[0][1], texts[0][2], texts[0][3], texts[1][0], texts[1][1], texts[1][2], texts[1][3], texts[2][0], texts[2][1], texts[2][2], texts[2][3]))
            if call.data == 'day3':
                texts = db_req("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Среда' AND timetable.parity = 1 ORDER BY start_time;")
                bot.send_message(call.message.chat.id, 'Среда (нечёт)\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s' % (texts[0][0],
    texts[0][1], texts[0][2], texts[0][3], texts[1][0], texts[1][1], texts[1][2], texts[1][3], texts[2][0], texts[2][1], texts[2][2], texts[2][3]))
            if call.data == 'day4':
                texts = db_req("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Четверг' AND timetable.parity = 1 ORDER BY start_time;")
                bot.send_message(call.message.chat.id, 'Четверг (нечёт)\n\n%s | %s | %s | %s\n%s | %s | %s | %s' % (texts[0][0],
    texts[0][1], texts[0][2], texts[0][3], texts[1][0], texts[1][1], texts[1][2], texts[1][3]))
            if call.data == 'day6':
                bot.send_message(call.message.chat.id, 'По субботам вы работаете исключительно из дома')
            if call.data == 'thisweek':
                texts = db_req("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.parity = 1 GROUP BY day ORDER BY start_time;")
                bot.send_message(call.message.chat.id,
'Расписание на нечетную неделю\n\nПонедельник\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n\nВторник\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s\n\nСреда\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s\n\nЧетверг\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n\nПятница\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s' % (texts[0][0], texts[0][1], texts[0][2], texts[0][3], 
    texts[1][0], texts[1][1], texts[1][2], texts[1][3], texts[2][0], texts[2][1], texts[2][2], texts[2][3], texts[3][0], texts[3][1], texts[3][2], texts[3][3], texts[4][0], texts[4][1], texts[4][2], texts[4][3], 
    texts[5][0], texts[5][1], texts[5][2], texts[5][3], texts[6][0], texts[6][1], texts[6][2], texts[6][3], texts[7][0], texts[7][1], texts[7][2], texts[7][3], texts[8][0], texts[8][1], texts[8][2], texts[8][3], 
    texts[9][0], texts[9][1], texts[9][2], texts[9][3], texts[10][0], texts[10][1], texts[10][2], texts[10][3], texts[11][0], texts[11][1], texts[11][2], texts[11][3], texts[12][0], texts[12][1], texts[12][2], texts[12][3], texts[13][0], texts[13][1], texts[13][2], texts[13][3]))    

            if call.data == 'nextweek':
                texts = db_req("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.parity = 2 GROUP BY day ORDER BY start_time;")
                bot.send_message(call.message.chat.id, 
'Расписание на четную неделю\n\nПонедельник\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s\n\nВторник\n\n=====\n\nСреда\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s\n\nЧетверг\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n\nПятница\n\n%s | %s | %s | %s\n%s | %s | %s | %s' % (texts[0][0], texts[0][1], texts[0][2], texts[0][3],
    texts[1][0], texts[1][1], texts[1][2], texts[1][3], texts[2][0], texts[2][1], texts[2][2], texts[2][3], texts[3][0], texts[3][1], texts[3][2], texts[3][3], texts[4][0], texts[4][1], texts[4][2], texts[4][3], 
    texts[5][0], texts[5][1], texts[5][2], texts[5][3], texts[6][0], texts[6][1], texts[6][2], texts[6][3], texts[7][0], texts[7][1], texts[7][2], texts[7][3], texts[8][0], texts[8][1], texts[8][2], texts[8][3], 
    texts[9][0], texts[9][1], texts[9][2], texts[9][3], texts[10][0], texts[10][1], texts[10][2], texts[10][3]))   

# четная
        else:
            if call.data == 'day1':
                texts = db_req("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Понедельник' AND timetable.parity = 2 ORDER BY start_time;")
                bot.send_message(call.message.chat.id, 'Понедельник (чёт)\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s' % (texts[0][0],
    texts[0][1], texts[0][2], texts[0][3], texts[1][0], texts[1][1], texts[1][2], texts[1][3], texts[2][0], texts[2][1], texts[2][2], texts[2][3], texts[3][0], texts[3][1], texts[3][2], texts[3][3]))
            if call.data == 'day2':
                bot.send_message(call.message.chat.id, 'Вторник (чёт)\n\n =====')
            if call.data == 'day3':
                texts = db_req("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Среда' AND timetable.parity = 2 ORDER BY start_time;")
                bot.send_message(call.message.chat.id, 'Среда (чёт)\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s' % (texts[0][0], 
    texts[0][1], texts[0][2], texts[0][3], texts[1][0], texts[1][1], texts[1][2], texts[1][3], texts[2][0], texts[2][1], texts[2][2], texts[2][3]))
            if call.data == 'day4':
                texts = db_req("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Четверг' AND timetable.parity = 2 ORDER BY start_time;")
                bot.send_message(call.message.chat.id, 'Четверг (чёт)\n\n%s | %s | %s | %s\n%s | %s | %s | %s' % (texts[0][0], 
    texts[0][1], texts[0][2], texts[0][3], texts[1][0], texts[1][1], texts[1][2], texts[1][3]))
            if call.data == 'day5':
                texts = db_req("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.day = 'Пятница' AND timetable.parity = 2 ORDER BY start_time;")
                bot.send_message(call.message.chat.id, 'Пятница (чёт)\n\n%s | %s | %s | %s\n%s | %s | %s | %s' % (texts[0][0], 
    texts[0][1], texts[0][2], texts[0][3], texts[1][0], texts[1][1], texts[1][2], texts[1][3]))
            if call.data == 'day6':
                bot.send_message(call.message.chat.id, 'По субботам вы работаете исключительно из дома')
            if call.data == 'thisweek':
                texts = db_req("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.parity = 2 ORDER BY timetable.id;")
                bot.send_message(call.message.chat.id, 
'Расписание на четную неделю\n\nПонедельник\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s\n\nВторник\n\n=====\n\nСреда\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s\n\nЧетверг\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n\nПятница\n\n%s | %s | %s | %s\n%s | %s | %s | %s' % (texts[0][0], texts[0][1], texts[0][2], texts[0][3],
    texts[1][0], texts[1][1], texts[1][2], texts[1][3], texts[2][0], texts[2][1], texts[2][2], texts[2][3], texts[3][0], texts[3][1], texts[3][2], texts[3][3], texts[4][0], texts[4][1], texts[4][2], texts[4][3], 
    texts[5][0], texts[5][1], texts[5][2], texts[5][3], texts[6][0], texts[6][1], texts[6][2], texts[6][3], texts[7][0], texts[7][1], texts[7][2], texts[7][3], texts[8][0], texts[8][1], texts[8][2], texts[8][3], 
    texts[9][0], texts[9][1], texts[9][2], texts[9][3], texts[10][0], texts[10][1], texts[10][2], texts[10][3]))
            if call.data == 'nextweek':
                texts = db_req("SELECT subjects.name, timetable.room_numb, timetable.start_time, teachers.full_name FROM (timetable JOIN subjects ON subjects.id = timetable.subject) JOIN teachers ON teachers.subject = subjects.id WHERE timetable.parity = 1 ORDER BY timetable.id;")
                bot.send_message(call.message.chat.id,
'Расписание на нечетную неделю\n\nПонедельник\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n\nВторник\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s\n\nСреда\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s\n\nЧетверг\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n\nПятница\n\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s\n%s | %s | %s | %s' % (texts[0][0], texts[0][1], texts[0][2], texts[0][3], 
    texts[1][0], texts[1][1], texts[1][2], texts[1][3], texts[2][0], texts[2][1], texts[2][2], texts[2][3], texts[3][0], texts[3][1], texts[3][2], texts[3][3], texts[4][0], texts[4][1], texts[4][2], texts[4][3], 
    texts[5][0], texts[5][1], texts[5][2], texts[5][3], texts[6][0], texts[6][1], texts[6][2], texts[6][3], texts[7][0], texts[7][1], texts[7][2], texts[7][3], texts[8][0], texts[8][1], texts[8][2], texts[8][3], 
    texts[9][0], texts[9][1], texts[9][2], texts[9][3], texts[10][0], texts[10][1], texts[10][2], texts[10][3], texts[11][0], texts[11][1], texts[11][2], texts[11][3], texts[12][0], texts[12][1], texts[12][2], texts[12][3], texts[13][0], texts[13][1], texts[13][2], texts[13][3]))    
    
bot.infinity_polling() 


