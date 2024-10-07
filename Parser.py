from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import lxml

from telethon import TelegramClient, events, sync, connection
from telethon.tl.functions.users import GetFullUserRequest #для полных данных пользователя, в т.ч. "О себе"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from datetime import datetime

import requests
import time

import csv
import json

































# #от некуй делать написал парсер gismeteo с выводом погоды в телеграм
# api_id = 92
# api_hash = 'a5'
# try:
#     url='https://www.gismeteo.by/weather-mogilev-4251/now/'
#     ua = UserAgent()
#     fake_ua = {'user-agent': ua.random, }
#     response = requests.get(url=url, headers=fake_ua)
#
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     time_update = soup.find('div', class_='now-localdate').text
#     temp = soup.find('div', class_='now-weather').find_all('temperature-value')
#     temp2 = [x['value'] for x in temp]
#     temperature = temp2[0]
#     weather = soup.find('div', class_='now-desc').text
#     result = (f'В Могилеве:\n'
#               f'{time_update},\n'
#               f'{weather}, \n'
#               f'Температура: {temperature} гр.')
#     client = TelegramClient('session_name', api_id, api_hash)
#     client.start()
#     client.send_message('@vikakrutova', result)
#     time.sleep(3600)
# except:
#     pass



'''#отправка сообщений пидорам
api_id = 92
api_hash = 'a5'

with TelegramClient('session_name', api_id, api_hash) as client:
    client.send_message('@Unoquatr', 'Соболезную')
    for x in range(30):
        client.send_message('@Unoquatr', 'Пидор')'''



# #выдергиваем из последних 5 сообщений никнеймы отправителей
# api_id = 92
# api_hash = 'a5'
#
# with TelegramClient('session_name', api_id, api_hash) as client:
#     client.start()
#     all_messages = client.get_messages('https://t.me/Parsinger_Telethon_Test', 5) #собираем с паблика сообщения в количестве 5 штук (от последнего написанного и выше)
#     for message in all_messages: #перебираем полученные пять сообщений
#         id_user = message.from_id.user_id #выдергиваем из сообщений user_id в виде цифр
#         print(client.get_entity(id_user).username) #через get_entity получаем объект User с таким user_id, а из него дергаем его никнейм



'''#парсим поле "О себе" участников группы (этот мудила (создатель курса) уже в ПЯТЫЙ раз дал нерабочий код (пришлось фиксить)
api_id = 92
api_hash = 'a5'

with TelegramClient('session_name', api_id, api_hash) as client:
    client.start()
    users = client.get_participants('https://t.me/Parsinger_Telethon_Test')
    for user in users:
        user_full_about = client(GetFullUserRequest(user))
        print(user_full_about.full_user.about)'''



# #сохраняем все фотографии всех профилей в группе (в четвертый раз пример кода - не работает)
# api_id = 92
# api_hash = 'a5'
#
# with TelegramClient('session_name', api_id, api_hash) as client:
#     client.start()
#     participants = client.get_participants('https://t.me/Parsinger_Telethon_Test')
#     for user in participants:
#         for photos in client.iter_profile_photos(user):
#             client.download_media(photos, file=f'images/')



'''#сохраняем основные фотографии всех профилей в группе (в третий раз пример кода не работает)
api_id = 92
api_hash = 'a5'

with TelegramClient('session_name', api_id, api_hash) as client:
    client.start()
    participants = client.get_participants('https://t.me/Parsinger_Telethon_Test')
    for i, user in enumerate(participants):
        client.download_profile_photo(user, f'images/i', download_big=True)'''


# #получаем данные пользователей группы тг (в цикле for только имена) P.S. get_participants работает только с группами до 4.000 человек
# api_id = 92
# api_hash = 'a5'
#
# client = TelegramClient('session_name', api_id, api_hash)
# client.start()
#
# participants = client.get_participants('https://t.me/Parsinger_Telethon_Test')
#
# print(participants)
## for item in participants:
##     print(item.first_name, item.last_name)



'''with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/1/index.html')
    element = WebDriverWait(browser, 10, poll_frequency=0.5).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    #присвоили WebDriverWait переменной element, указали экземпляр browser, время ожидания, частоту проверок (0.5 сек), пока через неявное ожидание не стала активной кнопка btn, после чего на нее кликнули 
    print(browser.find_element(By.ID, 'result').text)
    #после клика по кнопке на экране появляется текст в лейбле 'result' который мы вывели в консоль'''



