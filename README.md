# fastapi-staff
Экспериментальный репозиторий для создания API на FAST API

# Настройка Alembic для асинхронного драйвера
1. Находясь в корневой директории, запустить:
```
    alembic init -t async migrations
    alembic upgrade head
```
2. Перенести папку migrations внутрь папки src.
3. Заменить prepend_sys_path на . src и script_location на src/migrations внутри alembic.ini
