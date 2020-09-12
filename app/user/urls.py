from django.urls import path, include

from user import views

app_name = 'user'

urlpatterns = [
    # management
    path('me', views.ManageUserView.as_view(), name='me'),
]