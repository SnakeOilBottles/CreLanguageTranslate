from unittest import TestCase

from CreLanguageTranslate.LanguageTranslate import LanguageTranslate 
import CreLanguageTranslate 
from importlib.metadata import version

class TestTranslate(TestCase):

    def test_version(self):
        print(['CreLanguageTranslate: ', version("CreLanguageTranslate")])
        self.assertEqual('Version', 'Version')

    def test_translate(self):
        lt = LanguageTranslate()
        li = lt.getTranslatorByLanguage('en','hi')
        hiTree = li.translate('tree')
        self.assertEqual('पेड़', hiTree)
        hiHouse = li.translate('house')
        self.assertEqual('घर', hiHouse)

