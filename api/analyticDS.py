from bs4 import BeautifulSoup
import requests 

def analyticData():
    link = "https://www.analyticsvidhya.com/blog/category/data-science"

    source = requests.get(link).text
    soup = BeautifulSoup(source, 'html.parser')
    data = soup.find('div', class_ ='row block-streams el-module-2')

    link = []
    images = []
    author = []
    author_link = []
    title = []
    article = []

    for d in data.find_all('div', class_='up-up-child col-sm-6'):
        # To get Post Link
        post = d.find('article', class_='item-medium post-box-big')
        l = post.find('div', class_='thumb-wrap zoom-zoom').find('a')
        link.append(l)

        # To get article image
        img = post.find('img', class_='entry-thumb zoom-it three').get('src')
        images.append(img)

        # To get Author Name
        auth_name = post.find('div', class_='meta-info').find('span', class_='entry-author').text
        author.append(auth_name)
        
        # To get author link
        auth_link = post.find('div', class_='meta-info').find('span', class_='entry-author').find('a').get('href')
        author_link.append(auth_link)
        
        # To get Post title
        post_heading = post.find('h3', class_='entry-title').text.strip()
        title.append(post_heading)

        # To get article short summary
        short = post.find('div', class_='i-summary').text.strip()
        article.append(short)

        # To return as series of tuples
    return zip(link, images, author, author_link, title, article)

