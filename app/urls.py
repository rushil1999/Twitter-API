from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('tweets/',views.getParameters, name = 'getParameters')
    # path(r'^tweets$',views.getParameters)
]