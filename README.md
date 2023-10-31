# Для запуска проекта требуется:
## 1. Склонировать репозиторий
## 2. Добавить в корневой каталог файл .env:

- WEATHER_API_KEY=99ba78ee79a2a24bc507362c5288a81b
- DATABASE_HOST=database
- DATABASE_PORT=5432
- DATABASE_NAME=postgres
- DATABASE_USER=postgres
- DATABASE_PASSWORD=postgres
- LOG_LEVEL=debug
- PATH_TO_LOG_FILE=./log/backend.log

## 3. Выполнить команду:

```
make run
```

## При первом запуске потребуется применить миграции:

```
make migrations
```

## Документация к проекту находится по адресу:

### http://127.0.0.1:8000/docs
