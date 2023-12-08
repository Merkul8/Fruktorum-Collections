from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='home'),
    # Регистрация, авторизация, выход из аккаунта
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # Collection
    path('collections/', get_collections, name='collections'),
    path('collections/<int:pk>/', CollectionDetailView.as_view(), name='collection'),
    path('create-collection/', collection_create, name='collection_create'),
    path('collections/<int:pk>/delete/', delete_collection, name='collection_delete'),
    path('collection/<int:pk>/update/', update_collection, name='update_collection'),
    path('collection/<int:pk>/add-bookmark/', add_bookmark_to_collection, name='add_bookmark_to_collection'),
    path('collection/<int:pk>/add-new-bookmark/', add_new_bookmark_to_collection, name='add_new_bookmark_to_collection'),
    #Bookmark
    path('bookmarks/', get_bookmarks, name='bookmarks'),
    path('bookmarks/<int:pk>/', BookmarkDetailView.as_view(), name='bookmark'),
    path('create-bookmark/', bookmark_create, name='create_bookmark'),
    path('bookmarks/<int:pk>/delete/', delete_bookmark, name='bookmark_delete'),
]
