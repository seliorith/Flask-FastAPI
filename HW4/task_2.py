import argparse
import requests
from multiprocessing import Process
from os.path import join  # Используется для безопасного соединения частей пути к файлу или каталогу
from time import time
import os

urls = [
    "https://amiel.club/uploads/posts/2022-03/1647665789_12-amiel-club-p-malenkie-kotyata-kartinki-15.jpg",
    "https://cdn.ananasposter.ru/image/cache/catalog/poster/art/85/8067-1000x830.jpg",
    "https://ir.ozone.ru/s3/multimedia-u/6586916970.jpg"

]

# # Добавление возможности задавать список URL-адресов через аргументы командной строки.
# parser = argparse.ArgumentParser(
#     description='Скачивание изображений по URL.')  # Создаём объект парсер при помощи класса ArgumentParser
# parser.add_argument('urls', nargs='+',
#                     help='Список URL-адресов для скачивания.')  # Добавляем в полученный экземпляр аргументы для парсинга через метод add_argument
# args = parser.parse_args()  # Выгружаем результаты
# urls = args.urls  # Присваивает переменной urls список URL-адресов, который был получен из аргументов командной строки

target_folder = "Images_proc"

if not os.path.exists(target_folder):
    os.makedirs(target_folder)


def download(url):
    start_time = time()
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            filename = 'proc_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.jpg'
            full_path = join(target_folder, filename)
            with open(full_path, 'wb') as f:
                # Пошаговая загрузка файла, метод iter_content(chunk_size)
                # позволяет читать содержимое ответа по частям (chunk) фиксированного размера
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Файл {filename} скачан за {time() - start_time:.2f} сек")
        else:
            print(f"Ошибка при скачивании {url}: Статус {response.status_code}")
    except Exception as e:
        print(f"Ошибка при скачивании {url}: {e}")


if __name__ == '__main__':
    start_time = time()
    processes = []

    for url in urls:
        process = Process(target=download, args=[url], daemon=True)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time()
    print(f'Программа отработала за {end_time - start_time:.2f} сек')
