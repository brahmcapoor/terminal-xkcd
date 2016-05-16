from bs4 import BeautifulSoup
import requests
import os

class xkcdcomic():
    def __init__(self, json):
        self.title = json['title']
        self.number = int(json['num'])
        self.alt = json['alt']
        self.transcript = json['transcript']
        self.link = json['img']

def generate_database():
    newest_num = requests.get("http://xkcd.com/info.0.json").json()['num']
    database = {}
    for i in range(1,newest_num+1):
        num = str(i)
        print(num)
        url = ("http://xkcd.com/{}/info.0.json").format(num)
        try:
            json = requests.get(url).json()
            comic = xkcdcomic(json)
            database[comic.number] = comic
        except: continue
    return database

def download_comic(img):
    with open("img.png", 'wb') as pic:
        for chunk in img.iter_content(4096):
            pic.write(chunk)

def show_prompt(comic):
    print(("Comic title: {}").format(comic.title))
    print(("Alt text: {}").format(comic.alt))
    print("Opening comic...")
    os.system("open img.png")
    input("Press ENTER to delete the comic from storage")
    os.system("rm -rf img.png")


def main():
    print("Generating database...")
    database = generate_database()
    number = int(input("Comic number? Type 0 for most current comic: "))
    comic = database[number]
    url = comic.link
    img = requests.get(url)
    download_comic(img)
    os.system("open img.png")
    show_prompt(comic)

if __name__ == '__main__':
    main()
