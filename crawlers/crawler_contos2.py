from bs4 import BeautifulSoup
import requests


def get_content(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_texts():
    links = get_content('https://www.grimmstories.com/pt/grimm_contos/list')
    links = links.find('ul', class_='bluelink').find_all('a')
    all_texts = []
    count = 0
    total = len(links)
    for link in links:
        count+=1
        print(count, ' de ', total)
        page_text = get_content(link['href'])
        page_text = page_text.find('div', class_='text').text.replace('\n\n', '')
        all_texts.append(page_text)   
        print(f"Added link: {link['href']}")
    return all_texts


def export_content(list):        
    with open('input.txt', 'w') as f:
        f.write("\n\n\n".join(list))
    

def main():
    listTexts = get_texts()
    export_content(listTexts)

if __name__ == "__main__":
    main()