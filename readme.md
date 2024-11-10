<p>
  <img src="images/logo.png" alt="Logo" width="100%" style="padding: 10%"/>
</p>

---

# Aiotemplate

**Aiotemplate** is a robust starting point for building scalable, production-ready Telegram bots using the [aiogram](https://github.com/aiogram/aiogram) framework. This template provides a clean, modular structure that is optimized for easy scaling, debugging, and deployment. It’s ideal for developers looking to streamline the development of complex bots with integrated web functionality and database support.

This template serves as the **foundation** of a Telegram bot, with built-in **modules** that act as the essential "organs" for smooth bot operation.

## Key Features
---

- **Integrated Web Server** - Uses `aiohttp` to provide a fully integrated web server for handling requests, webhooks, and other web-based interactions.
- **Database Support with SQLAlchemy ORM** - Ready-to-use setup for integrating a SQL database using SQLAlchemy, simplifying database interactions.
- **Environment Variables via Pydantic Settings** - Environment management with `pydantic-settings` for seamless configuration control.
- **Modular Design** - Cleanly separated components, such as routers and middlewares, for easy customization and scaling.
- **Asynchronous and Efficient** - Optimized for handling multiple requests and messages asynchronously, providing efficient and fast responses.

---

## Table of Contents

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Features and Usage](#features-and-usage)
- [Environment Variables](#environment-variables)
- [License](#license)

---

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/nelexey/aiotemplate.git
    cd aiotemplate
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Environment Variables**:
    - Copy `.env.example` to `.env` and adjust the settings to match your configuration.

---

## Getting Started

1. **Configure Environment Variables**:
   - Define your bot token, database URL, and web server settings in the `.env` file.

2. **Run the Bot**:
    ```bash
    python main.py
    ```

---

## Project Structure

```plaintext
aiotemplate/
│
├── bot/
│   ├── database/         # Database setup, models, and session management
│   ├── handlers/         # Handlers for different bot commands and messages
│   ├── middlewares/      # Custom middlewares for request processing
│   ├── web/              # Web server and routes
│   ├── misc/             # Miscellaneous configurations and utilities
│   └── main.py           # Bot initialization and launch
│
├── .env.example          # Sample environment variables
├── requirements.txt      # Python package dependencies
└── README.md             # Project documentation
```

---

## Features

- ### Built-in Web Server

    - The web server is built using `aiohttp` and can be found in `bot/web/server.py`. It is configured to handle asynchronous requests efficiently and can be used for various purposes, including handling webhooks or serving a web-based interface.

- ### ORM with SQLAlchemy

The template includes a database setup using SQLAlchemy, with models defined in `bot/database/models/`. This setup supports CRUD operations and seamless integration with PostgreSQL or other SQL databases.

- ### Environment Configuration via Pydantic Settings

    - Environment variables are managed through `pydantic-settings`, enabling structured and easy-to-maintain configuration.


- ### Middlewares and Modular Routing

    - This template provides custom middlewares (e.g., rate-limiting, authentication checks) and uses modular routing to organize bot functionality. Handlers are neatly organized by functionality, making it easier to expand the bot’s capabilities.

---

## Environment Variables

Define the following variables in your `.env` file:

- `BOT_TOKEN`: Telegram bot token
- `DB_USER`, `DB_PASS`, `DB_HOST`, `DB_PORT`, `DB_NAME`: Database connection details
- `WEB_HOST`, `WEB_PORT`, `WEB_TIMEOUT`, `WEB_MAX_CONNECTIONS`: Web server settings

Example `.env` file:
```plaintext
BOT_TOKEN=your_bot_token
DB_USER=your_db_user
DB_PASS=your_db_pass
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_db_name
```

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.