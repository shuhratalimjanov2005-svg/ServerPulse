```markdown
# 🚀 ServerPulse Agent

[![Python Version](https://shields.io)](https://python.org)
[![License: MIT](https://shields.io)](https://opensource.org)
[![Status](https://shields.io)]()

Лёгкий и мощный агент для мониторинга вашего сервера в реальном времени.

---

## 🛠️ Быстрый старт (Установка)

### 1. Установите Python и pip (если не установлены)

Откройте терминал и выполните:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

> 📌 *Если ваша версия Ubuntu или Debian не содержит `python3-pip`, установите pip через `sudo apt install python3-pip` или `sudo apt install python3-venv`. При проблемах поищите в Google: `ubuntu install pip`.*

### 2. Установите зависимости

Перейдите в папку с агентом и выполните:

```bash
pip install -r requirements.txt
```

### 3. Настройте окружение

Скопируйте пример файла настроек:

```bash
cp .env.example .env
```

Отредактируйте `.env` в любом редакторе (nano, vim, etc.):

```env
API_TOKEN=ваш_секретный_токен
API_URL=https://professor-clarinet-penalty.ngrok-free.dev/api/v1/update
```

### 4. Запустите агента

```bash
python3 agent.py
```

> ⚠️ **После перезагрузки сервера агента нужно запускать заново** (см. раздел «Автозапуск» ниже).

---

## ⚡ Продвинутая настройка (Автозапуск через systemd)

Чтобы агент запускался автоматически вместе с сервером, создайте **systemd-сервис**.

1. Создайте файл `/etc/systemd/system/serverpulse-agent.service`:

```bash
sudo nano /etc/systemd/system/serverpulse-agent.service
```

2. Вставьте содержимое (замените `User` на имя вашего пользователя и `WorkingDirectory/ExecStart` на реальные пути):

```ini
[Unit]
Description=ServerPulse Monitoring Agent
After=network.target

[Service]
User=your_username
WorkingDirectory=/home/your_username/path/to/agent
ExecStart=/usr/bin/python3 /home/your_username/path/to/agent/agent.py
Restart=always

[Install]
WantedBy=multi-user.target
```

3. Включите и запустите службу:

```bash
sudo systemctl daemon-reload
sudo systemctl enable serverpulse-agent.service
sudo systemctl start serverpulse-agent.service
```

4. Проверьте статус:

```bash
sudo systemctl status serverpulse-agent.service
```

Теперь агент будет стартовать автоматически при загрузке системы.

> 📘 *Более подробные инструкции ищите в Google по запросу:*  
> *`how to run python script as service systemd ubuntu`*

---

## 🧪 Проверка работоспособности

После запуска агента вы увидите в консоли:

```
[*] Агент успешно инициализирован.
[+] Данные отправлены: CPU 12%, RAM 45%, HDD 67%
```

В основном боте ServerPulse через команду `/status` вы увидите ваш сервер и его метрики.

---

## 📄 Лицензия

Проект распространяется под лицензией MIT. Вы можете свободно использовать и изменять его.

---

# 🚀 ServerPulse Agent (English)

[![Python Version](https://shields.io)](https://python.org)
[![License: MIT](https://shields.io)](https://opensource.org)
[![Status](https://shields.io)]()

A lightweight monitoring agent for your server.

---

## 🛠️ Quick Start

### 1. Install Python & pip

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

> 📌 *If your Ubuntu/Debian version doesn't have `python3-pip`, try `sudo apt install python3-pip` or `sudo apt install python3-venv`. Google: `ubuntu install pip` if needed.*

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure

```bash
cp .env.example .env
```

Edit `.env` and set your token and server URL:

```env
API_TOKEN=your_token_here
API_URL=https://professor-clarinet-penalty.ngrok-free.dev/api/v1/update
```

### 4. Run

```bash
python3 agent.py
```

> ⚠️ *After a server reboot, you'll need to restart the agent (see Auto-start section below).*

---

## ⚡ Auto-start with systemd (optional)

To make the agent start automatically on boot, set up a systemd service.

1. Create file `/etc/systemd/system/serverpulse-agent.service`:

```bash
sudo nano /etc/systemd/system/serverpulse-agent.service
```

2. Fill with (replace paths and username with yours):

```ini
[Unit]
Description=ServerPulse Agent
After=network.target

[Service]
User=your_username
WorkingDirectory=/home/your_username/path/to/agent
ExecStart=/usr/bin/python3 /home/your_username/path/to/agent/agent.py
Restart=always

[Install]
WantedBy=multi-user.target
```

3. Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable serverpulse-agent.service
sudo systemctl start serverpulse-agent.service
```

4. Check status:

```bash
sudo systemctl status serverpulse-agent.service
```

> 📘 *For more details, search Google: `how to run python script as service systemd ubuntu`*

---

## 🧪 Testing

After starting the agent, you'll see:

```
[*] Агент успешно инициализирован.
[+] Данные отправлены: CPU 12%, RAM 45%, HDD 67%
```

In the main ServerPulse bot, use `/status` to see your server and its metrics.

---

## 📄 License

MIT License.
```


