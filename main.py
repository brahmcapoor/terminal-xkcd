from bs4 import BeautifulSoup
from tqdm import tqdm
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


def load_database():
    database = list()
    if(os.path.isfile('xkcd_database.pickle')):
        with open('xkcd_database.pickle', 'rb') as f:
            database = pickle.load(f)

    # get number of newest comic
    newest_num = requests.get("http://xkcd.com/info.0.json").json()['num']
    if(len(database) + 1 == newest_num):
        print("Database up to date!")
        return database
    else:
        print("Generating database...")
        for i in tqdm(range(len(database), newest_num + 1)):
            # create database of comics to search through
            num = str(i)
            url = ("http://xkcd.com/{}/info.0.json").format(num)
            try:
                jsondata = requests.get(url).json()
                comic = xkcdcomic(jsondata)
                entry = (comic.number, comic.title, comic)
                database.append(entry)
            except:
                continue
        with open('xkcd_database.pickle', 'wb') as f:
            # save database to file
            pickle.dump(database, f)
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


def download_and_show(comic):
    url = comic.link
    img = requests.get(url)
    download_comic(img)
    os.system("open img.png")
    show_prompt(comic)


def num_find(database):
    number_comics = str(len(database) + 1)
    number = int(
        input(
            "Comic number? The most recent comic is number " +
            number_comics +
            ". "))
    comic = None
    for entry in database:
        if entry[0] == number:
            comic = entry[2]
    if comic is None:
        print("Invalid comic number!")
        return
    download_and_show(comic)


def title_find(database):
    title = input("Comic title? ")
    comic = None
    for entry in database:
        if entry[1].lower() == title.lower():
            comic = entry[2]
    if comic is None:
        print("Couldn't find that title!")
        return
    download_and_show(comic)


def show_menu(database):
    print("What do you want to do? ")
    print("      To find a comic by number, type 'n'")
    print("      To find a comic by title, type 't'")
    print("      To search for a comic, type 's'")
    choice = input("Your choice: ")

    if choice == "n":
        num_find(database)
    elif choice == "t":
        title_find(database)
    elif choice == "s":
        pass
    else:
        print("Invalid choice!")


def main():
    database = load_database()
    show_menu(database)


if __name__ == '__main__':
    main()
