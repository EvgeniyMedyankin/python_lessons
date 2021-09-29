# scraper.py
import json
from bs4 import BeautifulSoup
from time import time, sleep
from selenium import webdriver
import webbrowser

"""
Инструкция по установке geckodriver на linux
wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
tar -xvzf geckodriver*
$ chmod +x geckodriver
$ mv geckodriver /usr/local/bin/
export PATH=$PATH:/usr/local/bin/geckodriver
"""

filename = 'news.json'
url = 'https://www.ukr.net/news/technologies.html'
driver = webdriver.Firefox('/usr/local/bin/')
driver.get(url)
sleep(5)


def all_the_same(array):
    return array.count(array[-1:][0])


# def read_file():
#     with open(filename, encoding='utf-8') as f:
#         get_file_data = json.load(f)
#         for text in get_file_data[0]:
#             print(text)


height = driver.execute_script("return document.body.scrollHeight")
driver.execute_script(f"window.scrollTo(0, {height - 50}+20);")
height_data = []
while True:
    new_height = driver.execute_script("return document.body.scrollHeight")
    sleep(2)
    go_to = new_height - 20
    driver.execute_script(f"window.scrollTo(0, {go_to});")
    height_data.append(go_to)

    if all_the_same(height_data) >= 5:
        soup = BeautifulSoup(driver.page_source, 'lxml')
        news = soup.find_all('a', class_='im-tl_a')

        obj = []
        html_body = ''

        for data in news:
            link = data.get("href")
            title = data.text
            obj.append({"title": title, "link": link})
            html_body += f"<p><a href=\"{link}\">{title}</a></p>"
            print(obj)

        with open(filename, 'w') as file_object:
            file_object.write(str(obj))

        f = open('index.html', 'w')
        html_template = f"""
        <html>
            <head>
            <title>Title</title>
            </head>
            <body>
            <h2>Welcome To GFG</h2>
            <p>Default code has been loaded into the Editor.</p>
            {html_body}
            </body>
        </html>
        """
        f.write(html_template)
        f.close()
        webbrowser.open('index.html')

        driver.quit()
        # read_file()
