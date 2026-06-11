import os
import requests
import psutil
import time
from dotenv import load_dotenv

# Загружаем настройки из файла .env
load_dotenv()

TOKEN = os.getenv("API_TOKEN").strip()
API_URL = os.getenv("API_URL")

if not API_URL:
    print("[!] ОШИБКА: API_URL не задан в переменных окружения!")
    exit(1)

if not TOKEN:
    print("[!] ОШИБКА: Токен не найден!")
    print("[!] Создайте файл .env и запишите туда: API_TOKEN=ваш_токен")
    exit(1)

print("[*] Агент успешно инициализирован.")

while True:
    try:
        data = {
            "cpu": psutil.cpu_percent(),
            "ram": psutil.virtual_memory().percent,
            "hdd": psutil.disk_usage('/').percent
        }
        response = requests.post(API_URL, json=data, headers={"api-token": TOKEN}, timeout=5)

        if response.status_code == 200:
            print(f"[+] Данные отправлены: CPU {data['cpu']}%, RAM {data['ram']}%, HDD {data['hdd']}%")
        else:
            print(f"[-] Сервер вернул ошибку: {response.status_code}")

    except Exception as e:
        print(f"[-] Ошибка подключения: {e}")

    time.sleep(60)

