from Directory import Directory


def main():
    path = input("Path to the directory you want to work: ")
    directory = Directory(path)
    directory.organize_dir()


if __name__ == '__main__':
    main()
