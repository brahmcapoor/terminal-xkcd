from xkcd_utils import load_database
from xkcd_menu import show_menu
from xkcd_comic import xkcdcomic


def main():
    database = load_database()
    show_menu(database)

if __name__ == '__main__':
    main()
