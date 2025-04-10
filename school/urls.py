from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('logout-user/', views.logout_user, name='logout'),
    path('register-user/', views.register_user, name='register'),
    path('view-record/<int:pk>', views.customer_record, name='view-record'),
    path('delete-record/<int:pk>', views.delete_record, name='delete-record'),
    path('add-record/', views.add_record, name='add-record'),
    path('update-record/<int:pk>', views.update_record, name='update-record'),
]
