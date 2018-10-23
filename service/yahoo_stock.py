import os
from bs4 import BeautifulSoup as bs
import lxml
import urllib.request as urlRequest
import time
import re
import datetime
import ssl


def prey():
    ssl._create_default_https_context = ssl._create_unverified_context
    url = "https://info.finance.yahoo.co.jp/ranking/"
    list_save = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    prey_request = urlRequest.Request(url, headers=headers)
    prey_page = urlRequest.urlopen(prey_request).read().decode('utf8')
    beautiful_soup_entity = bs(prey_page, 'lxml')
    # print(beautiful_soup_entity)
    list_save = beautiful_soup_entity.find_all(class_='rankingTabledata yjM')
    return list_save


def save_data(list_save):
    save_data_list = []
    for x in list_save:
        number = x.find_all(class_='txtcenter')[0].string
        market = x.find_all(class_='txtcenter yjSt')[0].string
        stock_name = x.find_all(class_='normal yjSt')[0].string
        stock_time = x.find_all(class_='txtcenter grey yjSt')[0].string
        stock_value = x.find_all(class_='txtright bold')[0].string
        stock_green_fin = x.find_all(class_='greenFin')[0].string
        stock_green_fin_2 = x.find_all(class_='greenFin')[1].string
        exp = x.find_all(class_='txtright')[3].string
        save_data_list.append(number)  # 順位
        save_data_list.append(market)  # 市場
        save_data_list.append(stock_name)  # 名称
        save_data_list.append(stock_time)
        save_data_list.append(stock_value)  # 取引値
        save_data_list.append(stock_green_fin)
        save_data_list.append(stock_green_fin_2)  # 前日比
        save_data_list.append(exp)  # 出来高
    return save_data_list
