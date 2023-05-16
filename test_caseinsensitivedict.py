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