from unittest import TestCase

from CreLanguageTranslate.LanguageTranslate import LanguageTranslate 
import CreLanguageTranslate 
from importlib.metadata import version

class TestTranslate(TestCase):

    def test_version(self):
        print(['CreLanguageTranslate: ', version("CreLanguageTranslate")])
        self.assertEqual('Version', 'Version')

    def test_indirect_translate(self):
        lt = LanguageTranslate()
        li1 = lt.getTranslatorByLanguage('pl','en')
        li2 = lt.getTranslatorByLanguage('en','la')

        enTree = li1.translate('drzewo')
        self.assertEqual('tree', enTree)
        laTree = li2.translate(enTree)
        self.assertEqual('arbor', laTree)

        enHouse = li1.translate('dom')
        self.assertEqual('house', enHouse)
        laHouse = li2.translate(enHouse)
        self.assertEqual('domus', laHouse)


    def test_direct_translate(self):
        lt = LanguageTranslate()
        li = lt.getTranslatorByLanguage('pl','la')
        laTree = li.translate('drzewo')
        self.assertEqual('arbor', laTree)
        laHouse = li.translate('dom')
        self.assertEqual('domus', laHouse)

