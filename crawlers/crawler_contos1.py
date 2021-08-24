from bs4 import BeautifulSoup
import requests


def get_content(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_texts():
    links = get_content('https://www.abcdobebe.com/category/comunidade/contos-infantis/')
    links = links.find('div', class_='td-ss-main-content').find_all('a')
    all_texts = []
    count = 0
    total = len(links)
    for link in links:
        count+=1
        print(count, ' de ', total)
        page_text = get_content(link['href'])
        page_text = page_text.find('div', class_='td-post-content').text.replace('\n\n', '')
        all_texts.append(page_text)   
        print(f"Added link: {link['href']}")
    return all_texts


def export_content(list):        
    with open('result_crawler_1.txt', 'w') as f:
        f.write("\n\n\n".join(list))
    

def main():
    listTexts = get_texts()
    export_content(listTexts)

if __name__ == "__main__":
    main()