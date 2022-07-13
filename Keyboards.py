from telebot.callback_data import CallbackData, CallbackDataFilter
from telebot import types, TeleBot
from telebot.custom_filters import AdvancedCustomFilter
from API_Tokens import *
from Contactinfo import *



products_factory = CallbackData('product_id', prefix='products')


class Keyboard:
    def year1():
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

    def year2():
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

    def year3():
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

    def year4():
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
    def year5():
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
    def year6():
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
