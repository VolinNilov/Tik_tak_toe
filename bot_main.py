import telebot
from config import TOKEN
from telebot import types
bot = telebot.TeleBot(TOKEN)

play_ground = [[],[]]

#@bot.message_handler(content_types=['text'])
#def get_text_messages(message):
    #if message.text == "Привет":
        #bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    #elif message.text =="Играть":
        #bot.send_message(message.from_user.id, "Поиск игры")
    #elif message.text == "Help" or "help":
        #bot.send_message(message.from_user.id, "Команды бота : Играть-начинается игра")
    #elif message.text == "рейтинг":
        #bot.send_message(message.from_user.id, "кд")
    #else:
        #bot.send_message(message.from_user.id, "Я тебя не понимаю")

@bot.message_handler(commands=['start'])
def start_game(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item_id= types.KeyboardButton('начать игру')
    markup_reply.add(item_id)
    bot.send_message(message.chat.id,'нажмите на одну из конпок', reply_markup = markup_reply)
    if "НАЧАТЬ ИГРУ" in message.text.upper():
        markup_buttons_pers = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_x = types.KeyboardButton('X')
        item_o = types.KeyboardButton('O')
        markup_buttons_pers.add(item_x, item_o)
        bot.send_message(message.chat.id, 'хороший выбор', reply_markup=markup_buttons_pers)

@bot.message_handler(commands=['inline'])
def inline_start_game(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_1_1 = types.InlineKeyboardButton(f'  ', callback_data = 'b_1_1')
    item_1_2 = types.InlineKeyboardButton(f'  ', callback_data = 'b_1_2')
    item_1_3 = types.InlineKeyboardButton(f'  ', callback_data = 'b_1_3')
    item_2_1 = types.InlineKeyboardButton(f'  ', callback_data = 'b_2_1')
    item_2_2 = types.InlineKeyboardButton(f'  ', callback_data = 'b_2_2')
    item_2_3 = types.InlineKeyboardButton(f'  ', callback_data = 'b_2_3')
    item_3_1 = types.InlineKeyboardButton(f'  ', callback_data = 'b_3_1')
    item_3_2 = types.InlineKeyboardButton(f'  ', callback_data = 'b_3_2')
    item_3_3 = types.InlineKeyboardButton(f'  ', callback_data = 'b_3_3')
    markup_inline.add(item_1_1, item_1_2, item_1_3, item_2_1, item_2_2, item_2_3, item_3_1, item_3_2, item_3_3)
    bot.send_message(message.chat.id, 'Hi', reply_markup = markup_inline)
    print(f'Comand from user id {message.from_user.id} with the name {message.from_user.first_name}:       {message.text}')

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'b_1_1':
            print(f'User press:        b_1_1')
        elif call.data == 'b_1_2':
            print(f'User press:        b_1_2')
        elif call.data == 'b_1_3':
            print(f'User press:        b_1_3')
        elif call.data == 'b_2_1':
            print(f'User press:        b_2_1')
        elif call.data == 'b_2_2':
            print(f'User press:        b_2_2')
        elif call.data == 'b_2_3':
            print(f'User press:        b_2_3')
        elif call.data == 'b_3_1':
            print(f'User press:        b_3_1')
        elif call.data == 'b_3_2':
            print(f'User press:        b_3_2')
        elif call.data == 'b_3_3':
            print(f'User press:        b_3_3')

@bot.message_handler(commands=['web'])
def website(message):
  markup = types.InlineKeyboardMarkup()
  markup.add(types.InlineKeyboardButton("Go", url = "https://www.youtube.com/watch?v=HodO2eBEz_8&t=430s"))
  bot.send_message(message.chat.id, "Класный ход", reply_markup=markup)



#messege.text = message.text.upper()
bot.polling(non_stop = True)
