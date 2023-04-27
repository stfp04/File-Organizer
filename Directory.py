from file_func import *


class Directory:
    def __init__(self, path):
        self.path = path
        self.files = []
        self.dir = []
        self.set_attributes()

    def set_attributes(self):
        for item in os.listdir(self.path):
            fullpath = os.path.join(self.path, item)
            if os.path.isfile(fullpath):
                self.files.append(item)
            else:
                self.dir.append(item)

    def make_dir(self, directory):
        if not os.path.exists((os.path.join(self.path, directory))):
            os.mkdir(os.path.join(self.path, directory))

    def organize_dir(self):
        folder_paths = {}

        for ext, directory in extension.items():
            self.make_dir(directory)
            path = os.path.join(self.path, directory)
            folder_paths.update({ext: path})

        for file in os.listdir(self.path):
            fullpath = os.path.join(self.path, file)
            if os.path.isfile(fullpath):
                _, ext = os.path.splitext(file)
                move_file(fullpath, folder_paths.get(ext))
            else:
                if file not in extension.values():
                    file = Directory(fullpath)
                    file.organize_dir()

    def list_all_pdf(self):
        changed = False
        for _, _, file in os.walk(self.path):
            name, ext = os.path.splitext(file)
            if ext == ".pdf":
                changed = True
                print(name, end=" ")

        if changed:
            print()
        else:
            print("There are no pdf files in this directory")

    def list_all_docx(self):
        changed = False
        for _, _, file in os.walk(self.path):
            name, ext = os.path.splitext(file)
            if ext == ".docx":
                changed = True
                print(name, end=" ")

        if changed:
            print()
        else:
            print("There are no pdf files in this directory")

    def list_txt(self):
        changed = False
        for _, _, file in os.walk(self.path):
            name, ext = os.path.splitext(file)
            if ext == ".txt":
                changed = True
                print(name, end=" ")

        if changed:
            print()
        else:
            print("There are no pdf files in this directory")


extension = {
    ".pdf": "Pdf",
    ".docx": "Word",
    ".txt": "Text",
    ".pptx": "Powerpoints",
    ".jpeg": "Images",
    ".zip": "Zips"
}
