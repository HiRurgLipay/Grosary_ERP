# Используем базовый образ Python
FROM python:3.9

# Установка переменной окружения для отключения записи .pyc файлов
ENV PYTHONDONTWRITEBYTECODE 1

# Установка переменной окружения для запуска Python в режиме не буферизованного вывода
ENV PYTHONUNBUFFERED 1

# Установка рабочей директории в /app
WORKDIR /app

# Копирование зависимостей в контейнер
COPY requirements.txt /app/

# Установка зависимостей
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копирование всего содержимого текущей директории в контейнер в /app
COPY . /app/

# Команда для запуска Django сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
