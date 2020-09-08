from bs4 import BeautifulSoup
import requests

def webio():
    link = "https://speckyboy.com/category/web-design/"

    source = requests.get(link).text
    soup = BeautifulSoup(source, 'html.parser')
    data = soup.find('div', class_='grid-layout')

    images = []
    link = []
    title = []
    author_link = []
    author = []
    article = []

    for d in data.find_all('article'):
        img = d.find('div',class_='grid-image').find('img').get('data-lazy-src')
        images.append(img)

        post = d.find('div', class_='information')

        l = post.find('header').find('a').get('href')
        link.append(l)

        post_heading = post.find('header').find('a').text
        title.append(post_heading)

        auth_link = post.find('header').find('div').find('span',class_='author').find('a').get('href')
        author_link.append(auth_link)
        
        auth_name = post.find('header').find('div').find('span',class_='author').find('a').text
        author.append(auth_name)

        short = post.find('footer').find('p').text
        article.append(short)

    return zip(images, link, title, author_link, author, article)
    
