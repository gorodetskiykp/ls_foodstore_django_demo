# ls_foodstore_django_demo
Демо-проект (Django + Bootstrap). Продуктовый магазин

# Структура
1. Товар
    - название (+ шт., кг., ...)
    - цена за ед.
2. Корзина
    - товар
    - кол-во
    - дата и время формирования позиции


# Взаимодействие Django-модулей
1. Brouser -> URL -> request
2. URL -> urls.py -> views.py
2'. views.py 
        <> models.my
        <> templates
        -> response

# Порядок действий
1. установить virtualenv
    - pipenv install

2. устновить зависимости (django)
    - pipenv install django
    
3. Создать проект
    - pipenv run django-admin startproject foodstore
    
4. Создать приложение
    - pipenv run python manage.py startapp store
5. Зарегистрировать приложение
    - "store.apps.StoreConfig"

Приложение:

1. Создать модели

2. Подготовить миграции
    - pipenv run python manage.py makemigrations

3. Осуществить миграции в БД
    pipenv run python manage.py migrate

4. Подготовить маршруты
5. Подготовить view (логика)
    - взаимодействие с моделями
    - взимодействие с шаблонами
6. Сформировать шаблоны (templates, html, json)
