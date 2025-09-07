# Базовый образ python (легковесный)
FROM python:3.11-slim

# Установка зависимостей
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Создание директории проекта
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt .
COPY . .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Настройка рабочей директории
WORKDIR /app

# Прослушиваемый порт для входящих соединений
EXPOSE 8000

# Команда запуска
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
