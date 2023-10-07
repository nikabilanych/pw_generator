#! python3

import sys
import pyperclip
import shelve
# run through terminal
# saves password from the clipboard to shelve database file


def main():
    """
    commands: save *name* - save password from clipboard with given key name

    """
    storage = shelve.open('storage')
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        # keyword gets stored into the storage object as a key:value
        # checks if the key exists or not
        if sys.argv[2] not in storage:
            storage[sys.argv[2]] = pyperclip.paste()
        else:
            print(f"keyword '{sys.argv[2]}' already exists")
            print("to update existing keyword's content, type: update")
            print("to add into existing keyword, type: add")
            print("to delete existing keyword, type: del")

            usr = input()
            if usr.lower() == 'update':
                storage[sys.argv[2]] = pyperclip.paste()
                print("keyword content updated")
                sys.exit()
            if usr.lower() == 'add':
                storage[sys.argv[2]] += pyperclip.paste()
                print("clipboard content added")
            if usr.lower() == 'del':
                del storage[sys.argv[2]]
                print("keyword deleted")

            else:
                print('No changes performed')
                sys.exit()
    elif len(sys.argv) == 2:
        storage = shelve.open('storage')
        if sys.argv[1] == 'list':
            pyperclip.copy(str(list(storage.keys())))
        if sys.argv[1] in storage:
            pyperclip.copy(storage[sys.argv[1]])
    storage.close()


if len(sys.argv) > 1:
    main()
