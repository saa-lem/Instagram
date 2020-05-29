from django.urls import path
from .views import ImageListView,ImageDetailView,ImageCreateView,ImageUpdateView,ImageDeleteView,UserImageListView,ImageLikeRedirectView, CommentCreateView
from . import views


urlpatterns = [
    path('',ImageListView.as_view(), name = 'home'),
    path('user/<str:username>/',UserImageListView.as_view(), name = 'user-images'),
    path('image/<int:pk>/',ImageDetailView.as_view(), name = 'image-detail'),
    path('profile/details/<str:username>/',views.display_profile, name = 'profile-detail'),
    path('image/new/',ImageCreateView.as_view(), name = 'image-create'),
    path('image/<int:pk>/comment/',CommentCreateView.as_view(), name = 'comment-create'),
    path('image/<int:pk>/update/',ImageUpdateView.as_view(), name = 'image-update'),
    path('image/<int:pk>/delete/',ImageDeleteView.as_view(), name = 'image-delete'),
    path('image/<int:pk>/like/',ImageLikeRedirectView.as_view(), name = 'image-likes'),
    path('follow/<username>/',views.get_followers, name = 'following'),
    path('search/',views.search_results, name = 'search_results'),
    
   
]