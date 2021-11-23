from django.shortcuts import get_object_or_404
from django.http import request
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.models import User
from codes.models import Code
import os
import random
from twilio.rest import Client


class ValidatePhone(APIView):
    """Verify the user's phone number with email and the SMS code."""

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        code = request.data.get('code')

        if email and code:
            email_verify = str(email)
            try:
                user = User.objects.get(email__iexact=email_verify)
                if user:
                    code_str = str(user.code)

                    stored_code = code_str
                    if str(code) == stored_code:
                        return Response('Phone number verified.')
                    else:
                        return Response('Wrong code phone number not verified.')
            except User.DoesNotExist:
                return Response('User does not exist.')
            else:
                return Response('User does not exist.')

        else:
            return Response('Email or Code is not given in post request')


class Resend(APIView):
    """Resend verification code using the users email"""

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        account_sid = os.environ['Account_SID']
        auth_token = os.environ['Auth_token']
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
                try:
                    code_user = Code.objects.get(user=user.id)
                    if code_user:
                        Code.objects.filter(
                            user=user.id).update(number=code_str)
                        client.messages \
                            .create(
                                body=f"Hi! Your user verification code is {code_str}",
                                from_='+12563803438',
                                to=f'{phone_str}'
                            )

                        return Response('verification code resent.')
                except Code.DoesNotExist:
                    myUser = get_object_or_404(User, id=user.id)
                    print(myUser)
                    Code.objects.create(number=code_str, user=myUser)
                    return Response('Code dose not exist but it has been created')
                finally:
                    try:
                        client.messages \
                            .create(
                                body=f"Hi! Your user verification code is {code_str}",
                                from_='+12563803438',
                                to=f'{phone_str}'
                            )
                        return Response('verification code sent.')
                    except:
                        return Response('Twilio failed to establish a new connection, pls check your network connection and resend again.')
            else:
                return Response('User does not exist.')
        else:
            return Response('Email was not sent as a post request.')
