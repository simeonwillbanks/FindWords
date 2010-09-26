#!/usr/bin/env python
# encoding: utf-8
"""
unittests.py

Unit tests for findwords module

Created by Simeon F. Willbanks on 2010-09-23.
"""


import unittest
import findwords


class TestFindWords(unittest.TestCase):
    def setUp(self):
        """Set regex used in all tests"""
        self.regex = "^[^aeiouy]{3}$"
    
    
    def test_wordslist(self):
        """$ cat /usr/share/dict/words | wc -l
          234936
        
        """
        wlist = findwords.wordslist()
        self.assertEqual(len(wlist), 234936)

    
    def test_wordsfilter(self):
        """$ egrep "^[^aeiouy]{3}$" /usr/share/dict/words
        Aht
        Alb
        Alf
        Ann
        Art
        cwm
        Emm
        grr
        Ind
        Ing
        Mrs
        nth
        Ods
        Odz
        Osc
        pst
        tch
        tck
        tst
        Uds
        
        """
        wlist = findwords.wordsfilter(findwords.wordslist(), self.regex)
        self.assertEqual(len(wlist), 20)
        self.assertEqual(wlist, ["Aht",
                                 "Alb",
                                 "Alf",
                                 "Ann",
                                 "Art",
                                 "cwm",
                                 "Emm",
                                 "grr",
                                 "Ind",
                                 "Ing",
                                 "Mrs",
                                 "nth",
                                 "Ods",
                                 "Odz",
                                 "Osc",
                                 "pst",
                                 "tch",
                                 "tck",
                                 "tst",
                                 "Uds"])

    
if __name__ == '__main__':
    unittest.main()