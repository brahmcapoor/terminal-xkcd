from bs4 import BeautifulSoup
import requests
import os

def download_newest_post():
    page = requests.get("http://www.xkcd.com").text
    soup = BeautifulSoup(page, "html.parser")
    imagelink = soup.find(id="comic")
    img = imagelink.find("img")
    img = "http:" + img['src']
    img = requests.get(img)
    with open("img.png", 'wb') as pic:
        for chunk in img.iter_content(4096):
            pic.write(chunk)
    os.system("open img.png")

def main():
    download_newest_post()

if __name__ == '__main__':
    main()
