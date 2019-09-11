from PySide import QtCore, QtGui
import sys
from mainwindow import Ui_MainWindow
import webbrowser
import requests
import csv
import time

#Create application
app = QtGui.QApplication(sys.argv)
#Create form and init ui
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
#Hook logic

def token_sayt():
	webbrowser.open('https://oauth.vk.com/authorize?client_id=6121396&scope=market&response_type=token')

ui.pushButton_2.clicked.connect(token_sayt)

def Start():
	token = ui.lineEdit.text()
	link_market = ui.lineEdit_2.text()
	#nazvanie_marketa = ui.lineEdit_3.text()
	vsego_1000_products(token, link_market)
	#file_write(nazvanie_marketa)

def vsego_1000_products(token, link_market):
	print(token)
	print(link_market)
	link = link_market.split('-')
	id_link = link[1]
	id_1 = '-' + id_link
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
		print(data)
		offset += 100
		time.sleep(0.5)
		all_market.extend(data)
		print(all_market)
	file_write(all_market)

def file_write(data):
	nazvanie_marketa = ui.lineEdit_3.text()
	print(nazvanie_marketa)
	puty = 'Result\\' + nazvanie_marketa + '.csv'
	print(puty)
	with open(puty, 'w', newline='') as file:
		a_pen = csv.writer(file)
		a_pen.writerow(('Название', 'Цена', 'Фото', 'Дата'))
		for market in data:
			f = time.ctime(market['date'])
			a_pen.writerow((market['title'], market['price']['text'], market['thumb_photo'], f))
	print('Выполненно.')

ui.pushButton_3.clicked.connect(Start)

#Run main loop
sys.exit(app.exec_())
