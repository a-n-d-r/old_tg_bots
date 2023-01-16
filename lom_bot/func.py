# coding: utf-8

import os
import sqlite3
import calendar
from datetime import datetime, timedelta

import matplotlib.pyplot as plt

import requests as req
from bs4 import BeautifulSoup as bs

##########################

def get_currency_text(currency, date):
    rates = get_rates_from_db()
    usd_rate = '{:.2f}'.format(currency.get_rates('USD', date)['RUB'])
    eur_rate = '{:.2f}'.format(currency.get_rates('EUR', date)['RUB'])
    cny_rate = '{:.2f}'.format(currency.get_rates('CNY', date)['RUB'])
    usd_change = float(usd_rate) - float(rates[0])
    eur_change = float(eur_rate) - float(rates[1])
    cny_change = float(cny_rate) - float(rates[2])
    update_rates_to_db(usd_rate, eur_rate, cny_rate)
    text = f"""
Курсы валют на 18:30, {date.day:02d}.{date.month:02d}.{date.year}

Курс USD к RUB:
1 Доллар США = {float(usd_rate):.2f} ({usd_change:+.2f}) руб.
Курс EUR к RUB:
1 Евро = {float(eur_rate):.2f} ({eur_change:+.2f}) руб.
Курс CNY к RUB:
1 Китайский Юань = {float(cny_rate):.2f} ({cny_change:+.2f}) руб."""
    return text

def get_lme_data_text(currency, date, metal):
    if metal == 'lead':
        resp = req.get("https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Pb_cash")
    else:
        return None, None
    text = "Цена на свинец (тыс. руб.) :\n\n"
    html = bs(resp.text, "html.parser")
    abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}
    usd_course = currency.get_rates('USD', date)['RUB']
    y_axis_arr = []
    lme_dates_list = html.select(f'div.section > a#y{date.year:04d}+h2+div+table > tbody > tr:not(.shaded) > td:nth-child(1)')
    lme_usd_prices_list = html.select(f'div.section > a#y{date.year:04d}+h2+div+table > tbody > tr:not(.shaded) > td:nth-child(2)')
    for i in range(4, -1, -1):
        lme_date = lme_dates_list[i].text
        lme_usd_price = lme_usd_prices_list[i].text
        lme_usd_price_float = float(lme_usd_price.replace(',', ''))
        date_day = int(lme_date.split(' ')[0].replace('.', ''))
        date_month = int(abbr_to_num[lme_date.split(' ')[1][:3]])
        date_year = int(lme_date.split(' ')[2])
        lme_rub_price = usd_course * lme_usd_price_float
        text += f"{date_day:02d}.{date_month:02d}.{date_year:04d} – {float(lme_rub_price/1000):.1f}\n"
        y_axis_arr.append(int(lme_usd_price_float))
    return text, y_axis_arr

def get_comp_data_text(metal, comp_prices):
    current_time = datetime.now()
    today_date = datetime.today()
    monday_date = today_date - timedelta(days=today_date.weekday())
    sunday_date = today_date + timedelta(days=4-today_date.weekday())

    plus_day_id = 5 if current_time.hour > 13 else 0
    if today_date.isoweekday() > 1:
        current_day_id = ( today_date.isoweekday() * 10 ) + plus_day_id
    else:
        current_day_id = 10 + plus_day_id

    write_comp_data_to_db(metal, current_day_id, comp_prices)

    if today_date.isoweekday() > 1:
        last_day_id = ( today_date.isoweekday() * 10 ) - 5
    else:
        last_day_id = 10
    daily_change_count = get_price_changes_count(metal, last_day_id)
    period_change_count = get_price_changes_count(metal, 5)
    daily_change_percent = daily_change_count / len(comp_prices)
    period_change_percent = period_change_count / len(comp_prices)

    daily_min, daily_max = get_price_changes_count(metal, last_day_id, func_return = 'min_max')
    period_min, period_max = get_price_changes_count(metal, 5, func_return = 'min_max')

    double_count = get_price_changes_count(metal, last_day_id, func_return = 'double')
    double_increase_text = '\nПовторное повышение' if double_count > 0 else ''

    text = f"""Свинец:ЦФО

Дата: {today_date.day:02d}.{today_date.month:02d} {double_increase_text}
Изменение цен – {percent_to_text( int(daily_change_percent * 100) )}
Максимальное изменение цены – +{daily_max:.2f} руб.; -{daily_min:.2f} руб.

За период: {monday_date.day:02d}.{monday_date.month:02d} - {sunday_date.day:02d}.{sunday_date.month:02d}
Изменение цен – {percent_to_text( int(period_change_percent * 100) )}
Максимальное изменение цены – +{period_max:.2f} руб.; -{period_min:.2f} руб."""

    if current_day_id == 55:
        delete_comp_data_from_db(metal)

    return text

