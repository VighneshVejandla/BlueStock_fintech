# bluestock/urls.py

from django.urls import path
from .views import login_view, signup_view, forgot_password_view

from .views import dashboard

from .views import dashboard, manageipo, register_ipo
from .views import dashboard


urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('forgotpassword/', forgot_password_view, name='forgot_password'),
    path('dashboard/', dashboard, name='dashboard'),
    path('manageipo/', manageipo, name='manageipo'),
    path('register/', register_ipo, name='register_ipo'),
]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

