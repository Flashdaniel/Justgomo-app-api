from django.db import models
from django.conf import settings
from rest_framework.response import Response
import random
from twilio.rest import Client


class Code(models.Model):
    number = models.CharField(max_length=5, blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_items = []

        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)

        code_str = ''.join(str(item) for item in code_items)
        self.number = code_str
        phone_str = self.user.phone_number
        try:
            account_sid = 'AC6daf8291a2423367c34d7f204225fc5f'
            auth_token = '9a0cde9aaa6d59634380a433ccc32111'
            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                body=f"Hi! Your user verification code is {self.number}",
                                from_='+12563803438',
                                to=f'{phone_str}'
                            )

            print(message.sid)
        except:
            raise Exception('Twilio  Failed to establish a new connection')
        finally:
            super().save(*args, **kwargs)
