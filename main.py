import requests
import os

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

if __name__ == '__main__':
    main()
