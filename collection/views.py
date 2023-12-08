from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from .models import *
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import DetailView
from .services import get_some_parameters
from collection.tasks import send_test_message

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'collection/login.html', {'form': form})

# view выхода из аккаунта
def user_logout(request):
    logout(request)
    return redirect('home')

# view регистрации
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Успешная регистрация')
            send_test_message.delay(form.cleaned_data['email'])
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'collection/register.html', {'form': form})

# view главной страницы
def main(request):
    return render(request, 'collection/main.html')

# Collection 
def get_collections(request):
    all_collections = Collection.objects.all()
    return render(request, 'collection/collections_templates/collections.html', context={'all_collections': all_collections})

class CollectionDetailView(DetailView):
   model = Collection
   context_object_name = 'collection'
   template_name = 'collection/collections_templates/collection_detail.html'

def collection_create(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            Collection.objects.create(
                title=form.cleaned_data['title'], 
                description=form.cleaned_data['description'], 
                user=request.user
                )
            messages.success(request, 'Создание коллекции выполнено!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка.')
    else:
        form = CollectionForm()
    return render(request, 'collection/collections_templates/create_collection.html', {'form': form})

def delete_collection(request, pk):
   collection = get_object_or_404(Collection, pk=pk)
   if request.method == 'POST':
       collection.delete()
       return redirect('collections')
   return render(request, 'collection/collections_templates/delete_collection.html', {'collection': collection})

def update_collection(request, pk):
  collection = get_object_or_404(Collection, pk=pk)
  if request.method == 'POST':
      form = CollectionForm(request.POST, instance=collection)
      if form.is_valid():
          collection = form.save()
          return redirect('collections')
  else:
      form = CollectionForm(instance=collection)
  return render(request, 'collection/collections_templates/update_collection.html', {'form': form})

# Bookmark
def get_bookmarks(request):
    all_bookmarks = Bookmark.objects.all()
    return render(request, 'collection/bookmarks_templates/bookmarks.html', context={'all_bookmarks': all_bookmarks})

class BookmarkDetailView(DetailView):
   model = Bookmark
   context_object_name = 'bookmark'
   template_name = 'collection/bookmarks_templates/bookmark_detail.html'

def bookmark_create(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            parametrs_for_bookmark = get_some_parameters(url=form.cleaned_data['url'])
            Bookmark.objects.create(
                title=parametrs_for_bookmark.get('title', 'Не найдено'),
                description=parametrs_for_bookmark.get('description', 'Не найдено'),
                og_image=parametrs_for_bookmark.get('image', 'Не найдено'),
                og_type=parametrs_for_bookmark.get('type', 'Не найдено'),
                site_name=parametrs_for_bookmark.get('site_name', 'Не найдено'),
                url=form.cleaned_data['url'],
                user=request.user,
                )
            messages.success(request, 'Создание коллекции выполнено!')
            return redirect('bookmarks')
        else:
            messages.error(request, 'Ошибка.')
    else:
        form = BookmarkForm()
    return render(request, 'collection/bookmarks_templates/create_bookmark.html', {'form': form})

def delete_bookmark(request, pk):
   bookmark = get_object_or_404(Bookmark, pk=pk)
   if request.method == 'POST':
       bookmark.delete()
       return redirect('bookmarks')
   return render(request, 'collection/bookmarks_templates/delete_bookmark.html', {'bookmark': bookmark})

# добавление закладки в коллекцию
def add_bookmark_to_collection(request, pk):
   collection = get_object_or_404(Collection, pk=pk)
   if request.method == 'POST':
       form = BookmarkAddToCollectionForm(request.POST)
       if form.is_valid():
           bookmark = form.cleaned_data['bookmark']
           collection.bookmarks.add(bookmark)
           messages.success(request, 'Добавление коллекции выполнено!')
           return redirect('collections')
       else:
           messages.error(request, 'Ошибка.')
   else:
       form = BookmarkAddToCollectionForm()
   return render(request, 'collection/collections_templates/add_bookmark_to_collection.html', {'form': form})


def add_new_bookmark_to_collection(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            parametrs_for_bookmark = get_some_parameters(url=form.cleaned_data['url'])
            bookmark = Bookmark.objects.create(
                title=parametrs_for_bookmark.get('title', 'Не найдено'),
                description=parametrs_for_bookmark.get('description', 'Не найдено'),
                og_image=parametrs_for_bookmark.get('image', 'Не найдено'),
                og_type=parametrs_for_bookmark.get('type', 'website'),
                site_name=parametrs_for_bookmark.get('site_name', 'Не найдено'),
                url=form.cleaned_data['url'],
                user=request.user,
                )
            collection.bookmarks.add(bookmark)
            messages.success(request, 'Добавление новой закладки в коллекцию выполнено!')
            return redirect('collections')
        else:
            messages.error(request, 'Ошибка.')
    else:
        form = BookmarkForm()
    return render(request, 'collection/collections_templates/add_new_bookmark_to_collection.html', {'form': form})