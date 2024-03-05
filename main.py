import selenium as se
from bs4 import BeautifulSoup
import requests as req



def get_html(url):
    response = req.get(url)
    return response.text if response.status_code == 200 else None 

def get_soup(html):
    return BeautifulSoup(html, 'html.parser')

def get_links(soup):
    return [a['href'] for a in soup.find_all('a', href=True)]

def main():
    url = 'https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=4,1,5,2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Noida&BudgetMin=5-Lacs&BudgetMax=20-Crores'
    html = get_html(url)
    if html:
        soup = get_soup(html)
        links = get_links(soup)
        print(links)
    else:
        print('Error: Could not get html')
    return

if __name__ == '__main__':
    main()