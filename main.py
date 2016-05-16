from bs4 import BeautifulSoup
import requests
import os



def search_posts(keyword):
    all_comics = requests.get('https://www.explainxkcd.com/wiki/index.php/List_of_all_comics_(full)').text
    soup = BeautifulSoup(all_comics, "html.parser")
    table = soup.find("table")
    for row in table.findAll('tr'):
        for col in table.findAll('td'):
            #TODO: data structure representing comic


def download_newest_post():
    comic = requests.get("http://xkcd.com/info.0.json").json()
    img = requests.get(comic['img'])
    with open("img.png", 'wb') as pic:
        for chunk in img.iter_content(4096):
            pic.write(chunk)
    print(("Comic title: {}").format(comic['safe_title']))
    print(("Alt text: {}").format(comic['alt']))
    print("Opening comic...")
    os.system("open img.png")
    input("Press ENTER to delete the comic from storage")
    os.system("rm -rf img.png")

def main():
    download_newest_post()
    search_posts("")

if __name__ == '__main__':
    main()
