from telebot.callback_data import CallbackData, CallbackDataFilter
from telebot import types, TeleBot
from telebot.custom_filters import AdvancedCustomFilter
from API_Tokens import *
from Contactinfo import *



products_factory = CallbackData('product_id', prefix='products')


def year1_keyboard():
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text=subject['name'],
                    callback_data=products_factory.new(product_id=subject["id"])
                )
            ]
            for subject in year1
        ]
    )

def year2_keyboard():
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text=subject['name'],
                    callback_data=products_factory.new(product_id=subject["id"])
                )
            ]
            for subject in year2
        ]
    )

def year3_keyboard():
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text=subject['name'],
                    callback_data=products_factory.new(product_id=subject["id"])
                )
            ]
            for subject in year3
        ]
    )

def year4_keyboard():
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text=subject['name'],
                    callback_data=products_factory.new(product_id=subject["id"])
                )
            ]
            for subject in year4
        ]
    )
def year5_keyboard():
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text=subject['name'],
                    callback_data=products_factory.new(product_id=subject["id"])
                )
            ]
            for subject in year5
        ]
    )
def year6_keyboard():
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text=subject['name'],
                    callback_data=products_factory.new(product_id=subject["id"])
                )
            ]
            for subject in year6
        ]
    )

def dean_keyboard():
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text=subject['name'],
                    callback_data=products_factory.new(product_id=subject["id"])
                )
            ]
            for subject in dean
        ]
    )

class SubjectsCallbackFilter(AdvancedCustomFilter):
    key = 'config'

    def check(self, call: types.CallbackQuery, config: CallbackDataFilter):
        return config.check(query=call)
