from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('register/', views.UserFormView.as_view(), name = "register"),
    path('<pk>/', views.DetailView.as_view(), name ="detail"),
    # path('song/<pk>', views.SongView.as_view(), name ="songs"),
    # path('<album_id>/favorite', views.favorite, name ="favorite")
    path('album/add/$', views.AlbumCreate.as_view(), name = "album-add"),
    path('song/add/$', views.SongCreate.as_view(), name = "song-add"),
    path('album/<pk>/$', views.AlbumUpdate.as_view(), name = "album-update"),
  
    path('song/update/<pk>/', views.SongUpdate.as_view(), name = "song-update"),
    # path('song/<pk>/', views.SongView.as_view(), name = "songDetails"),
    path('songs/list', views.SongView.as_view(), name = "songList"),
    path('song/<pk>/delete/$', views.SongDelete.as_view(), name = "song-delete"),
    path('album/<pk>/delete/$', views.AlbumDelete.as_view(), name = "album-delete")
    

]