from service.celery import app
from django.core.mail import send_mail

# Отправление письма с помощью celery
@app.task
def send_test_message(person_mail):
    send_mail('Добро пожаловать!', 
              'Добрый день, спасибо за регистрацию! Теперь вы можете добавлять, удалять, изменять свои коллекции, добавлять к ним закладки и изменять их, создавать новые закладки. Теперь вы можете приступать к ознакомлению!', 
              'test.maksim99@gmail.com', 
              [person_mail]
            )