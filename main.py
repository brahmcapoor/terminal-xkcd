from bs4 import BeautifulSoup
import requests
import os
import pickle

class xkcdcomic():
    def __init__(self, json):
        self.title = json['title']
        self.number = int(json['num'])
        self.alt = json['alt']
        self.transcript = json['transcript']
        self.link = json['img']
    def __str__(self):
        return(("{}: {}").format(self.title, self.link))

def generate_database():
    newest_num = requests.get("http://xkcd.com/info.0.json").json()['num']
    database = {}
    for i in range(1,newest_num+1):
        num = str(i)
        print(num)
        url = ("http://xkcd.com/{}/info.0.json").format(num)
        try:
            jsondata = requests.get(url).json()
            comic = xkcdcomic(jsondata)
            database[comic.number] = comic
        except: continue
    with open('xkcd_database.pickle', 'wb') as f:
        pickle.dump(database,f)
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
    number_comics = str(len(database))
    number = int(input("Comic number? The most recent comic is number " + number_comics + ". "))
    number = int(input("Comic number? Type 0 for most current comic: "))
    comic = database[number]
    url = comic.link
    img = requests.get(url)
    download_comic(img)
    os.system("open img.png")
    show_prompt(comic)

if __name__ == '__main__':
    main()
