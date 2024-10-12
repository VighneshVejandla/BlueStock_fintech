from django.urls import path, include
from django.contrib import admin
from .views import signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bluestock.Blue_Stock_Project.urls')),

    # path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    # path('forgotpassword/', forgot_password_view, name='forgot_password'),
]