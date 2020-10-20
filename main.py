import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']


def habr_scrapper():
    ret = requests.get('https://habr.com/ru/all/')
    soup = BeautifulSoup(ret.text, 'html.parser')
    posts = soup.find_all('article', class_='post')

    post_collection = []
    for post in posts:
        title = post.find('a', class_='post__title_link')
        title_text = title.text
        title_link = title.attrs.get('href')
        date = post.find('span', class_='post__time')
        title_date = date.text
        for keyword in KEYWORDS:
            if keyword in post.text.lower():
                post_collection.append([title_text, title_link, title_date])

    return post_collection

articles_info = habr_scrapper()

for item in articles_info:
    print(f'Название поста: {item[0]}\n'
          f'Ссылка на пост: {item[1]}\n'
          f'Дата публикации: {item[2]}\n')