##########################

def create_graphic(y_axis_arr):
    try:
        os.remove('img/graphic.png')
    except Exception as e:
        print(f"Ошибка при удалении графика!\nКод ошибки: {e.strerror}\n")
    plt.clf()
    plt.plot([1,2,3,4,5], y_axis_arr, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=False) # labels along the bottom edge are off
    plt.xlabel("Цены на графике указаны в долларах США")
    plt.savefig('img/graphic.png', bbox_inches='tight')
    plt.clf()

def percent_to_text(percent):
    percent = int(percent)
    if percent == 0:
        return "изменений нет"
    elif percent > 0 and percent <= 15:
        return "еденичное"
    elif percent >= 16 and percent <= 30:
        return "незначительное"
    elif percent >= 31 and percent <= 49:
        return "ощутимое"
    elif percent >= 50:
        return "значительное"

def get_comp_prices(companies_arr):
    prices = {}
    for company in companies_arr:
        try:
            if company == 'ferratek':
                resp = req.get("https://www.ferratek.com/price")
                html = bs(resp.text, "html.parser")
                html2 = html.select('div.pagecontent > section.import-price > div.item:nth-child(34)')[0]
                price = html2.select('div.itemContent > div.priceContent > div.priceBlock > div.priceValue')[0].text
                prices.update({ company : float( price.split(' ')[0].replace(',', '.') ) })
            elif company == 'ugmet':
                resp = req.get("http://lom.ugmet.ru/we-buy/batteries-white#/price-list/to-rub")
                html = bs(resp.text, "html.parser")
                price = html.select('tr.group-8 > td:nth-child(2) > span.price-rub')[0].text
                if int( price.replace(' ', '') ) > 1000:
                    prices.update({ company : int(price) / 1000 })
                else:
                    prices.update({ company : int(price) })
            elif company == 'taz':
                resp = req.get("http://tyumen-battery.ru/107")
                html = bs(resp.text, "html.parser")
                price = html.select('td.body_text_main > table > tbody > tr:nth-child(3) > td:nth-child(2)')[0].text
                prices.update({ company : int( price.split(',')[0].replace(' ', '') ) / 1000 })
            elif company == 'energomet':
                resp = req.get("https://akb-moscow.ru/utilizaciya-akkumulyatorov-bu-v-moskve/")
                html = bs(resp.text, "html.parser")
                html2 = html.select('div.entry-content > div.textwidget')[1]
                price = html2.select('table > tbody > tr:nth-child(4) > td:nth-child(2) > p > span > strong')[0].text
                prices.update({ company : float(price) })
            elif company == 'intermet':
                resp = req.get("https://www.metallolom-lom-spb.ru/lom-akkumuljatorov/lom-akkumulyatorov.html")
                html = bs(resp.text, "html.parser")
                price = html.select('div.s_price-table-overflow > table > tr:nth-child(2) > td:nth-child(5) > span')[0].text
                prices.update({ company :  int( price.strip() ) / 1000 })
            elif company == 'forsage':
                resp = req.get("http://formetall.ru/index.php/price/zena-na-zvetnoy-lom")
                html = bs(resp.text, "html.parser")
                price = html.select('tr.row45 > td.dtc1')[0].text
                prices.update({ company : float(price) })
            elif company == 'ferrokom':
                resp = req.get("https://f-vm.ru/index.php?q=price")
                html = bs(resp.text, "html.parser")
                price = html.select('div.single-article > table.cvet_table > tr:nth-child(54) > td.price3 > span')[0].text
                prices.update({ company : float( price.replace(',', '.') ) })
            elif company == 'metnadonu':
                resp = req.get("https://metall-na-dony.ru/uslugi/tsvetnoj-metall/")
                html = bs(resp.text, "html.parser")
                price = html.select('table#tablepress-2 > tbody > tr.row-31.odd > td.column-5')[0].text
                prices.update({ company : float(price) })
        except:
            pass
    return prices

def find_dict_differ(current_dict, past_dict, search = 'changed'):
    if not current_dict or not past_dict:
        return {}
    elif current_dict == past_dict:
        return {}

    set_current, set_past = set(current_dict.keys()), set(past_dict.keys())
    intersect = set_current.intersection(set_past)

    if search == 'changed':
        return set(o for o in intersect if past_dict[o] != current_dict[o])
    elif search == 'increased':
        return set(o for o in intersect if past_dict[o] > current_dict[o])

