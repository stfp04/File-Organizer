import os
from Directory import Directory


def main():
    command = None

    path = input("Path to the directory you want to work: ")
    while not os.path.exists(path):
        print("\n\tThat directory doesn't exists!\n")
        path = input("Path to the directory you want to work: ")

    directory = Directory(path)

    while command != 'quit':
        command = input("> ")
        if "dir -o" in command:
            if command == "dir -o -rd":
                directory.rmvdup()

            directory.organize_dir()
        elif command == "dir -p":
            directory.list_all_pdf()
        elif command == "dir -w":
            directory.list_all_docx()
        elif command == "dir -t":
            directory.list_all_txt()
        elif command != 'quit':
            print("Sorry, that command is not valid")
        else:
            print("Unknown syntax")


if __name__ == '__main__':
    main()
