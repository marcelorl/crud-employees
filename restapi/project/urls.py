from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.crud.views import EmployeeView

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'employees', EmployeeView, 'crud')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
