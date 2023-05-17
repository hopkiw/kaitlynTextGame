from unittest import TestCase
from caseinsensitivedict import CaseInsensitiveDict


class TestCaseInsensitiveDict(TestCase):
    def test_getitem(self):
        myinstance = CaseInsensitiveDict()
        myinstance['jhin'] = 4
        self.assertEqual(myinstance['jhin'], 4)
        self.assertEqual(myinstance['JHIN'], 4)
        with self.assertRaises(KeyError):
            myinstance['Liam']

    def test_setitem(self):
        myinstance = CaseInsensitiveDict()
        myinstance['Kaisa'] = 5
        myinstance['KAISA'] = 'daughter of the void'
        self.assertEqual(myinstance['Kaisa'], 'daughter of the void')

    def test_list(self):
        myinstance = CaseInsensitiveDict()
        myinstance['jhin'] = 4
        myinstance['Kaisa'] = 5
        self.assertEqual(list(myinstance), ['jhin', 'Kaisa'])

    def test_len(self):
        myinstance = CaseInsensitiveDict()
        myinstance['jhin'] = 4
        myinstance['Kaisa'] = 5
        self.assertEqual(len(myinstance), 2)

    def test_remaining(self):
        pass
        # del d[key]
        #     Remove d[key] from d. Raises a KeyError if key is not in the map.

        # myinstance = CaseInsensitiveDict()
        # myinstance['Kaisa'] = 5
        # self.assertEqual(myinstance['Kaisa'], 5)
        # del myinstance['Kaisa']
        # self.assertNotIn('Kaisa', myinstance)
        # with self.assertRaises(KeyError):
        #     myinstance['Kaisa']

        # key in d
        #     Return True if d has a key key, else False.

        # myinstance = CaseInsensitiveDict()
        # myinstance['Kaisa'] = 5
        # self.assertIn('Kaisa', myinstance)

        # key not in d
        #     Equivalent to not key in d.

        # clear()
        #     Remove all items from the dictionary.

        # copy()
        #     Return a copy of the dictionary, a new instance with the same
        #     items.

        # get(key[, default])
        #     Return the value for key if key is in the dictionary, else
        #     default.  If default is not given, it defaults to None, so that
        #     this method never raises a KeyError.

        # items()
        #     Return a new view of the dictionary’s items ((key, value) pairs).
        #     See the documentation of view objects.

        # keys()
        #     Return the dictionary’s keys.

        # pop(key[, default])
        #     If key is in the dictionary, remove it and return its value, else
        #     return default. If default is not given and key is not in the
        #     dictionary, a KeyError is raised.

        # popitem()
        #     Remove and return a (key, value) pair from the dictionary.  Pairs
        #     are returned in LIFO order.

        # setdefault(key[, default])
        #     If key is in the dictionary, return its value. If not, insert key
        #     with a value of default and return default.  default defaults to
        #     None.

        # update([other])
        #     Update the dictionary with the key/value pairs from other,
        #     overwriting existing keys. Return None.
        #
        #     update() accepts either another dictionary object or an iterable
        #     of key/value pairs (as tuples or other iterables of length two).
        #     If keyword arguments are specified, the dictionary is then
        #     updated with those key/value pairs: d.update(red=1, blue=2).

        # values()
        #     Return a new view of the dictionary’s values. See the documentation
        #     of view objects.
