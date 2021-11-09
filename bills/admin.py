from django.contrib import admin
from .models import Bill, PayedBill
admin.site.register(Bill)
admin.site.register(PayedBill)
