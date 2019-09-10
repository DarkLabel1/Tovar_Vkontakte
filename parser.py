import requests
import csv
import time

def vsego_1000_products(id_1):
    token = 'e6a9c599e7d326c63ec2b0f6dc4f94330407aa86a67b1a41e43964904c12ebff4cad9394bfd17f0d2cc43'
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
    with open('Result\'' + nazvanie + '.csv', 'w', newline='') as file:
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
