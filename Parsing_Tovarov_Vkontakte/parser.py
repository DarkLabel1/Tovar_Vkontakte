import requests
import csv
import time

def vsego_1000_products(id_1):
    token = '16f938c21d1c8c373ee5c7b6ea6c06faabb74728fbc6a86365d80470f103f1117efbed4b2f1a17ff06a56'
    owner_id = id_1
    count = 100
    offset = 0
    version = 5.101
    all_market = []
    while offset < 1000:
        response = requests.get('https://api.vk.com/method/market.get',
        params={
            'access_token': token,
            'owner_id': owner_id,
            'count': count,
            'offset': offset,
            'v': version
        })
        data = response.json()['response']['items']
        offset += 100
        time.sleep(0.5)
        all_market.extend(data)
    return all_market

def file_write(data):
    with open('Result\ ' + nazvanie + '.csv', 'w', newline='') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('Название', 'Цена', 'Фото', 'Дата'))
        for market in data:
            f = time.ctime(market['date'])
            a_pen.writerow((market['title'], market['price']['text'], market['thumb_photo'], f))


lin = input('Вставьте ссылку: ')
text = lin.split('-')
id_link = text[1]
id_1 = '-' + id_link

all_market = vsego_1000_products(id_1)
nazvanie = input('Введите название:')
file_write(all_market)

print('Выполнено.')
