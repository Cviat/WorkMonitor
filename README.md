# WorkMonitor

WorkMonitor — программа для мониторинга активности пользователей. Состоит из двух компонентов:

- **Клиент** — собирает информацию о пользователе и скриншоты экрана, отправляет их на сервер.
- **Сервер** — принимает данные и предоставляет доступ через веб-интерфейс.



## Структура проекта

- `client/` — исходный код клиента
- `server/` — Django-приложение
- `requirements.txt` — зависимости сервера

## Установка

### Клиент

g++ client.cpp -o WorkMonitor -lws2_32 -lgdi32 -mwindows

### Сервер

1. Создать виртуальное окружение:
python -m venv venv
2. Активировать окружение:
.\venv\Scripts\activate
3. Установить зависимости:
pip install -r requirements.txt
4. Выполнить миграции:
python manage.py migrate
5. Запустить сервер:
python manage.py runserver




