# Yatube API
### Описание:
API для сайта микроблогов.
Доступные модели: Посты, Группы, Подписки, Комментарии

### Описание API



### Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:akchau/api_final_yatube.git
```

```
cd api_final_yatube
```

2. Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

3. Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

4. Выполнить миграции в папке yatube_api:

```
cd yatube_api
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
### Примеры запросов

