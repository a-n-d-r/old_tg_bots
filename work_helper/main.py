import os, glob, subprocess
from random import randint
from time import sleep

# куда сохранять скрин
screenshot_path = '/path/to/screenshot.png'

import telebot
from telebot import types
bot = telebot.TeleBot('12345:token')

# id админов списком
chat_ids_list = [123, 456]

###################################

while True:

    # удаляем старые скрины по маске
    fileList = glob.glob(screenshot_path.replace('screenshot', '*'))
    for filePath in fileList:
        try:
            os.remove(filePath)
        except:
            print("Error while deleting file : ", filePath)

    # делаем новый скрин
    subprocess.run(f'flameshot full --path {screenshot_path}',
        shell=True, check=True,
        executable='/bin/bash')

    # отправляем скрин в телегу
    for chat_id in chat_ids_list:
        with open(screenshot_path, 'rb') as photo:
            bot.send_photo(chat_id, photo)

    # ждём 15-30 минут
    sleep_time = randint(15,30) * 60 # минуты в секунды
    sleep(sleep_time)
