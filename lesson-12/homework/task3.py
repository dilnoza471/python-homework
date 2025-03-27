import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def get_data():
    chrome_options = Options()
    chrome_options.add_argument("--window-position=0, 0")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.demoblaze.com/")
    time.sleep(3)
    laptop = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div[1]/div/a[3]')
    laptop.click()
    time.sleep(3)
    next_btn = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div[2]/form/ul/li[2]')
    next_btn.click()
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    card_blocks = soup.find_all('div', class_='card-block')
    laptops = []
    for card in card_blocks:
        name = card.find('a').text
        price = card.find('h5').text
        description = card.find('p').text
        laptops.append({'name': name, 'price': price, 'description': description})
    with open('laptops.json', 'w', newline='') as file:
        json.dump(laptops, file, indent=4)
if __name__ == "__main__":
    get_data()