# #итерация по вкладкам но с какого-то лысого код работает в порядке 2, 1, 3, 4 и без reversed - 4, 3, 1, 2
# with webdriver.Chrome() as browser:
#     browser.execute_script('window.open("http:parsinger.ru/blank/2/1.html", "_blank1");')
#     browser.execute_script('window.open("http:parsinger.ru/blank/2/2.html", "_blank2");')
#     browser.execute_script('window.open("http:parsinger.ru/blank/2/3.html", "_blank3");')
#     browser.execute_script('window.open("http:parsinger.ru/blank/2/4.html", "_blank4");')
#
#     for x in reversed(range(len(browser.window_handles))):
#         browser.switch_to.window(browser.window_handles[x])
#         time.sleep(3)
#         for y in browser.find_elements(By.CLASS_NAME, 'check'):
#             y.click()



'''#скролинг страниц через JS
chrome_options = webdriver.ChromeOptions()
url = 'https://parsinger.ru/scroll/1/'

with webdriver.Chrome(options=chrome_options) as browser:
    browser.maximize_window()
    browser.get(url)
    browser.execute_script('window.scrollBy(0, 5000)')
    time.sleep(3)
    browser.execute_script('window.scrollBy(0, 5000)')
    time.sleep(3)
    browser.execute_script('window.scrollBy(0, 5000)')
    browser.quit()'''


# #Та же дрочь, но не с XPATH, а как хотел автор курса, через CLASS_NAME, но также через ZIP в цикле FOR и без TRY/EXCEPT
# chrome_options = webdriver.ChromeOptions()
# url = 'https://parsinger.ru/selenium/1/1.html'
#
# with webdriver.Chrome(options=chrome_options) as browser:
#     browser.maximize_window()
#     browser.get(url)
#
#     find_input = browser.find_elements(By.CLASS_NAME, 'form')
#     input_list = ['Питонов', 'Скрипт', 'Бэкэндович', '20.02.1991', 'Нидерланды', 'gvanrossum@git.com']
#
#     for x, i in zip(find_input, input_list):
#         x.send_keys(i)
#
#     button = browser.find_element(By.XPATH, '//*[@id="btn"]')
#     button.click()
#     time.sleep(5)
#     browser.quit()





'''#Дрочь с XPATH. Пытался решить задачу, но получилось только этим способом.
try:
    chrome_options = webdriver.ChromeOptions()
    url = 'https://parsinger.ru/selenium/1/1.html'

    with webdriver.Chrome(options=chrome_options) as browser:
        browser.get(url)
        time.sleep(0.5)
        input_fn = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/input")
        input_fn.send_keys('Питонов')
        input_ln = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/input")
        input_ln.send_keys('Скрипт')
        input_patron = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[5]/input")
        input_patron.send_keys('Бэкендович')
        input_age = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[6]/input")
        input_age.send_keys('20.02.1991')
        input_city = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[7]/input")
        input_city.send_keys('Нидерланды')
        input_email = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[8]/input")
        input_email.send_keys('gvanrossum@git.com')
        button = browser.find_element(By.XPATH, '//*[@id="btn"]')
        button.click()
        time.sleep(10)
except Exception as _ex:
    pass'''



# #проверяем прокси и выводим на консоль работающие
# proxy_list = ['49.13.9.253:80',
#               '66.228.33.190:49117',
#               '193.26.157.224:80',
#               '92.204.40.109:14200',
#               '187.49.17.115:8080', ]
#
# for PROXY in proxy_list:
#     try:
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('--proxy-server=%s' % PROXY)
#         url = 'https://2ip.ru/'
#
#         with webdriver.Chrome(options=chrome_options) as browser:
#             browser.get(url)
#             print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#
#             browser.set_page_load_timeout(7)
#             proxy_list.remove(PROXY)
#     except Exception as _ex:
#         print(f'Превышен timeout ожидания для - {PROXY}')
#         continue



'''#запускаем браузер в selenium и открываем первую найденную ссылку
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless') #.add_extension('coordinates.crx') - расширение для встроенного хрома

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    a = browser.find_element(By.TAG_NAME, 'a') #никуя не объяснил за By.Tag_NAME
    print(a.get_attribute('href'))'''



