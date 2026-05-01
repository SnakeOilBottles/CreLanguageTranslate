from unittest import TestCase
import unittest

from CreLanguageTranslate.LanguageTranslate import LanguageTranslate 
import CreLanguageTranslate 
from importlib.metadata import version

class TestTranslate(TestCase):

    class TestResult(unittest.TestResult):
        def addFailure(self, test, err):
            print('This is my own Failure')
            super(TestTranslate.TestResult, self).addFailure(test, err)
        def addError(self, test, err):
            print('This is my own Error')
            super(TestTranslate.TestResult, self).addError(test, err)

    def test_version(self):
        print(['CreLanguageTranslate: ', version("CreLanguageTranslate")])
        self.assertEqual('Version', 'Version')

    def test_simple_translate(self):
        lt = LanguageTranslate()
        li = lt.getTranslatorByLanguage('en','de')
        tarTree = li.translate('tree')
        self.assertEqual('Baum', tarTree)
        tarHouse = li.translate('house')
        self.assertEqual('Haus', tarHouse)

