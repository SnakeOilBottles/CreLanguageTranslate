from CreLanguageTranslate.TranslateBase import TranslateBase

from translate import Translator


# https://mymemory.translated.net/
# https://mymemory.translated.net/doc/spec.php
# http://mymemory.translated.net/doc/usagelimits.php

class tMyMemory(TranslateBase):

    sourceLanguages = []
    targetLanguages = []
    callCounter = 0
    totalTextLength = 0 
    isoDictionary = {}
    nameDictionary = {}
    isWorking = True

    # limit = 5000 chars/day (without email)
    # limit = 50000 chars/day (with email)
    # limit = 150000 chars/day (CAT Tool)
    maxTextLength = 500 #(bytes)

    def __init__(self):
      
      tMyMemory.sourceLanguages = ['en','de']
      tMyMemory.targetLanguages = ['en','de']

    def getServiceName(self):
        return 'translate.mymemory'

    def translate(self, sourceText, sourceLanguage, targetLanguage):
        tMyMemory.callCounter += 1
        tMyMemory.totalTextLength += len(sourceText)

        gt = GoogleTranslator(source=anySource, target=anyTarget) 
        translator = Translator(provider='mymemory', from_lang=sourceLanguage,to_lang=targetLanguage) # secret_access_key=''
        targetText = translator.translate(sourceText)  

        # tMyMemory.isWorking = False
        return targetText
