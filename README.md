<p align="center">
  <img src="images/logo.png" alt="Logo" width="50%"/>
</p>

##

**Aiotemplate** – базовая структура для быстрого начала разработки telegram-ботов на [aiogram 3.x](https://github.com/aiogram/aiogram).
Шаблон предоставляет модульную ахритектуру, позволяет легко ориентироваться в коде, даёт прочный фундамент для поддержки и расширения функционала.

## Ключевые особенности

- **Встроенный веб-сервер** - Использует `aiohttp` для обеспечения интегрированного веб-сервера, обрабатывающего запросы, вебхуки и другие веб-взаимодействия.
- **Переменные окружения через Pydantic Settings** - Управление окружением с помощью `pydantic-settings` для удобного контроля конфигурации.
- **Поддержка баз данных через SQLAlchemy ORM** - Готовая настройка для интеграции SQL базы данных с использованием SQLAlchemy, упрощающая взаимодействие с базой данных.

## Установка

1. **Клонирование репозитория**:
    ```bash
    git clone https://github.com/nelexey/aiotemplate.git
    cd aiotemplate
    ```

2. **Создание и активация виртуальной среды**:
    ```bash
    python -m venv env
    
    # Для Linux/MacOS:
    source env/bin/activate
    
    # Для Windows:
    env\Scripts\activate
    ```

3. **Установка зависимостей**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Переменные окружения**:
    - Скопируйте `.env.example` в `.env` и настройте параметры под вашу конфигурацию.

_Примечание: После завершения работы вы можете деактивировать виртуальную среду командой `deactivate`_

## Начало работы

1. **Настройка переменных окружения**:
   - Определите токен бота, URL базы данных и настройки веб-сервера в файле `.env`.

2. **Запуск бота**:
    ```bash
    python run.py
    ```

## Структура проекта

```plaintext
aiotemplate/
│
├── bot/
│   ├── database/         # Настройка базы данных, модели и управление сессиями
│   ├── handlers/         # Обработчики различных команд и сообщений бота
│   ├── middlewares/      # Пользовательские промежуточные слои для обработки запросов
│   ├── web/              # Веб-сервер и маршруты
│   ├── misc/             # Различные конфигурации и утилиты
│   └── main.py           # Инициализация и запуск бота
│
├── .env.example          # Пример переменных окружения, .env должен быть тут же
├── requirements.txt      # Зависимости Python-пакетов
└── README.md             # Документация проекта
```

## Возможности

- ### Встроенный веб-сервер

    - Веб-сервер построен с использованием `aiohttp` и находится в `bot/web/server.py`. Он настроен на эффективную обработку асинхронных запросов и может использоваться для различных целей, включая обработку вебхуков или обслуживание веб-интерфейса.

- ### ORM с SQLAlchemy

    - Шаблон включает настройку базы данных с использованием SQLAlchemy, с моделями, определенными в `bot/database/models/`. Эта настройка поддерживает операции CRUD и беспроблемную интеграцию с PostgreSQL или другими SQL базами данных.

- ### Конфигурация окружения через Pydantic Settings

    - Переменные окружения управляются через `pydantic-settings`, обеспечивая структурированную и легко поддерживаемую конфигурацию.

- ### Промежуточные слои и модульная маршрутизация

    - Этот шаблон предоставляет пользовательские промежуточные слои (например, ограничение скорости, проверки аутентификации) и использует модульную маршрутизацию для организации функциональности бота. Обработчики аккуратно организованы по функциональности, что упрощает расширение возможностей бота.

## Переменные окружения

Определите следующие переменные в вашем файле `.env`:

- `BOT_TOKEN`: Токен Telegram бота
- `DB_USER`, `DB_PASS`, `DB_HOST`, `DB_PORT`, `DB_NAME`: Детали подключения к базе данных
- `WEB_HOST`, `WEB_PORT`, `WEB_TIMEOUT`, `WEB_MAX_CONNECTIONS`: Настройки веб-сервера

Пример файла `.env`:
```plaintext
BOT_TOKEN=your_bot_token_here

DB_USER=your_db_user
DB_PASS=your_db_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_db_name

WEB_HOST=localhost
WEB_PORT=8000
WEB_TIMEOUT=1
WEB_MAX_CONNECTIONS=10000000

WEB_SERVICE_HOST=https://example.com/api
WEB_SERVICE_PORT=8081
```

## Лицензия

Этот проект лицензирован под MIT License. Смотрите [LICENSE](LICENSE) для подробностей.