# #здесь я спарсил json двумя способами, выведя колиство каждого товара на сайте
# url = 'http://parsinger.ru/downloads/get_json/res.json'
# resopnse = requests.get(url=url).json()
#
# count = []
# for item in resopnse:
#     count.append({item['categories']:int(item['count'])})
#
# watch_count = []
# mobile_count = []
# mouse_count = []
# hdd_count = []
# headphones_count = []
#
# # for x in count:
# #     try:
# #         watch_count.append(x['watch'])
# #     except KeyError:
# #             try:
# #                 mobile_count.append(x['mobile'])
# #             except KeyError:
# #                 try:
# #                     mouse_count.append(x['mouse'])
# #                 except KeyError:
# #                     try:
# #                         hdd_count.append(x['hdd'])
# #                     except KeyError:
# #                         headphones_count.append(x['headphones'])
# #######################################################################################################
# for x in count:
#     try:
#         watch_count.append(x['watch'])
#     except KeyError:
#         pass
# for x in count:
#     try:
#         mobile_count.append(x['mobile'])
#     except KeyError:
#         pass
# for x in count:
#     try:
#         mouse_count.append(x['mouse'])
#     except KeyError:
#         pass
# for x in count:
#     try:
#         hdd_count.append(x['hdd'])
#     except KeyError:
#         pass
# for x in count:
#     try:
#         headphones_count.append(x['headphones'])
#     except KeyError:
#         pass
# print('Часов всего: ', sum(watch_count))
# print('Телефонов всего: ', sum(mobile_count))
# print('Мышей всего: ', sum(mouse_count))
# print('Жестких дисков всего: ', sum(hdd_count))
# print('Наушников всего: ', sum(headphones_count))



'''#еще один пример выдергивания id 
response = requests.get(url='https://parsinger.ru/html/watch/1/1_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
description = soup.find('ul', id='description').find_all('li')
li_id = [x['id'] for x in description]
print(li_id)'''



# #собираем данные со страницы в формате json
# url = f'https://parsinger.ru/html/index4_page_1.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8-sig'
# soup = BeautifulSoup(response.text, 'lxml')
#
# name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
# description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')] #.split - разделить по плиткам (ячейкам/строчкам), .strip() - "раздеть", снять(удалить) лишнее (одежду(начало/окончание))    #.strip() удаляет пробелы перед и после x.text, а .split('\n') разделяет строку на несколько строк по параметру '\n', т.е. каждую новую строку одной строки делает новой строкой
# price = [x.text.strip(' руб') for x in soup.find_all('p', class_='price')] #.strip(' руб) добавил сам.
#
# result_json = []
#
# for list_item, price_item, name in zip(description, price, name): #итерация для переменных 1, 2, 3 в итерируемом объекте, который является ZIP'ом из трех объектов // три однотипные итерации мы объединили в одну кривую итерацию
#     result_json.append({
#         'name': name,
#         'brand': [x.split(':')[1] for x in list_item][0], #[0], [1], [2], [3] - порядковые номера строк в list_item (т.е. discription)
#         'type': [x.split(':')[1] for x in list_item][1],
#         'connect': [x.split(':')[1] for x in list_item][2],
#         'game': [x.split(':')[1] for x in list_item][3],
#         'price': price_item,
#     })
#
# with open('res.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)



'''#парс данных со всех страниц категории в csv файл с моей доработкой (указания в названии даты/времени создания)
file_name = datetime.now().strftime('%d.%m.%Y  %H_%M_%S')
with open(f'{file_name}.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Бренд', "Форм-фактор", 'Ёмкость', 'Объем буф. памяти', 'Цена'])


for x in range(1, 5):
    url = f'https://parsinger.ru/html/index4_page_{x}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8-sig'
    soup = BeautifulSoup(response.text, 'lxml')

    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
    price = [x.text for x in soup.find_all('p', class_='price')]

    for item, price, descr in zip(name, price, description):
        flatten = item, *[x.split(':')[1].strip() for x in descr if x], price

        file = open(f'{file_name}.csv', 'a', encoding='utf-8-sig', newline='')
        writer = csv.writer(file, delimiter=';')
        writer.writerow(flatten)

print('Файл res.csv создан')
file.close()'''




