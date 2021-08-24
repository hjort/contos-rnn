from bs4 import BeautifulSoup
import requests


def get_content(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_links(pages):
    all_links = []
    for i in range(1,pages):
        links = get_content(f'https://historiasinfantisabobrinha.wordpress.com/blog/page/{i}')
        posts = links.find_all('article', class_='post')
        for post in posts:
            
            link = post.find('h1', class_='entry-title').find('a')
            all_links.append(link['href'])
            
    return all_links


def get_text(link):
    page_content = get_content(link)
    page_content = page_content.find('div', class_='entry-content')
    paragraphs = page_content.find_all('p')
    texto = '\n'.join(p.text for p in paragraphs)
    return texto


def export_content(list):        
    with open('input_data.txt', 'w') as f:
        f.write("\n\n\n".join(list))
        

links = get_links(11)
all_texts = []
for link in links:
    texto = get_text(link)
    all_texts.append(texto)
export_content(all_texts)    
