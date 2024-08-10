# encoding: utf-8
import requests
from bs4 import BeautifulSoup

def get_google_news():
    url = "https://news.google.com/news/"
    response = requests.get(url)
    # soup = BeautifulSoup(response.content,
    soup = BeautifulSoup(response.content,"html.parser")
    news_list = soup.find_all("item")
    for news in news_list:
        title = news.title.text
        link = news.link.text
        print(f"標題: {title}")
        print(f"鏈接: {link}")
        print("")

if __name__ == "__main__":
    get_google_news()
