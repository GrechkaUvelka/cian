# поменял структуру таблицы
# циан не предоставляет координаты. необходмо получать их через доп. сервисы
# парсил только flatsale
# добавил дату объявления и ссылку для удобства

from bs4 import BeautifulSoup as bs
import re
import codecs
from consts import *
from dbfunctions import *
from parsefunctions import *

connect('offers.db')#создаем бд если ее нет

while True:
    body_html = codecs.decode(request())
    soup = bs(body_html, 'html.parser')
    cards = soup.find_all(attrs={'data-name': 'CardComponent'})
    page += 1
    for i in cards:
        # ищем id
        offer_id = i.find(attrs={'href': re.compile(r'cian.ru/sale/')})
        url = str(offer_id.attrs['href'])
        offer_id = str(offer_id.attrs['href'][-10:-1])

        # из заголовка получаем кол-во комнат, площадь, этаж
        title_prev = i.find(attrs={'data-mark': 'OfferTitle'})
        title = title_prev.span.text

        room_count = title[:title.find(',')]

        area = title[title.find(',') + 2:title.find('м²') + 2]

        floor = title[title.find('²') + 3:title.find(' этаж')]

        # ищем дату
        offer_date = i.find(attrs={'data-name': 'TimeLabel'})
        offer_date = offer_date.select('div:nth-of-type(2)')
        offer_date = offer_date[0].text

        # форматурием дату
        if offer_date[:offer_date.find(',')] in day_options:    # если формат 'вчера', 'сегодня'
            offer_date = day_options[offer_date[:offer_date.find(',')]]
        else:   # если формат 'месяц день'
            date_buffer = offer_date[:offer_date.find(',')]
            month = months[date_buffer.split()[1]]
            day = date_buffer.split()[0]
            offer_date = '{}-{}-{}'.format(str(year), month, day)

        address_prev = i.find_all(attrs={'data-name': 'GeoLabel'})
        address = ''
        for j in address_prev:
            address += j.text + ' '

        price = i.find(attrs={'data-mark': 'MainPrice'})
        price = price.span.text[:-2]

        now = datetime.now()
        parse_date = now.strftime("%Y-%m-%d, %H:%M:%S")
        values_to_db = []
        values_item = (offer_id, price, room_count, area, floor, offer_date, parse_date, address, url)
        values_to_db.append(values_item)
        print(values_to_db)
        write_db(values_to_db)
