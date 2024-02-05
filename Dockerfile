# Используем официальный образ Python как базовый
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY . .

# Установка Firefox и GeckoDriver
USER root
RUN apt-get update \
    && apt-get install -y firefox-esr \
    && wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz \
    && tar -xvzf geckodriver* \
    && chmod +x geckodriver \
    && mv geckodriver /usr/local/bin/ \
    && apt-get clean

# Запускаем Flask приложение на порту 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
