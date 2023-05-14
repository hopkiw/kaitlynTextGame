import os


def print_directory_entries(dir_name):
    # dirname =
    print(dir_name)
    entries = os.listdir(dir_name)
    files = []
    directories = []
    for entry in entries:
        entry_path = dir_name + '/' + entry
        if os.path.isdir(entry_path):
            directories.append(entry_path)
        else:
            files.append(entry)
    for file in files:
        print(file)
    for directory in directories:
        print_directory_entries(directory)


if __name__ == '__main__':
    # print_directory_entries('/Users/kaitlynmodz/PycharmProjects/dirtest')
    print_directory_entries('/')

