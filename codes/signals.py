from users.models import User
from .models import Code
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_generated__code(sender, instance, created, *args, **kwargs):
    if created:
        Code.objects.create(user=instance)
