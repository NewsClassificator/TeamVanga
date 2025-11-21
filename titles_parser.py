import collections

collections.Callable = collections.abc.Callable
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from collections.abc import Callable
from time import sleep


# Выбираем категории, которые будем парсить
clickbait_sites = [
    'https://ria.ru/politics/',
    # 'https://ria.ru/society/',
    # 'https://ria.ru/science/',
    # 'https://ria.ru/culture/',
    # 'https://ria.ru/world/',
    # 'https://ria.ru/economy/',
    # 'https://ria.ru/religion/'
]

chrome_options = Options()
chrome_options.add_argument("--headless")  # отключаем чтобы не показывалось окно в котором код что-то делает

driver = webdriver.Chrome(options=chrome_options)


def get_titles_from_site(url):
    try:
        driver.get(url)
        # в range - кол-во прокруток страницы до конца(подгружаем еще посты)
        for i in range(1):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        titles = [title.text.strip() for title in
                  soup.find_all('a', {"class": "list-item__title color-font-hover-only"})]

        return titles
    except Exception as e:
        print(f"Ошибка при обработке {url}: {e}")
        return []


counter = 0
for i in clickbait_sites:
    for title in get_titles_from_site(i):
        print(title)
        counter += 1

print(counter)
