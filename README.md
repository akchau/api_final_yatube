# Yatube API
### Описание:
API для сайта микроблогов.
Доступные модели: Посты, Группы, Подписки, Комментарии




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

#### 1. Запрос к постам

[GET, POST] http://127.0.0.1:8000/api/v1/posts/

#### Response
```
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
        {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
    ]
}
```
#### 2. Запрос к посту

[GET, PULL, PATCH, DELETE] http://127.0.0.1:8000/api/v1/posts/{id}/

#### Response
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```


#### 3. Запрос к комментариям поста

[GET, POST] http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

#### Response
```
[
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "created": "2019-08-24T14:15:22Z",
        "post": 0
    }
]
```


#### 4. Подписка на автора

[GET, POST] http://127.0.0.1:8000/api/v1/follow/

#### Response
```
{
    "following": "string"
}
```


