import xkcd_comic
import os


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
    xkcd_comic.download_and_show(comic)


def title_find(database):
    title = input("Comic title? ")
    comic = None
    for entry in database:
        if entry[1].lower() == title.lower():
            comic = entry[2]
    if comic is None:
        print("Couldn't find that title!")
        return
    xkcd_utls.download_and_show(comic)


def title_search(database):
    keyword = input("Enter search term: ")

    possible_comics = list()
    for entry in database:
        if keyword.lower() in entry[1].lower():
            possible_comics.append(entry)

    num_comics = len(possible_comics)
    if num_comics == 0:
        print("Couldn't find any comics with that search term!")
        return

    print("Results:")
    for i in range(len(possible_comics)):
        print(("{}) {}").format(i + 1, possible_comics[i][2].title))

    # TODO: Check if integer
    choice = int(input("Enter the number of the comic you want to see: "))
    comic = possible_comics[choice - 1][2]
    xkcd_comic.download_and_show(comic)


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
        title_search(database)
    else:
        print("Invalid choice!")
