
## Развертывание Django проекта

**Системы:**

* Linux
* macOS
* Windows

**Требования:**

* Python 3.8+
* Pipenv (или Poetry)
* PostgreSQL

**Инструкция:**

**1. Виртуальное окружение и пакеты:**

# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
py -3 -m venv venv
venv\Scripts\activate

pipenv install --dev

**2. Создание администратора Django:**

python manage.py createsuperuser

**3. Создание базы данных PostgreSQL:**

# Создать пользователя и базу данных
psql -U postgres -c "CREATE USER django WITH PASSWORD 'password';"
psql -U postgres -c "CREATE DATABASE myproject;"

# Подключиться к базе данных
psql -U django myproject

**4. Подключение к Django (.env):**

Создать файл .env

DATABASE_NAME='database_name'
DATABASE_USER='username'
DATABASE_PASSWORD='password
DATABASE_HOST='localhost'
DATABASE_PORT='5432`

**5. Запуск сервера:**

``python manage.py runserver``
