from django.urls import path, include
from . import views

app_name = 'bills'

urlpatterns = [
    path('', views.ListBill.as_view(), name='listbill'),
    path('create/', views.CreateBill.as_view(), name='createbill'),
    path('retrieve/<int:pk>/', views.RetrievesBill.as_view(), name='retrievebill'),
    path('update/<int:pk>/', views.UpdateBill.as_view(), name='updatebill'),
    path('delete/<int:pk>/', views.DestroyBill.as_view(), name='deletebill'),
    path('payed/', views.ListPayedBill.as_view(), name='listbill'),
    path('payed/create/', views.CreatePayedBill.as_view(), name='createbill'),
    path('payed/<int:pk>/', views.RetrievesPayedBill.as_view(), name='retrievebill'),
    path('payed/update/<int:pk>/',
         views.UpdatePayedBill.as_view(), name='updatebill'),
]