def get_price_changes_count(metal, last_day_id, func_return = 'count'):
    data = read_comp_data_from_db(metal)
    changes_list = []

    for i in range(len(data)):
        first_dict = eval(data[i][1]) if data[i][1].startswith('{') else False
        if first_dict:
            break

    entries_arr = []
    for entry in data:
        entry_dict = eval(entry[1]) if entry[1].startswith('{') else False
        changes_list += find_dict_differ(first_dict, entry_dict)
        entries_arr.append(entry_dict)
        if entry[0] <= last_day_id:
            break

    if func_return == 'double':
        try:
            inc1 = find_dict_differ(entries_arr[1], entries_arr[0], search = 'increased')
            inc2 = find_dict_differ(entries_arr[2], entries_arr[1], search = 'increased')
            inc_list = list(inc1) + list(inc2)
            if len(inc_list) > len( list( set(inc_list) ) ):
                return len(inc_list) - len( list( set(inc_list) ) )
            else:
                return 0
        except:
            return 0

    if func_return == 'min_max':
        min_dict = first_dict.copy()
        max_dict = first_dict.copy()
        for entry in reversed(entries_arr):
            for dict_key in entry.keys():
                if entry[dict_key] < min_dict[dict_key]:
                    min_dict.update({dict_key: entry[dict_key]})
                if entry[dict_key] > max_dict[dict_key]:
                    max_dict.update({dict_key: entry[dict_key]})
        lowest_arr = []
        highest_arr = []
        for dict_key in first_dict.keys():
            lowest_arr.append(entries_arr[-1][dict_key] - min_dict[dict_key])
            highest_arr.append(max_dict[dict_key] - entries_arr[-1][dict_key])
        return max(lowest_arr), max(highest_arr)

    changes_count = len(set(changes_list)) if changes_list else 0
    return changes_count

##########################

def add_user(chat_id, username, name):
    conn = sqlite3.connect('db/users.db')
    cursor = conn.cursor()
    # try:
    #     cursor.execute('CREATE TABLE users (chat_id integer, username text, name text)')
    #     print("База была успешно создана!")
    # except:
    #     print("База уже создана!")
    cursor.execute(f"SELECT * FROM users WHERE chat_id like {chat_id}")
    row = cursor.fetchone()
    # print(row)
    if str(type(row)) == "<class 'NoneType'>":
        print(f'Пользователь [id:{chat_id}, @{username}] не найден в базе - cоздаю запись')
        cursor.execute(f"INSERT INTO users (chat_id, username, name) VALUES ('{chat_id}','@{username}','{name}')")
        conn.commit()
    cursor.close()
    conn.close()

def get_users_list():
    conn = sqlite3.connect('db/users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT chat_id FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

def update_rates_to_db(usd_rate, eur_rate, cny_rate):
    conn = sqlite3.connect('db/rates.db')
    cursor = conn.cursor()
    # try:
    #     cursor.execute('CREATE TABLE rates (usd_rate text, eur_rate text, cny_rate text)')
    #     print("База была успешно создана!")
    # except:
    #     print("База уже создана!")
    cursor.execute(f"UPDATE rates SET usd_rate = '{usd_rate}'")
    cursor.execute(f"UPDATE rates SET eur_rate = '{eur_rate}'")
    cursor.execute(f"UPDATE rates SET cny_rate = '{cny_rate}'")
    conn.commit()
    cursor.close()
    conn.close()

def get_rates_from_db():
    conn = sqlite3.connect('db/rates.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM rates")
    rates = cursor.fetchone()
    cursor.close()
    conn.close()
    return rates

def write_comp_data_to_db(metal, day_id, data):
    conn = sqlite3.connect(f'db/metals/{metal}.db')
    cursor = conn.cursor()
    # try:
    #     cursor.execute(f'CREATE TABLE {metal} (day_id integer, data text)')
    #     print(f"База {metal} была успешно создана!")
    # except:
    #     print(f"База {metal} уже создана!")
    cursor.execute(f"INSERT INTO {metal} (day_id, data) VALUES ('{day_id}',\"{data}\")")
    conn.commit()
    cursor.close()
    conn.close()

def delete_comp_data_from_db(metal):
    conn = sqlite3.connect(f'db/metals/{metal}.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {metal} WHERE day_id < 55")
    conn.commit()
    cursor.execute(f"UPDATE {metal} SET day_id = 5 WHERE day_id = 55")
    conn.commit()
    cursor.close()
    conn.close()

def read_comp_data_from_db(metal):
    conn = sqlite3.connect(f'db/metals/{metal}.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {metal} ORDER BY day_id DESC")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data