# #парс всех данных по мышам со страницы
# with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([
#         'Наименование', 'Цена', 'Бренд', "Тип", 'Подключение', 'Игровая'])
#
# url = 'https://parsinger.ru/html/index3_page_2.html'
#
# response = requests.get(url=url)
# response.encoding = 'utf-8-sig'
# soup = BeautifulSoup(response.text, 'lxml')
#
# name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
# description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
# price = [x.text for x in soup.find_all('p', class_='price')]
#
# for item, price, descr in zip(name, price, description):
#     flatten = item, price, *[x.split(':')[1].strip() for x in descr if x]
#
#     file = open('res.csv', 'a', encoding='utf-8-sig', newline='')
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(flatten)
# file.close()
# print('Файл res.csv создан')



'''with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file: #создаем файл res.csv
     writer = csv.writer(file, delimiter=';') #вписываем в него через ';' следующие названия столбцов
     writer.writerow([
         'Наименование', 'Артикул', 'Бренд', 'Модель',
         'Тип', 'Игровая', 'Размер', 'Подсветка', 'Разрешение',
         'Сайт производителя', 'В наличии', 'Цена'])

url='http://parsinger.ru/html/mouse/3/3_11.html'

response = requests.get(url=url)            #парсим сайт 
response.encoding = 'utf-8'                 
soup = BeautifulSoup(response.text, 'lxml')

# из нижеуказанных данных сайта выдергиваем текст и через split разделяем данные в строке разделителем ': ' (что делает [0] и [1] я хз 
name = soup.find('p', id='p_header').text
article = soup.find('p', class_='article').text.split(': ')[1]
brand = soup.find('li', id='brand').text.split(': ')[1]
model = soup.find('li', id='model').text.split(': ')[1]
type = soup.find('li', id='type').text.split(': ')[1]
purpose = soup.find('li', id='purpose').text.split(': ')[1]
light = soup.find('li', id='light').text.split(': ')[1]
size = soup.find('li', id='size').text.split(': ')[1]
dpi = soup.find('li', id='dpi').text.split(': ')[1]
site = soup.find('li', id='site').text.split(': ')[1]
in_stock = soup.find('span', id='in_stock').text.split(': ')[1]
price = soup.find('span', id='price').text.split(': ')[0]


# записываем в вышесозданный файл через 'a' парс-данные по следующему шаблону.  
with open('res.csv', 'a', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        name, article, brand, model,
        type, purpose, size, light, dpi,
        site, in_stock, price])'''



# #пример преобразования списка в csv-файл
# lst = ['one', 'two', 'three']
#
# with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file: #newline='' надо указывать, чтобы документ не "сползал". utf-8-sig нужен для правильной интерпритации файла Excel'ем (по умолчанию unicode).
#     writer = csv.writer(file, delimiter=';') #создали экземпляр класса и применили к нему метод writer(), у которого есть метод writerow().
#     writer.writerow(lst) #delimiter=';' #С помощью wiriterow()можно записывать список в соответствующий формат построчно.указывает разделитель между элементами списка


'''#задача на парс табличных данных с сайта и вывода на итог суммы УНИКАЛЬНЫХ значений из этой таблицы
url='https://parsinger.ru/table/1/index.html'
response = requests.get(url=url)
response.encoding = 'uthf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find('div', class_='main').find_all('td')
div_list = []
for x in div: #в каждой итерации
    div_list.append(x.text) #добавляем значение в список div_list  
uniq_div_list = set(div_list) #через set собираем их списка div_list в iniq_div_list  только уникальные значения
summa = list(map(float, uniq_div_list)) #переводитм список uniq_div_list в тип float из типа str
print(sum(summa)) #выводим на экран сумму получившегося float списка summa'''



# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
#     'x-requested-with': 'XMLHttpRequest', #F12, Сеть, Fetch/XHR, Название : GetSum?GiveName..., Заголовки, X-Requested-With: XMLHttpRequest.
# }
# data = {
#     'GiveName': "Monero",
#     'GetName': 'Dash',
#     'Sum': 100,
#     'Directtion': 0
# }
#
# url='https://bitality.cc/Home/GetSum?' #Обрезали URL, дальше вставим data
# response = requests.get(url=url, headers=headers, params=data).json() #в params вставили data
# print(response)



'''headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest', #F12, Сеть, Fetch/XHR, Название : GetSum?GiveName..., Заголовки, X-Requested-With: XMLHttpRequest.
}

url='https://bitality.cc/Home/GetSum?GiveName=Sberbank&GetName=Bitcoin&Sum=20000&Direction=0' #Тот же путь, что и сверху, но вверху Заголовков стоит правильный URL запроса.
response = requests.get(url=url, headers=headers).json() #AJAX работает с json() форматом.
print(response)'''


