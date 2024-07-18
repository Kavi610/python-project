from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
   path('home/',views.home,name="home"),
   path('register/',views.register,name="register"),
   path('login/',views.my_login,name="login"),
   path('logout/',views.user_logout,name="logout"),
   path('dashboard/',views.dashboard,name="dashboard"),
   path('create/',views.create_record,name="create-record"),
   path('update/<int:pk>',views.update_record,name="update-record"),
   path('record/<int:pk>',views.singular_record,name="singular-record"),
   path('delete/<int:pk>',views.delete_record,name="delete-record"),
   path('upload/',views.uploadfile,name="upload-file"),
   path('books/',views.book_list,name="book_list"),
   path('books/uploaded',views.upload_book,name="upload_book")

]

if settings.DEBUG:
   urlpatterns +=static(settings.MEDIA_URL,socument_root=settings.MEDIA_ROOT)
   
   


