import os


def print_directory_entries(dirname):
    # dirname =
    entries = os.listdir(dirname)
    print(f'The list is: {entries}')
    for entry in entries:
        entrypath = dirname + '/' + entry
        if os.path.isdir(entrypath):
            print(f'{entrypath} is a directory')
            print_directory_entries(entrypath)
        else:
            print(f'{entrypath} is not a directory')


if __name__ == '__main__':
    print_directory_entries('/Users/kaitlynmodz/PycharmProjects/dirtest')
