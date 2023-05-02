# Valid actions:
# Inventory
# Location ('looking around')
# Pick up
# Use
# Examine
# Go left
# Go right
# Go forward
# Go back
# Room number, x position, y position, title, description, items

import csv

x = 0
y = 0
location = None
inventory = {}
shouldprint = True


class Item:
    def __init__(self, name, description, setting):
        self.name = name
        self.description = description
        self.setting = setting


class Location:
    def __init__(self, title, description, items):
        self.title = title
        self.description = description
        self.items = items


def passfunc():
    pass


def main():
    global shouldprint
    global location
    location = parse_game_data()
    print('Welcome to the game.')
    name = input('Name: ')
    print(f'Welcome to the game, {name}.')
    userinput = ''
    while userinput != 'Quit':
        curr = location[(x, y)]
        if shouldprint:
            print(curr.title)
            print(curr.description)
            for i in curr.items:
                print(curr.items[i].setting)
            shouldprint = False
            # if shouldprint were not set to false after this while loop, the location title, description,
            # and item setting would print after every command
        userinput = input('>>> ')
        check_input(userinput)
    print('You opted to quit the game.')


def pick_up(userinput):
    global location
    global inventory
    items = userinput.split()
    if len(items) != 3:
        print("You can't do that.")
        return
    item = items[2]
    for i in location[(x, y)].items:
        if item == i.lower():
            r = location[(x, y)].items.pop(i)
            inventory[i] = r.description
            print(f"{i} has been added to your Inventory.")
            return
    print(f"There's no {item} here.")


def inventory_func(userinput):
    out = 'Your inventory contains: '
    sep = ', '.join(inventory.keys())
    print(out + sep + '.')


def examine(userinput):
    items = userinput.split()
    if len(items) != 2:
        print("You can't do that.")
        return
    item = items[1]
    for i in inventory:
        if item == i.lower():
            print(inventory[i])


def go_left(userinput):
    global shouldprint
    global x
    if (x - 1, y) in location:
        x = x - 1
        shouldprint = True
    else:
        print("You can't do that.")


def go_right(userinput):
    global shouldprint
    global x
    if (x + 1, y) in location:
        x = x + 1
        shouldprint = True
    else:
        print("You can't do that.")


def go_up(userinput):
    global shouldprint
    global y
    if (x, y + 1) in location:
        y = y + 1
        shouldprint = True
    else:
        print("You can't do that.")


def go_down(userinput):
    global shouldprint
    global y
    if (x, y - 1) in location:
        y = y - 1
        shouldprint = True
    else:
        print("You can't do that.")


def check_input(userinput):
    global shouldprint
    global location
    global x
    global y
    functionmap = {'Inventory': inventory_func, 'Location': passfunc, 'Pick up': pick_up, 'Use': passfunc,
                   'Examine': examine, 'Go left': go_left, 'Go right': go_right, 'Go up': go_up,
                   'Go down': go_down}
    for i in functionmap:
        if userinput.startswith(i):
            func = functionmap[i]
            func(userinput)
            return
    # print an error message if we didn't find the valid command in functionmap:
    print("You definitely can't do that.")


def parse_game_data(filename='gamedata.csv'):
    datafile = open(filename)
    csvreader = csv.reader(datafile)
    locations = {}
    for line in csvreader:
        x = int(line[1])
        y = int(line[2])
        items = line[5:]
        itemsdict = {}
        if len(items) > 1:
            for i in range(0, len(items), 3):
                itemname = items[i]
                itemsetting = items[i+1]
                itemdescription = items[i+2]
                itemsdict[itemname] = Item(itemname, itemdescription, itemsetting)
        locations[(x, y)] = Location(line[3], line[4], itemsdict)
        #locations = {
        #             (0,0): Location
        #                     title=...
        #                     description=...
        #                     items={
        #                               'Rope': Item(name=..., description=...)
        #                               'Dagger': Item(name=..., description=...)
        #                     },
        #             (-1,0): Location(...)
        #            }
    return locations


if __name__ == '__main__':
    main()