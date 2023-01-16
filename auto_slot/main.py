from config import *

import requests as req
from time import sleep
from random import randint
from secrets import token_hex as token

from colorama import Fore, Style
from colorama import init
init()



def print_logo():
    print(Fore.YELLOW + Style.BRIGHT + "             _               _     _  __ _")
    print("  __ _ _   _| |_ ___     ___| |__ (_)/ _| |_ ___ _ __")
    print(" / _` | | | | __/ _ \   / __| '_ \| | |_| __/ _ \ '__|")
    print("| (_| | |_| | || (_) |  \__ \ | | | |  _| ||  __/ |")
    print(" \__,_|\__,_|\__\___/___|___/_| |_|_|_|  \__\___|_|")
    print("                   |_____| ")
    print(Style.RESET_ALL)

def take_pause():
    pass

def take_shift(start_time, end_time):

    if DEBUG_PRINT:
        print(Fore.GREEN + Style.BRIGHT + f'[…] Запускаю подбор слотов {start_time[11:16]}-{end_time[11:16]} на {start_time[5:7]}.{start_time[8:10]}.{start_time[:4]}' + Style.RESET_ALL)

    success = False

    while not success:

        headers = {"Host": "ctt.eda.yandex",
                    "Authorization": f"Bearer {TOKEN}",
                    "X-App-Version": APP_VERSION,
                    "Content-Type": "application/json; charset=UTF-8",
                    "Content-Length": "285",
                    "Accept-Encoding": "gzip, deflate",
                    "User-Agent": "okhttp/4.3.1",
                    "Connection": "close"}
        # print(headers)

        json = {"id": f"{token(4)}-{token(2)}-{token(2)}-{token(2)}-{token(6)}",
                  "items": [
                                {"id": f"{token(4)}-{token(2)}-{token(2)}-{token(2)}-{token(6)}",
                                "startsAt": start_time,
                                "endsAt": end_time,
                                "startPointId": START_POINT_ID,
                                "startLocationId": START_LOCATION_ID}
                            ]
                }
        # print(json)

        resp = req.post("https://ctt.eda.yandex/courier-shifts/", headers=headers, json=json)
        # print(resp.status_code)

        if resp.status_code == 204: # слот успешно забронирован
            print(Fore.BLUE + Style.BRIGHT + "[#] Слот успешно забронирован!" + Style.RESET_ALL)
            success = True

        elif resp.status_code == 400: # ошибка при бронировании слота
            print(Fore.RED + Style.BRIGHT + "[!] Ошибка 400: " + resp.json()['errors'][0]['attributes']['title'] + Style.RESET_ALL)
            # print("[!] Ошибка: ")
            success = True

        elif resp.status_code == 401: # не удалось войти в аккаунт
            print(Fore.RED + Style.BRIGHT + "[!] Ошибка 401: " + resp.json()['errors'][0]['attributes']['title'] + Style.RESET_ALL)
            print(Fore.YELLOW + Style.BRIGHT + "[…] Пробую ещё раз..." + Style.RESET_ALL)
            sleep(randint(3, 6))

        elif resp.status_code == 403: # доступ запрещён (очень редко)
            # print(Fore.RED + Style.BRIGHT + "[!] Ошибка: " + resp.json()['errors'][0]['attributes']['title'] + Style.RESET_ALL)
            print(Fore.RED + Style.BRIGHT + "[!] Ошибка 403: Доступ запрещён" + Style.RESET_ALL)
            print(Fore.RED + Style.BRIGHT + "[*] DEBUG:" + resp.text + Style.RESET_ALL)
            success = True



if DEBUG_PRINT:
    print_logo()

# for i in range(2):
#     take_shift(f"2021-05-0{i+1}T10:00:00+03:00", f"2021-05-0{i+1}T16:00:00+03:00")
#     take_shift(f"2021-05-0{i+1}T16:00:00+03:00", f"2021-05-0{i+1}T22:00:00+03:00")
