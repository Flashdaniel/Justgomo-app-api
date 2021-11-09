from django.http import request
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.models import User
from codes.models import Code
import random
from twilio.rest import Client


class ValidatePhone(APIView):
    """Verify the user's phone number with email and the SMS code."""

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        code = request.data.get('code')

        if email and code:
            email_verify = str(email)
            user = User.objects.get(email__iexact=email_verify)
            if user:
                code_str = str(user.code)

                stored_code = code_str
                if str(code) == stored_code:
                    return Response('Phone number verified.')
                else:
                    return Response('Phone number not verified.')
            else:
                return Response('User does not exist.')

        else:
            return Response('Email or Code is not given in post request')


class Resend(APIView):
    """Resend verification code using the users email"""

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        account_sid = 'AC6daf8291a2423367c34d7f204225fc5f'
        auth_token = '9a0cde9aaa6d59634380a433ccc32111'
        client = Client(account_sid, auth_token)

        if email:
            user = User.objects.get(email=email)
            if user:
                number_list = [x for x in range(10)]
                code_items = []

                for i in range(5):
                    num = random.choice(number_list)
                    code_items.append(num)

                code_str = ''.join(str(item) for item in code_items)
                phone_str = user.phone_number

                code_user = Code.objects.get(user=user.id)

                if code_user:
                    Code.objects.filter(user=user.id).update(number=code_str)
                    client.messages \
                        .create(
                            body=f"Hi! Your user verification code is {code_str}",
                            from_='+12563803438',
                            to=f'{phone_str}'
                        )

                    return Response('verification code resent.')
                else:
                    Code.objects.create(number=code_str, user=user.id)
                    client.messages \
                        .create(
                            body=f"Hi! Your user verification code is {code_str}",
                            from_='+12563803438',
                            to=f'{phone_str}'
                        )

                    return Response('verification code sent.')

            else:
                return Response('User does not exist.')
        else:
            return Response('Email was not sent as a post request.')
