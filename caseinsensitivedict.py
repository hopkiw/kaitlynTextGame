# vim: ts=4 sts=4 sw=4

def isequal(x, y):
    """
    If x and y are both str, returns whether x.lower() == y.lower().
    Otherwise, returns whether x == y.
    """
    if isinstance(x, str) and isinstance(y, str) and x.lower() == y.lower():
        return True
    elif x == y:
        return True
    else:
        return False


class CaseInsensitiveDict:
    def __init__(self, other=(), **kwargs):
        self.dict = dict()
        self.update(other, **kwargs)

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __delitem__(self, key):
        for i in self.dict:
            if isequal(i, key):
                break
        else:
            raise KeyError(key)

        del self.dict[i]

    def __getitem__(self, key):
        for i in self.dict:
            if isequal(i, key):
                return self.dict[i]

        raise KeyError(key)

    def __setitem__(self, key, value):
        for i in self.dict:
            if isequal(i, key):
                del self.dict[i]
                break

        self.dict[key] = value

    def __eq__(self, other):
        if not isinstance(other, (dict, CaseInsensitiveDict)):
            return False

        # Special case check: if other has two keys that only differ by case,
        # self can't possibly be equal to it.
        other_keys = []
        for key in other:
            if isinstance(key, str):
                key = key.lower()
            other_keys.append(key)

        if len(other_keys) > len(set(other_keys)):
            return False

        if len(self) != len(other):
            return False

        for key in self:
            for other_key in other:
                if isequal(other_key, key):
                    if self[key] == other[other_key]:
                        break
                    else:
                        return False

        return True

    def __iter__(self):
        return iter(self.dict)

    def __len__(self):
        return len(self.dict)

    def clear(self):
        self.dict.clear()

    def copy(self):
        return CaseInsensitiveDict(self)

    def items(self):
        return self.dict.items()

    def keys(self):
        return self.dict.keys()

    def popitem(self):
        return self.dict.popitem()

    def values(self):
        return self.dict.values()

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def setdefault(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            self[key] = default
            return default

    def update(self, other=(), **kwargs):
        if isinstance(other, (dict, CaseInsensitiveDict)):
            for key in other:
                self[key] = other[key]
        elif hasattr(other, 'keys'):
            for key in other.keys():
                self[key] = other[key]
        else:
            for key, value in other:
                self[key] = value

        for key, value in kwargs.items():
            self[key] = value