# #то же самое, но с созданием ссылок в list comprehension
# url='https://parsinger.ru/html/index1_page_1.html'
# response = requests.get(url=url)
# response.encoding = 'uthf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# shema = 'https://parsinger.ru/html/'
# pagen = [f'[{shema}{link['href']}' for link in soup.find('div', class_='pagen').find_all('a')]
# print(pagen)



'''#Выгоняем ссылки пагинации с сайта
url='https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'uthf-8'
soup = BeautifulSoup(response.text, 'lxml')
# pagen = soup.find('div', class_='pagen').find_all('a')
# #проходим циклом по классу пагинации и дергаем из нее непосредственно ссылки.
# list_link = []
# for link in pagen:
#     list_link.append(link['href'])
# #то же самое, но через list comprehension
pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
#переменная pagen состоит из итераций включающих только ссылки в цикле, где каждая итерация проходит по данным, полученным при поиске элементов супа.
print(pagen)'''




# #прикольная задача на парс всех ценников со страницы и вывода их суммы
# url='https://parsinger.ru/html/index1_page_1.html'
# response = requests.get(url=url)
# response.encoding = 'uthf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# div = soup.find_all('p', class_='price')
# result = []
# for x in div:
#     result.append(x.text)
# numbers = re.findall(r'\b\d+\b', str(result)) #вот этой еботой с 'import re' я переписал из списка result в список numbers только цифры (без 'руб')
# summa = list(map(int, numbers)) #вот этой еботой я перевел список str(numbers) в список int(summa)
# sum_of_numbers = sum(summa) #а вот этой еботой я сложил все элементы (цены) списка
# print(sum_of_numbers)

#-----------------------------------------------------------------------------------------------------


# url='https://parsinger.ru/html/headphones/5/5_32.html'
# response = requests.get(url=url)
# response.encoding = 'uthf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# div = soup.find('span', {'name':'count'}).text #поиск по атрибутам
# print(div)


'''url='https://parsinger.ru/html/headphones/5/5_32.html'
response = requests.get(url=url)
response.encoding = 'uthf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find('p', id='p_header').text #поиск по id
print(div)'''


# url='https://parsinger.ru/html/headphones/5/5_32.html'
# response = requests.get(url=url)
# response.encoding = 'uthf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# div = soup.find('p', class_='article').text #class_ пишется с подчеркиванием внизу. Такой синтаксис. Также нельзя применять .text к списку возвращаемому find_all
# print(div)



'''url='https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'uthf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find('div', 'item').find_all('li')
result = [] #не забывай добавлять пустой список для записи новых данных (а не перезаписи старых)
for x in div:
    result.append(x) #Команда добавления результата итерации в список result

# или через однострочный list comprehension вида: div = [x.text for x in soup.find('div', 'item').find_all('li')]'''




#with open('index.html', 'r', encoding='utf-8') as file:
    #soup = BeautifulSoup(file, 'lxml')
    #print(soup)

'''link_list = [] #странный парс картинок,с сайта по названиям, равными номеру итераций (1.png, 2.png ... 160.png). Почему картинки записываются в список link_list так и не понял (взял из другого примера). Точную ссылку на картинки взял в html-коде F12
for i in range(1, 161):
    urls = f'https://parsinger.ru/img_download/img/ready/{i}.png'
    ua = UserAgent()
    fake_ua = {'user-agent': ua.random}
    req = requests.get(url=urls, headers=fake_ua)
    response = req.content

    with open(f'image/{i}.png', 'wb') as file:
        file.write(response)
        link_list.append(file)
        print(f'File {file.name} is downloaded')'''


#url = 'https://youtu.be/iB17BJ2ohNU'
#response = requests.get(url=url, stream=True)
#with open('file.mp4', 'wb') as video:
#  for piece in response.iter_content(chunk_size=100000): #В байтах
#    video.write(piece)


'''response = requests.get(url=url, stream=True)
with open('file.mp4', 'wb') as file:
    file.write(response.content)'''



#for x in range(10):
#  ua = UserAgent()
#  fake_ua = {'user-agent': ua.random}
#  response = requests.get(url=url, headers=fake_ua)
#  print(response.text)

