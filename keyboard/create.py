import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

def init_canteen_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Change canteen", callback_data="cb_canteen"))
    return markup

def get_canteen_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Fine Food (UTown)", callback_data="cb_ff"),
                InlineKeyboardButton("Frontier", callback_data="cb_frontier"),
                InlineKeyboardButton("The Deck", callback_data="cb_deck"),
                InlineKeyboardButton("Techno Edge", callback_data="cb_technoedge"))
    return markup

def get_poll_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Share this poll", switch_inline_query=""),
                InlineKeyboardButton("Select", callback_data="cb_selectstall"),
                InlineKeyboardButton("Close", callback_data="cb_close"),
                InlineKeyboardButton("Delete", callback_data="cb_delete"))
    return markup

def get_stalls_keyboard(canteen):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    if canteen == "Flavours @ UTown (Foodclique)":
        markup.add(InlineKeyboardButton("Japanese", callback_data="cb_fcjap"),
                    InlineKeyboardButton("Taiwanese", callback_data="cb_fctai"),
                    InlineKeyboardButton("Noodles", callback_data="cb_fcnoo"),
                    InlineKeyboardButton("Chicken Rice", callback_data="cb_fcchi"),
                    InlineKeyboardButton("Mini Wok", callback_data="cb_fcmin"),
                    InlineKeyboardButton("Tenderbreast", callback_data="cb_fcten"))
    return markup

def get_fcjap_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("1", callback_data="fcjap_1"),
                InlineKeyboardButton("2", callback_data="fcjap_2"),
                InlineKeyboardButton("3", callback_data="fcjap_3"),
                InlineKeyboardButton("4", callback_data="fcjap_4"),
                InlineKeyboardButton("5", callback_data="fcjap_5"),
                InlineKeyboardButton("6", callback_data="fcjap_6"),
                InlineKeyboardButton("7", callback_data="fcjap_7"),
                InlineKeyboardButton("8", callback_data="fcjap_8"))
    markup.add(InlineKeyboardButton("Back", callback_data="cb_back"))
    return markup

def get_fctai_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("1", callback_data="fctai_1"),
                InlineKeyboardButton("2", callback_data="fctai_2"),
                InlineKeyboardButton("3", callback_data="fctai_3"),
                InlineKeyboardButton("4", callback_data="fctai_4"),
                InlineKeyboardButton("5", callback_data="fctai_5"),
                InlineKeyboardButton("6", callback_data="fctai_6"),
                InlineKeyboardButton("7", callback_data="fctai_7"),
                InlineKeyboardButton("8", callback_data="fctai_8"),
                InlineKeyboardButton("9", callback_data="fctai_9"))
    markup.add(InlineKeyboardButton("Back", callback_data="cb_back"))
    return markup