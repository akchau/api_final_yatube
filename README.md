# Yatube API
### Описание:
API для сайта микроблогов.
Доступные модели: Посты, Группы, Подписки, Комментарии

### Описание API
1. Запустить проект: В режиме разработчика перейти

```
http://127.0.0.1:8000/swagger/
```

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
python3 -m venv venv
```

```
source venv/Scripts/activate
```

3. Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

4. Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
