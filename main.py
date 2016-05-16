from bs4 import BeautifulSoup
import requests
import os

def download_newest_post():
    comic = requests.get("http://xkcd.com/info.0.json").json()
    img = requests.get(comic['img'])
    with open("img.png", 'wb') as pic:
        for chunk in img.iter_content(4096):
            pic.write(chunk)
    os.system("open img.png")

def main():
    download_newest_post()

if __name__ == '__main__':
    main()
