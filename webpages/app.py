
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
def scrape_youtube():
    url = 'https://www.youtube.com/feed/trending'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    videos = soup.find_all('h3', {'class': 'yt-lockup-title'})
    return [video.a['title'] for video in videos]
def scrape_amazon():
    url = 'https://www.amazon.com/best-sellers-books-Amazon/zgbs/books'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('div', {'class': 'p13n-sc-truncate'})
    return [book.get_text().strip() for book in books]

@app.route('/')
def index():
    youtube_data = scrape_youtube()
    amazon_data = scrape_amazon()
    return render_template('index.html', youtube_data=youtube_data, amazon_data=amazon_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5002)
