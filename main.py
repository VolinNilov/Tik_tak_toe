import types
import telebot
import config
from telebot import types
from DB import DB
import mysql.connector
import json

bot = telebot.TeleBot(config.TOKEN)
database = DB(config.mysql)
bot.send_message(1294113685, "Start Bot")

def json_loads(data):
    try:
        return json.loads(data)
    except:
        return None

def get_user(message):
    data = database.select('users', ['id', 'name', 'status', 'settings'], [['id', '=', message.chat.id]], 1)
    if (data):
        return {"id": data[0][0], "name": data[0][1], "status": data[0][2], "settings": json.loads(data[0][3])}
    else:
        database.insert('users', ['id', 'name', 'status', 'settings'], [[message.chat.id, message.chat.first_name, 'menu', '{\"subscribe\": [], \"commands\": []}']])
        return {"id": message.chat.id, "name": message.chat.first_name, "status": 'menu', "settings": {"subscribe": [], "commands": []}}

def log(message, user):
    query = "INSERT INTO log (text) VALUES (%s)"

def user_update(user, status=None, settings=None):
    if status and not settings:
        database.update('users', {'status': status}, [['id', '=', user['id']]])
    elif settings and not status:
        database.update('users', {'settings': settings}, [['id', '=', user['id']]])
    else:
        database.update('users', {'status': status, 'settings': settings}, [['id', '=', user['id']]])

def markups(buttons):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b = []
    for i in buttons:
        b.append(types.KeyboardButton(i))
    markup.add(*b)
    return markup

def menu_markups(user):
    answer = markups(["Поиск противника🔍", "Настройки⚙️", "Информацияℹ️"])
    b = []
    for i in user["settings"]["commands"]:
        b.append(types.KeyboardButton(i))
    if b:
        answer.add(*b)
    return answer

@bot.message_handler(commands=['start'])
def start_message(message):
    user = get_user(message)
    bot.send_message(message.chat.id,"Привет! Я бот, в котором можно играть в крестики нолики")
    log(message, user)
    user_update(user, "menu")

@bot.message_handler(commands=["reload_menu"])
def start_message(message):
    user = get_user(message)
    bot.send_message(message.chat.id,"Перезаряжаю!!!!!!!!!!", reply_markup=menu_markups(user))
    log(message, user)
    user_update(user, "menu")

bot.polling()