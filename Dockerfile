# Используем готовый образ selenium с Chrome и chromedriver
# FROM selenium/standalone-chrome:latest
FROM selenoid/chrome:128.0

# Устанавливаем Python и pip внутри контейнера
USER root
RUN apt-get update && apt-get install -y python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Копируем проект
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .

# Проверяем версию ChromeDriver
RUN chromedriver --version

# Проверяем версию Google Chrome
RUN google-chrome --version

# Переменные окружения (Chromium уже в другом контейнере)
ENV SELENIUM_REMOTE_URL="http://selenium:4444/wd/hub"

EXPOSE 4444
EXPOSE 8000
EXPOSE 7070
EXPOSE 8080
EXPOSE 135
EXPOSE 445
EXPOSE 2179
EXPOSE 7680
EXPOSE 8081
EXPOSE 49664
EXPOSE 49665
EXPOSE 49666
EXPOSE 49667
EXPOSE 49668
EXPOSE 49977
EXPOSE 49669



# ENTRYPOINT ["/usr/bin/selenoid", "-listen", ":4444", "-conf", "/etc/selenoid/browsers.json", "-video-output-dir", "/opt/selenoid/video/"]

# Переменные окружения (Chromium уже в другом контейнере)
# ENV SELENIUM_REMOTE_URL="http://selenium:4444/wd/hub"

# Проверяем аботает ли локальный сервер Selenium
# RUN curl -f http://127.0.0.1:4444/wd/hub/ || exit 1

# Запускаем pytest по умолчанию
CMD ["pytest"]
# CMD ["pytest", "--alluredir", "allure_results"]
#CMD ["pytest"]
