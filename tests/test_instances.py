from unittest import TestCase

from CreLanguageTranslate.dTgoogleTranslate import dTgoogleTranslate
from CreLanguageTranslate.rAPItranslator2 import rAPItranslator2
from CreLanguageTranslate.rAPImultiTraduction import rAPImultiTraduction

class TestTranslate(TestCase):

    def test_each_language(self):
      allInstances = [dTgoogleTranslate(), rAPItranslator2(), rAPImultiTraduction() ]
      for inst in allInstances:
        print(['service name: ',inst.getServiceName()])
        self.assertTrue('de' in inst.sourceLanguages)
        self.assertTrue('en' in inst.sourceLanguages) 
        self.assertTrue('de' in inst.targetLanguages)
        self.assertTrue('en' in inst.targetLanguages) 

    def test_each_translate(self):
      allInstances = [dTgoogleTranslate(), rAPItranslator2(), rAPImultiTraduction() ]
      for inst in allInstances:
        print(['service name: ',inst.getServiceName()])
        tarTree = inst.translate('tree', 'en','de')
        self.assertEqual('Baum', tarTree)
        tarHouse = inst.translate('Haus','de','en')
        self.assertEqual('house', tarHouse.lower())

        tarHail = inst.translate('Thunderstorm: hail germany', 'en','de')
        self.assertEqual('Gewitter: Hagel Deutschland', tarHail)
        tarHail2 = inst.translate('hail germany', 'en','de')
        self.assertEqual('Heil Deutschland', tarHail2)

