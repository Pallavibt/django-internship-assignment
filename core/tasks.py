from celery import shared_task 
from django.contrib.auth.models import User 
from django.core.mail import send_mail 

@shared_task 
def send_welcome_email(user_id): 
    user = User.objects.get(id=user_id) 
    send_mail( 'Welcome!', 
              f'Hello {user.username}, welcome!', 
              'admin@example.com', 
              [user.email], 
              fail_silently=False, 
    )