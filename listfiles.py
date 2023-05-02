import os

def main():
    entries = os.listdir()
    print(f'The list is: {entries}')
    for entry in entries:
        if os.path.isdir(entry):
            print(f'{entry} is a directory')
        else:
            print(f'{entry} is not a directory')


if __name__ == '__main__':
    main()