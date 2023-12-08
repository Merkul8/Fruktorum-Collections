from django.shortcuts import redirect
import requests
from bs4 import BeautifulSoup

CONTENT = [
    'og:description',
    'og:type',
    'og:site_name',
    'og:title',
    'og:image',
]

def is_og_property(tag):
   global CONTENT
   return tag.name == 'meta' and tag.get('property') in CONTENT

def get_some_parameters(url):
    """
    Получение нужных отсортированных данный для заполнения
    информации о закладке
    """
    responce = requests.get(url)
    if responce.status_code == 200:
        soup = BeautifulSoup(responce.text, 'html.parser')
        try:
            res = soup.find_all(is_og_property)
            res = {meta_tag.get('property')[3:]: meta_tag.get('content') for meta_tag in res}
            if not res.get('description'):
                description = soup.find('meta', attrs={'name': 'description'})
                res['description'] = description.get('content')
            if not res.get('title'):
                title = soup.find('title')
                res['title'] = title.text
        except:
            print('Не было найдено Open Graph разметки')
    else:
        if responce.status_code == 404:
            print('Страница не найдена')
        else:
            print('Не удалось получить страницу, статус-код: ', responce.status_code)
        return redirect('bookmarks')
    return res
