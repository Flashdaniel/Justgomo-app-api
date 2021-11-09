from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'bills/{filename}'.format(filename=filename)


class Bill(models.Model):
    """Bill model"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(_('image'), upload_to=upload_to)
    account = models.IntegerField(_('account'))
    amount = models.IntegerField(_('amount'))
    payment_method = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


class PayedBill(models.Model):
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)
    payed = models.BooleanField(default=False)
    sumbited_date = models.DateTimeField(timezone.now)

    def __str__(self):
        return str(self.sumbited_date)
