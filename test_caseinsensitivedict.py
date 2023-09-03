from unittest import TestCase
from caseinsensitivedict import CaseInsensitiveDict, isequal


class TestCaseInsensitiveDict(TestCase):
    def setUp(self):
        self.cidict = CaseInsensitiveDict({'jhin': 4, 'KAISA': 5, 22: 6})

    def test_isequal(self):
        self.assertTrue(isequal('hello', 'hello'))
        self.assertTrue(isequal('HELLO', 'hello'))
        self.assertTrue(isequal(22, 22))

    def test_init(self):
        self.assertDictEqual(dict(self.cidict), {'jhin': 4, 'KAISA': 5, 22: 6})

        cidict = CaseInsensitiveDict((('jhin', 4), ('KAISA', 5), (22, 6)))
        self.assertDictEqual(dict(cidict), {'jhin': 4, 'KAISA': 5, 22: 6})

        cidict = CaseInsensitiveDict(jhin=4, KAISA=5)
        self.assertDictEqual(dict(cidict), {'jhin': 4, 'KAISA': 5})

        cidict = CaseInsensitiveDict({'KAISA': 5, 22: 6}, jhin=4)
        self.assertDictEqual(dict(cidict), {'jhin': 4, 'KAISA': 5, 22: 6})

        cidict = CaseInsensitiveDict((('KAISA', 5), (22, 6)), jhin=4)
        self.assertDictEqual(dict(cidict), {'jhin': 4, 'KAISA': 5, 22: 6})

    def test_getitem(self):
        self.cidict = CaseInsensitiveDict((('jhin', 4), ('KAISA', 5), (22, 6)))

        self.assertEqual(self.cidict['jhin'], 4)
        self.assertEqual(self.cidict['JHIN'], 4)
        self.assertEqual(self.cidict['kaisa'], 5)
        self.assertEqual(self.cidict['KAISA'], 5)
        self.assertEqual(self.cidict[22], 6)

        with self.assertRaises(KeyError):
            self.cidict['Liam']

    def test_setitem(self):
        self.cidict = CaseInsensitiveDict((('jhin', 4), ('KAISA', 5), (22, 6)))

        self.cidict['Kaisa'] = 'daughter of the void'
        self.cidict[5] = True
        self.assertDictEqual(dict(self.cidict),
                             {'jhin': 4, 22: 6, 5: True,
                              'Kaisa': 'daughter of the void'})

    def test_len(self):
        self.cidict = CaseInsensitiveDict((('jhin', 4), ('KAISA', 5), (22, 6)))

        self.assertEqual(len(self.cidict), 3)

    def test_del(self):
        self.cidict = CaseInsensitiveDict((('jhin', 4), ('KAISA', 5), (22, 6)))

        del self.cidict['Kaisa']
        del self.cidict[22]
        self.assertDictEqual(dict(self.cidict), {'jhin': 4})

    def test_contains(self):
        self.cidict = CaseInsensitiveDict((('jhin', 4), ('KAISA', 5), (22, 6)))

        self.assertIn('Kaisa', self.cidict)
        self.assertIn(22, self.cidict)
        self.assertNotIn('Fakey', self.cidict)

    def test_clear(self):
        self.cidict = CaseInsensitiveDict((('jhin', 4), ('KAISA', 5), (22, 6)))

        self.cidict.clear()
        self.assertDictEqual(dict(self.cidict), {})

    def test_copy(self):
        self.cidict = CaseInsensitiveDict((('jhin', 4), ('KAISA', 5), (22, 6)))

        mysecondinstance = self.cidict.copy()
        self.assertEqual(self.cidict, mysecondinstance)
        self.assertIsNot(self.cidict, mysecondinstance)
