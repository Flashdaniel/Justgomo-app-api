from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'dashboard/{filename}'.format(filename=filename)


class DashboardBill(models.Model):
    """Dashboard Bill model"""

    bill_name = models.CharField(max_length=200)
    bill_icon = models.ImageField(_('bill_icon_image'), upload_to=upload_to)

    class Meta:
        ordering = ('-bill_name',)

    def __str__(self):
        return self.bill_name
