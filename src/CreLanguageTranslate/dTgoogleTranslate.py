from CreLanguageTranslate.TranslateBase import TranslateBase

import deep_translator
from deep_translator import GoogleTranslator
import random

##        translatorList.append(GoogleTranslator(source=language, target=newLanguage))
##        translatorList.append(MyMemoryTranslator(source=language, target=newLanguage)) 
##         if((not language in ['ar','he','no','se','ud','ur']) and (not newLanguage in ['ar','he','no','se','ud','ur'])):
##            translatorList.append(LingueeTranslator(source=language, target=newLanguage))
## 

##
## dupl: ['long', 'chinese (simplified)', 'short', 'zh-CN']
##       ['long', 'chinese (traditional)', 'short', 'zh-TW']
## https://de.wikipedia.org/wiki/Liste_der_ISO-639-Sprachcodes
## wrong: ['long', 'cebuano', 'short', 'ceb', 'iso', 'ce']
##        ['long', 'hawaiian', 'short', 'haw', 'iso', 'ha']
##        ['long', 'hmong', 'short', 'hmn', 'iso', 'hm']

class dTgoogleTranslate(TranslateBase):

    ## https://stackoverflow.com/questions/9056957/correct-way-to-define-class-variables-in-python
    ## class variable vs instance variable

    sourceLanguages = []
    targetLanguages = []
    callCounter = 0
    totalTextLength = 0 
    isoDictionary = {}
    nameDictionary = {}

    maxTextLength = 5000

    def __init__(self):
        allLanguages = GoogleTranslator().get_supported_languages(as_dict=True)
        for langLong in allLanguages:
            langShort = allLanguages[langLong] 
            langIso = langShort.split('-')[0]
            print(['long',langLong,'short',langShort,'iso',langIso])
            ## ['long', 'chinese (simplified)', 'short', 'zh-CN']
            ## ['long', 'chinese (traditional)', 'short', 'zh-TW']
            if(not langIso in dTgoogleTranslate.isoDictionary):
              dTgoogleTranslate.isoDictionary[langIso] = []
            if(not langShort in dTgoogleTranslate.isoDictionary[langIso]):
              dTgoogleTranslate.isoDictionary[langIso].append(langShort)  
            if(not langIso in dTgoogleTranslate.nameDictionary):
              dTgoogleTranslate.nameDictionary[langIso] = []
            if(not langLong in dTgoogleTranslate.nameDictionary[langIso]):
              dTgoogleTranslate.nameDictionary[langIso].append(langLong)   
            if(not langShort in dTgoogleTranslate.sourceLanguages):
              dTgoogleTranslate.sourceLanguages.append(langIso)
            if(not langShort in dTgoogleTranslate.targetLanguages):
              dTgoogleTranslate.targetLanguages.append(langIso)
        print(dTgoogleTranslate.isoDictionary)

    def getServiceName(self):
        return 'deepTranslator.google'

    def translate(self, sourceText, sourceLanguage, targetLanguage):
        dTgoogleTranslate.callCounter += 1
        dTgoogleTranslate.totalTextLength += len(sourceText)
        anySource = random.choice(dTgoogleTranslate.isoDictionary[sourceLanguage])
        anyTarget = random.choice(dTgoogleTranslate.isoDictionary[targetLanguage])  
        gt = GoogleTranslator(source=anySource, target=anyTarget) 
        targetText = gt.translate(sourceText)
        return targetText




