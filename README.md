# 🚀 ServerPulse Agent

[![Python Version](https://shields.io)](https://python.org)
[![License: MIT](https://shields.io)](https://opensource.org)
[![Status](https://shields.io)]()

Легковесный и мощный агент для мониторинга состояния вашего сервера в реальном времени.

---

## 🛠️ Быстрый старт (Установка)

Следуйте этим простым шагам, чтобы развернуть и запустить агента за пару минут:

### 1. Подготовка окружения
Убедитесь, что в вашей системе установлен **Python 3.8** или выше. Если его нет, скачайте с [официального сайта](https://python.org).

### 2. Установка зависимостей
Установите все необходимые библиотеки одной командой в терминале:
```bash
pip install -r requirements.txt
```

### 3. Настройка конфигурации
Переименуйте демонстрационный файл настроек в рабочий файл конфигурации:
```bash
cp .env.example .env
```
Откройте созданный файл `.env` в любом текстовом редакторе и укажите ваш токен и URL-адрес сервера:
```env
API_TOKEN=ваш_секретный_токен_тут
API_URL=https://professor-clarinet-penalty.ngrok-free.dev/api/v1/update
```

### 4. Запуск агента
Запустите скрипт мониторинга:
```bash
python agent.py
```

> ⚠️ **Важно:** Если ваш сервер перезагрузился или временно отключился, не забудьте запустить агента заново.

---

## ⚡ Продвинутая настройка (Автозапуск)

Чтобы не запускать агента вручную после каждой перезагрузки сервера, настройте его как фоновую службу с помощью **systemd**. Это позволит агенту стартовать автоматически вместе с операционной системой.

🔍 Подробную пошаговую инструкцию по настройке можно найти в Google по запросу:
> *`how to run python script as service systemd`*

---

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. Вы можете свободно использовать и изменять его.

# 🚀 ServerPulse Agent

A lightweight monitoring agent for your server. Follow the steps below to install and configure the agent quickly.

---

## 🛠️ Installation & Setup

### 1. Install Dependencies
First, ensure you have Python installed on your system. Then, install the required packages:
```bash
pip install -r requirements.txt
```

### 2. Configuration
Prepare your environment variables by renaming the example file:
```bash
cp .env.example .env
```
Open the newly created `.env` file and insert your unique **Server Token** and **Server URL**:
```env
API_TOKEN=your_token_here
API_URL=https://professor-clarinet-penalty.ngrok-free.dev/api/v1/update
```

### 3. Run the Agent
Launch the agent using Python:
```bash
python agent.py
```
*💡 Note: If your server restarts or goes offline, make sure to restart the agent.*

---

## ⚡ Advanced Setup (Auto-start)

For advanced users who want the agent to start automatically when the server boots, we recommend setting up a **systemd service**. 

You can find detailed guides by searching Google for:
> *`how to run python script as service systemd`*
