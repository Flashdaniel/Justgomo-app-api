from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', include('users.urls',  namespace='users')),
    path('api/bill/', include('bills.urls',  namespace='bill')),
    path('api/verify/', include('codes.urls',  namespace='code')),
    path('api/dashboard-bill-list/',
         include('dashboard.urls',  namespace='dashboardbill')),
    path('api/password_reset/',
         include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('doc/', include_docs_urls(title='JustGomo')),
    path('schema', get_schema_view(
        title="JustGomo",
        description="API on the JustGomo",
        version="1.0.0"
    ), name='openapi-schema'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
