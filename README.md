#### Установка проекта

- установить версию python 3.8
- создать виртуальное окружение 
```shell script
python3.8 -m venv venv
```
- активировать виртуальное окружение
```shell script
source venv/bin/activate
```
- установить зависимости
```shell script
pip install -r requirements.txt
```
- проверить код на соответствие стайлгайдам и стандарту pep8
```shell script
flake8 .
```
- запустить тестовый django-проект
```shell script
./manage.py runserver
``` 
- открыть в браузере http://localhost:8000
- открыть в браузере http://localhost:8000/departure/str
- открыть в браузере http://localhost:8000/tour/123
