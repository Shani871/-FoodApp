from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:item_id>/', views.detail, name='detail'),
    path('add',views.create_item, name='add'),
    path('update/<int:id>/', views.update_product, name='update_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
]