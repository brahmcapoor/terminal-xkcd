import pickle
import os
import requests
from tqdm import tqdm
from xkcd_comic import xkcdcomic


def load_database():
    database = list()
    if(os.path.isfile('xkcd_database.pickle')):
        with open('xkcd_database.pickle', 'rb') as f:
            database = pickle.load(f)
    # get number of newest comic
    newest_num = requests.get("http://xkcd.com/info.0.json").json()['num']
    print(len(database))
    print(newest_num)
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
    print(len(database))
    print(newest_num)
    with open('xkcd_database.pickle', 'wb') as f:
            # save database to file
        pickle.dump(database, f)
    return database
