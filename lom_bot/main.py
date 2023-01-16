# coding: utf-8

from func import *

import os
import traceback
from datetime import datetime, timedelta

import telebot
from telebot import types
from forex_python.converter import CurrencyRates
from apscheduler.schedulers.background import BackgroundScheduler

BOT_TOKEN = '12345:token'

##########################

def send_messages():

    try:

        currency = CurrencyRates()
        pre_date = datetime.now() - timedelta(days=1)
        date = datetime(pre_date.year, pre_date.month, pre_date.day, 18, 30)

        try:
            currency_text = get_currency_text(currency, date)
        except:
            currency_text = None

        try:
            lme_data_text, y_axis_arr = get_lme_data_text(currency, date, 'lead')
            create_graphic(y_axis_arr)
        except:
            lme_data_text = None

        try:
            # comp_prices = get_comp_prices(['ferratek', 'ugmet', 'taz', 'energomet', 'intermet', 'forsage', 'ferrokom', 'metnadonu'])
            comp_prices = get_comp_prices(['ferratek', 'taz', 'energomet', 'forsage', 'metnadonu'])
            comp_data_text = get_comp_data_text('lead', comp_prices)
        except:
            comp_data_text = None

        users_list = get_users_list()
        success_count = 0
        errors_count = 0
        for chat_id in users_list:
            # if int(chat_id[0]) == 1832920700:
            #     continue
            try:
                if currency_text:
                    bot.send_message(chat_id[0], currency_text)
                if lme_data_text:
                    with open('img/graphic.png', 'rb') as graphic_img:
                        bot.send_photo(chat_id[0], graphic_img, caption=lme_data_text)
                if comp_data_text:
                    bot.send_message(chat_id[0], comp_data_text)
                success_count += 1
            except Exception as e:
                bot.send_message(-635343434, f"Не удалось отправить сообщение юзеру!\nID: {chat_id[0]}\n\n{e.__class__}\n{e}")
                errors_count += 1

        os.remove("img/graphic.png")

        result_msg_text = f"""Рассылка была успешна отправлена!
Получило рассылку: {success_count} юзеров
Не получило: {errors_count} юзеров"""
        bot.send_message(-635343434, result_msg_text)

        prices_msg_text = f'Данные по текущей рассылке:\n\n'
        for dict_key in comp_prices.keys():
            prices_msg_text += f'{dict_key}: {comp_prices[dict_key]}\n'
        bot.send_message(-635343434, prices_msg_text)

        bot.send_message(-635343434, '===')

    except Exception as e:

        now_is = datetime.now()

        with open('error_log.txt', 'a') as log_file:
            log_file.write(f'===\nERROR WHILE SENDING MESSAGES\nTime: {now_is}\nError class: {e.__class__}\n{e}\n')

        with open(f'msgsend_traceback_{now_is.second}.txt', 'a') as log_file:
            log_file.write(traceback.format_exc())
            bot.send_message(-635343434, f'Error!\nTime: {now_is}\n\n{traceback.format_exc()}\n===\n')

##########################

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_messages, 'cron', day_of_week='mon-fri', hour=9, minute=29)
    scheduler.add_job(send_messages, 'cron', day_of_week='mon-fri', hour=15, minute=29)
    scheduler.start()

    bot = telebot.TeleBot(BOT_TOKEN)

    @bot.message_handler(commands=['start'])
    def start_command(message):
        if message.chat.id < 0: return 0 # если сообщение из чата, не отвечаем
        add_user(message.chat.id, message.from_user.username, message.from_user.first_name)
        bot.send_message(message.chat.id, f'Добро пожаловать, {message.from_user.first_name}!')

    print('Бот запущен! Нажмите Ctrl+Break для выхода')

    try:
        bot.polling()

    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

    except Exception as e:
        with open('error_log.txt', 'a') as log_file:
            log_file.write(f'===\nERROR WHILE POLLING\nTime: {datetime.now()}\nError class: {e.__class__}\n{e}\n')
