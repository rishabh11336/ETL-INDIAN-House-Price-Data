import selenium as se
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


from bs4 import BeautifulSoup
import requests as req

import time
import csv

def open_browser(url, city):
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get(url)
    a=10000
    for i in range(60):
        driver.execute_script("window.scrollTo(0, {});".format(a))
        time.sleep(3)
        a += 10000
        print(i)
        print("****************")
    with open(f"MB_{city}.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    return driver.quit()


def get_html(url):
    response = req.get(url)
    return response.text if response.status_code == 200 else None 

def get_soup(html):
    return BeautifulSoup(html, 'html.parser')

def get_cards(soup):
    return [html for html in soup.find_all('div', class_='mb-srp__list')]

def main():
    with open('MagicBricks Link Tier1 City.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            city = lines[0]
            url = lines[1]


            open_browser(url, city)
            # read html from mb.html
            with open(f'MB_{city}.html', 'r', encoding='utf-8') as f:
                html = f.read()
            if html:
                soup = get_soup(html)
                cards = get_cards(soup)
                with open(f'MBHouse_{city}.csv', 'w', encoding='utf-8') as f:
                    f.write('property_title, society_name, carpet_area, status, floor_info,transaction_type, furnishing_type, facing, ownership_type, car_parking, bathroom_count, balcony_count, price_amount, price_per_sqft \n')
                    for soup in cards:
                        property_title_element = soup.find('h2', class_='mb-srp__card--title')
                        property_title = property_title_element.text.strip() if property_title_element else None
                        property_title = property_title.replace(',', ' ')
                        
                        society_name_element = soup.find('a', class_='mb-srp__card__society--name')
                        society_name = society_name_element.text.strip() if society_name_element else None
                        society_name = society_name.replace(',', ' ') if society_name else None

                        carpet_area_element_1 = soup.find('div', {'data-summary': 'carpet-area'})
                        carpet_area_element = carpet_area_element_1.find('div', class_='mb-srp__card__summary--value') if carpet_area_element_1 else None
                        carpet_area = carpet_area_element.text.strip() if carpet_area_element else None
                        carpet_area = carpet_area.replace(',', ' ') if carpet_area else None
                        if not carpet_area:
                            carpet_area_element_1 = soup.find('div', {'data-summary': 'super-area'})
                            carpet_area_element = carpet_area_element_1.find('div', class_='mb-srp__card__summary--value') if carpet_area_element_1 else None
                            carpet_area = carpet_area_element.text.strip() if carpet_area_element else None
                            carpet_area = carpet_area.replace(',', ' ') if carpet_area else None
                        
                        status_element_1 = soup.find('div', {'data-summary': 'status'})
                        status_element = status_element_1.find('div', class_='mb-srp__card__summary--value') if status_element_1 else None
                        status = status_element.text.strip() if status_element else None
                        status = status.replace(',', ' ') if status else None
                        
                        floor_info_element_1 = soup.find('div', {'data-summary': 'floor'})
                        floor_info_element = floor_info_element_1.find('div', class_='mb-srp__card__summary--value') if floor_info_element_1 else None
                        floor_info = floor_info_element.text.strip() if floor_info_element else None
                        floor_info = floor_info.replace(',', ' ') if floor_info else None
                        
                        transaction_type_element_1 = soup.find('div', {'data-summary': 'transaction'})
                        transaction_type_element = transaction_type_element_1.find('div', class_='mb-srp__card__summary--value') if transaction_type_element_1 else None
                        transaction_type = transaction_type_element.text.strip() if transaction_type_element else None
                        transaction_type = transaction_type.replace(',', ' ') if transaction_type else None
                        
                        furnishing_type_element_1 = soup.find('div', {'data-summary': 'furnishing'})
                        furnishing_type_element = furnishing_type_element_1.find('div', class_='mb-srp__card__summary--value') if furnishing_type_element_1 else None
                        furnishing_type = furnishing_type_element.text.strip() if furnishing_type_element else None
                        furnishing_type = furnishing_type.replace(',', ' ') if furnishing_type else None
                        
                        facing_element_1 = soup.find('div', {'data-summary': 'facing'})
                        facing_element = facing_element_1.find('div', class_='mb-srp__card__summary--value') if facing_element_1 else None
                        facing = facing_element.text.strip() if facing_element else None
                        facing = facing.replace(',', ' ') if facing else None
                        
                        ownership_type_element_1 = soup.find('div', {'data-summary': 'ownership'})
                        ownership_type_element = ownership_type_element_1.find('div', class_='mb-srp__card__summary--value') if ownership_type_element_1 else None
                        ownership_type = ownership_type_element.text.strip() if ownership_type_element else None
                        ownership_type = ownership_type.replace(',', ' ') if ownership_type else None
                        
                        car_parking_element_1 = soup.find('div', {'data-summary': 'parking'})
                        car_parking_element = car_parking_element_1.find('div', class_='mb-srp__card__summary--value') if car_parking_element_1 else None
                        car_parking = car_parking_element.text.strip() if car_parking_element else None
                        car_parking = car_parking.replace(',', ' ') if car_parking else None
                        
                        bathroom_count_element_1 = soup.find('div', {'data-summary': 'bathroom'})
                        bathroom_count_element = bathroom_count_element_1.find('div', class_='mb-srp__card__summary--value') if bathroom_count_element_1 else None
                        bathroom_count = bathroom_count_element.text.strip() if bathroom_count_element else None
                        bathroom_count = bathroom_count.replace(',', ' ') if bathroom_count else None
                        
                        balcony_count_element_1 = soup.find('div', {'data-summary': 'balcony'})
                        balcony_count_element = balcony_count_element_1.find('div', class_='mb-srp__card__summary--value') if balcony_count_element_1 else None
                        balcony_count = balcony_count_element.text.strip() if balcony_count_element else None
                        balcony_count = balcony_count.replace(',', ' ') if balcony_count else None
                        
                        price_amount_element = soup.find('div', class_='mb-srp__card__price--amount')
                        price_amount = price_amount_element.text.strip() if price_amount_element else None
                        price_amount = price_amount.replace(',', ' ') if price_amount else None
                        
                        price_per_sqft_element = soup.find('div', class_='mb-srp__card__price--size')
                        price_per_sqft = price_per_sqft_element.text.strip() if price_per_sqft_element else None
                        price_per_sqft = price_per_sqft.replace(',', ' ') if price_per_sqft else None

                        f.write(f'{property_title}, {society_name}, {carpet_area}, {status}, {floor_info},{transaction_type}, {furnishing_type}, {facing}, {ownership_type}, {car_parking}, {bathroom_count}, {balcony_count}, {price_amount}, {price_per_sqft}\n')
               
            else:
                print('Error: Could not get html')
            print("Done")
    return

if __name__ == '__main__':
    main()