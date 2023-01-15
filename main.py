#!/usr/bin/python3

import os
from webbrowser import get
import telebot

from display.create import get_init_text, get_stalls_text, get_fcjap_text, get_fctai_text, get_fcjap_order_text
from keyboard.create import init_canteen_keyboard, get_canteen_keyboard, get_poll_keyboard, get_stalls_keyboard, get_fcjap_keyboard, get_fctai_keyboard

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

poll_name = "untitled"
canteen = "Flavours @ UTown (Foodclique)"

@bot.message_handler(commands=['start'])
def start(message):
    text = "Hello, welcome to NUS Dabao!\nType or click /create to create a new poll.\nType or click /help for instructions on using this pollbot."
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['help'])
def help(message):
    text = "1. Type or click /create to create a new poll.\n2. Choose the canteen where you would like to collate your dabao orders from.\n3. Send me the name of your poll.\n4. Once the poll is created, a list of stalls from the canteen chosen will appear. Choose a stall and select a food item from the menu.\n5. Your order is placed!"
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: True, commands=['create'])
def initialise(message):
    text = get_init_text(canteen)
    keyboard = init_canteen_keyboard()
    sent = bot.send_message(message.chat.id, text, reply_markup=keyboard)
    bot.register_next_step_handler(sent, title)

def title(message): 
    global poll_name
    poll_name = message.text + "\n\n"
    text = poll_name + get_stalls_text(canteen)
    keyboard = get_poll_keyboard()
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global canteen
    first_name = call.message.chat.first_name
    if call.data == "cb_canteen":
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=get_canteen_keyboard())
    elif call.data == "cb_ff":
        canteen = "Fine Food @ UTown"
        text = get_init_text(canteen)
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif call.data == "cb_frontier":
        canteen = "Frontier"
        text = get_init_text(canteen)
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif call.data == "cb_deck":
        canteen = "The Deck"
        text = get_init_text(canteen)
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif call.data == "cb_technoedge":
        canteen = "Techno Edge"
        text = get_init_text(canteen)
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif call.data == "cb_selectstall":
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=get_stalls_keyboard(canteen))
    elif call.data == "cb_delete":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif call.data == "cb_back":
        text = poll_name + get_stalls_text(canteen)
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=get_stalls_keyboard(canteen))
    elif call.data == "cb_fcjap":
        text = poll_name + get_fcjap_text()
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=get_fcjap_keyboard())
    elif call.data == "fcjap_1":
        order = "{} - Tenzaru Soba".format(first_name)
        text = poll_name + get_fcjap_order_text(order)
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif call.data == "fcjap_2":
        order = "{} - Salmon Mentai Don".format(first_name)
        text = poll_name + get_fcjap_order_text(order)
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif call.data == "cb_fctai":
        text = poll_name + get_fctai_text()
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=get_fctai_keyboard())

bot.polling()
#bot.infinity_polling()