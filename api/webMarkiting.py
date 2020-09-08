from bs4 import BeautifulSoup
import requests

def webMark():
    link = "https://www.web-savvy-marketing.com/category/website-development/"

    source = requests.get(link).text
    soup = BeautifulSoup(source, 'html.parser')
    data = soup.find('main', class_='content')
    
    images = []
    link = []
    title = []
    article = []

    for d in data.find_all('article'):
        img = d.find('header', class_='entry-header').find('img').get('src')
        images.append(img)

        l = d.find('h2', class_='entry-title').find('a').get('href')
        link.append(l)

        post_heading = d.find('h2', class_='entry-title').find('a').text
        title.append(post_heading)

        short = d.find('div', class_='entry-content').find('p').text
        article.append(short)

    return zip(images, link, title, article)
