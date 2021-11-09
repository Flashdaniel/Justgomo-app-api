from django.urls import path, include
from . import views

app_name = 'dashboardbills'

urlpatterns = [
    path('', views.ListDashboardBill.as_view(), name='listbill'),
    path('create/', views.CreateDashboardBill.as_view(), name='createbill'),
    path('update/<int:pk>/', views.UpdateDashboardBill.as_view(), name='updatebill'),
    path('retrieve/<int:pk>/', views.RetrievesDashboard.as_view(), name='retrievebill'),
    path('delete/<int:pk>/', views.DestroyDashboardBill.as_view(), name='deletebill'),
]
