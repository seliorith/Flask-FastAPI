import argparse
import asyncio
import aiohttp
from os.path import join  # Используется для безопасного соединения частей пути к файлу или каталогу
import os
from time import time

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
#

target_folder = "Images_async"

if not os.path.exists(target_folder):
    os.makedirs(target_folder)


async def download(url, session):
    start_time = time()
    try:
        async with session.get(url) as response:
            if response.status == 200:
                filename = 'async_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.jpg'
                full_path = join(target_folder, filename)
                with open(full_path, 'wb') as f:
                    async for chunk in response.content.iter_chunked(1024):
                        f.write(chunk)
                print(f"Файл {filename} скачан за {time() - start_time:.2f} сек")
            else:
                print(f"Ошибка при скачивании {url}: Статус {response.status}")
    except Exception as e:
        print(f"Ошибка при скачивании {url}: {e}")


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [download(url, session) for url in urls]
        await asyncio.gather(*tasks)  # Используется для запуска нескольких асинхронных корутин


if __name__ == '__main__':
    start_time = time()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.close()
    end_time = time()
    print(f'Программа отработала за {end_time - start_time:.2f} сек')
