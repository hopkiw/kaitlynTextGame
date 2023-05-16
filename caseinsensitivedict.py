class CaseInsensitiveDict:
    def __init__(self):
        self.dict = {}

    def __getitem__(self, key):
        print('I was called.')
        for i in self.dict:
            if i.lower() == key.lower():
                return self.dict[i]
        raise KeyError('That is not correct.')

    def __setitem__(self, key, value):
        # key = 'Snake' value = 5
        existing = None
        for i in self.dict:
            if i.lower() == key.lower():
                existing = i
                break
        if existing:
            del self.dict[existing]
        self.dict[key] = value
    def __iter__(self):
        return iter(self.dict)
    def __len__(self):
        return len(self.dict)


if __name__ == '__main__':
    myinstance = CaseInsensitiveDict()
    myvariable = myinstance['jhin']
    # myvariable = myinstance.__getitem__('jhin')
    # myvariable = myinstance.__getitem__(myinstance, 'jhin')
    print(f'myvariable is {myvariable}')
    myinstance['Kaisa'] = 5
    print(f'Kaisa is', myinstance['Kaisa'])
    myinstance['KAISA'] = 'daughter of the void'
    print(f'Kaisa is now', myinstance['Kaisa'])
    # 1. Get a value by key
    # 2. Set a value by key
    # 3. Delete a value by key
    # j['Jhin'] = 4
    # j = {'Key': (value1, value2), 'Jhin': 4}
    # j['jhin'] = 5
    # j = {'Key': (value1, value2), 'Jhin': 4, 'jhin': 5}
    # j = {'Key': (value1, value2), 'jhin': 5}
    # del j['jhin']
    # j = {'Key': (value1, value2)}