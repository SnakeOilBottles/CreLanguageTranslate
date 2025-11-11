from unittest import TestCase

from CreLanguageTranslate.googleTranslate import googleTranslate
from CreLanguageTranslate.rAPItranslator2 import rAPItranslator2

class TestTranslate(TestCase):

    def test_each_language(self):
      allInstances = [googleTranslate(), rAPItranslator2() ]
      for inst in allInstances:
        self.assertTrue('de' in inst.sourceLanguages)
        self.assertTrue('en' in inst.sourceLanguages) 
        self.assertTrue('de' in inst.targetLanguages)
        self.assertTrue('en' in inst.targetLanguages) 

    def test_each_translate(self):
      allInstances = [googleTranslate(), rAPItranslator2() ]
      for inst in allInstances:
        tarTree = inst.translate('tree', 'en','de')
        self.assertEqual('Baum', tarTree)
        tarHouse = inst.translate('Haus','de','en')
        self.assertEqual('house', tarHouse.lower())

