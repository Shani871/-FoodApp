from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import users
from users.views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Ensure this line appears only once
    path('', include('FoodApp.urls')),  # Your app's URL inclusion
    path('register/',register,name='register'),  # Your app's URL inclusion
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', users.views.profile, name='profile'),
  ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)