# Fruktorum-Collections
Приложение для создания коллекций и хранения закладок в этих коллекциях и отдельно от них.

Старт проекта:

Для запуска приложения необходимо воспользоваться докером, и выполнить 3 команды.
Находясь в корневой директории(где находится manage.py) в терминале вводим команды:
1. docker-compose build
2. docker-compose up
3. После запуска проекта необходимо выполнить миграции: docker exec -it service-web-1 python manage.py migrate

При необходимости создать суперюзера: docker exec -it service-web-1 python manage.py createsuperuser 

API реализовано согласно ТЗ, так же были использованы celery и redis(в качестве брокера) для отправки сообщения 
зарегистрировавшемуся пользователю на почту, с информацией о возможностях сайта.
