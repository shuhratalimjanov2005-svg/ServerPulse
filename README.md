```markdown
# ServerPulse Agent

[🇷🇺 Русский](#русский) | [🇺🇸 English](#english)

---

<a name="русский"></a>
## 🇷🇺 Русский

# Легковесный агент для мониторинга сервера

ServerPulse Agent — это инструмент для мониторинга состояния вашего сервера в реальном времени. Мы используем **Docker**, поэтому вам не нужно вручную устанавливать Python или зависимости — всё уже настроено внутри контейнера.

### 🚀 Быстрый старт

#### 1. Установка Docker
Если Docker еще не установлен, выполните команды:
```bash
sudo apt update
sudo apt install docker.io docker-compose -y
sudo systemctl enable --now docker

```

#### 2. Настройка конфигурации

Скопируйте файл с примером настроек и создайте рабочий файл:

```bash
cp .env.example .env

```

Откройте файл `.env` для редактирования:

```bash
nano .env

```

Вставьте туда ваши данные:

```text
API_TOKEN=ваш_секретный_токен_тут
API_URL=https://professor-clarinet-penalty.ngrok-free.dev/api/v1/update

```

*(Для сохранения в nano: нажмите `Ctrl+O`, `Enter`, затем `Ctrl+X`)*

#### 3. Запуск

Запустите агента одной командой:

```bash
docker-compose up -d --build

```

#### 4. Управление

* **Просмотр логов:** `docker-compose logs -f`
* **Остановка:** `docker-compose down`
* **Автозапуск:** Агент будет автоматически запускаться при старте системы благодаря настройке `restart: always`.

---

## 🇺🇸 English

# Lightweight Server Monitoring Agent

ServerPulse Agent is a real-time server monitoring tool. We use **Docker**, so there is no need to manually install Python or any dependencies.

### 🚀 Quick Start

#### 1. Install Docker

If Docker is not installed yet, run:

```bash
sudo apt update
sudo apt install docker.io docker-compose -y
sudo systemctl enable --now docker

```

#### 2. Configuration

Create your `.env` file from the example:

```bash
cp .env.example .env

```

Open it for editing:

```bash
nano .env

```

Add your details:

```text
API_TOKEN=your_token_here
API_URL=https://professor-clarinet-penalty.ngrok-free.dev/api/v1/update

```

*(To save in nano: press `Ctrl+O`, `Enter`, then `Ctrl+X`)*

#### 3. Run

Launch the agent:

```bash
docker-compose up -d --build

```

#### 4. Management

* **View logs:** `docker-compose logs -f`
* **Stop:** `docker-compose down`
* **Auto-start:** The agent restarts automatically on system boot thanks to `restart: always`.

---

## 📄 License

MIT.

```

---

### А теперь проверь, чтобы у тебя в папке лежали эти два файла:
### Just check if these files exists in your dir
**1. Файл `Dockerfile`** (пусть лежит рядом с `agent.py`):
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "agent.py"]

```

**2. Файл `docker-compose.yml**` (тоже в корне):

```yaml
services:
  agent:
    build: .
    container_name: serverpulse-agent
    restart: always
    env_file:
      - .env

```

