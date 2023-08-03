from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('images/', views.images, name='images'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('recover/', views.recover, name='recover'),
    path('logout/', views.logout, name='logout'),
    path('avatar/', views.avatar_upload, name='avatar'),
    path('upload-image/', views.image_upload, name='upload-image'),

]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
