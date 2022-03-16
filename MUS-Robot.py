from telebot.callback_data import CallbackData, CallbackDataFilter
from telebot import types, TeleBot
from telebot.custom_filters import AdvancedCustomFilter
from API_Tokens import *
from Contactinfo import *
from Keyboards import *

API_TOKEN = testing_bot

bot = TeleBot(API_TOKEN)



@bot.message_handler(commands=['year1info'])
def products_command_handler(message: types.Message):
    bot.send_message(message.chat.id, 'Subjects:', reply_markup=year1_keyboard())

@bot.message_handler(commands=['year2info'])
def products_command_handler(message: types.Message):
    bot.send_message(message.chat.id, 'Subjects:', reply_markup=year2_keyboard())

@bot.message_handler(commands=['year3info'])
def products_command_handler(message: types.Message):
    bot.send_message(message.chat.id, 'Subjects:', reply_markup=year3_keyboard())

@bot.message_handler(commands=['year4info'])
def products_command_handler(message: types.Message):
    bot.send_message(message.chat.id, 'Subjects:', reply_markup=year4_keyboard())

@bot.message_handler(commands=['year5info'])
def products_command_handler(message: types.Message):
    bot.send_message(message.chat.id, 'Subjects:', reply_markup=year5_keyboard())

@bot.message_handler(commands=['year6info'])
def products_command_handler(message: types.Message):
    bot.send_message(message.chat.id, 'Subjects:', reply_markup=year6_keyboard())

@bot.message_handler(commands=['dean'])
def products_command_handler(message: types.Message):
    bot.send_message(message.chat.id, 'Subjects:', reply_markup=dean_keyboard())




@bot.callback_query_handler(func=None, config=products_factory.filter())
def products_callback(call: types.CallbackQuery):
    callback_data: dict = products_factory.parse(callback_data=call.data)
    product_id = int(callback_data['product_id'])
    subject = subjects_all[product_id]

    text = f"{subject['email']}"
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=text, )


@bot.callback_query_handler(func=lambda c: c.data == 'back')
def back_callback(call: types.CallbackQuery):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text='Subjects:', )
@bot.message_handler(commands=['library'])
def send_library(message):
    bot.send_message(message.chat.id, """
https://drive.google.com/drive/u/0/folders/1jwAcnVtDQwHH2yQgbClMMBzmh85gBarW \nUse your university email to login, if you have any additional resources you wish to be added let me know, educational resources should be accessible for everyone :)
""")

@bot.message_handler(commands=['info'])
def send_library(message):
    bot.send_message(message.chat.id, """
    Hello, you can find the source code of MUS-Robot on my github account: https://github.com/ThanosApollo/MUS-Bot
""")


bot.add_custom_filter(SubjectsCallbackFilter())
bot.infinity_polling()
