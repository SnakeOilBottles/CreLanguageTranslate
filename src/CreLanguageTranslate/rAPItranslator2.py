from CreLanguageTranslate.TranslateBase import TranslateBase

import os
import requests
import json
import random


## MOVE to tools/utils later....
from pathlib import Path
DATA_PATH = Path.cwd()
#import os.path
#sys.path.insert(0, os.path.abspath(BASE_DIR))
import mysecrets 
##

# https://rapidapi.com/dickyagustin/api/text-translator2
# https://rapidapi.com/dickyagustin/api/text-translator2/pricing
# 100000 characters/month; 1000 requests/month; (1000 request/hour)
# RAPIDAPI_KEY
class rAPItranslator2(TranslateBase):

    ## https://stackoverflow.com/questions/9056957/correct-way-to-define-class-variables-in-python
    ## class variable vs instance variable

    sourceLanguages = []
    targetLanguages = []
    callCounter = 0
    totalTextLength = 0 
    isoDictionary = {}
    nameDictionary = {}

    maxTextLength = 5000
    service = 'text-translator2'

    def __init__(self):
        allLanguages = self.languages()
        for language in allLanguages:
            langIso = language['code']
            langName = language['name']
            if(not langIso in rAPItranslator2.isoDictionary):
              rAPItranslator2.isoDictionary[langIso] = []
            if(not langIso in rAPItranslator2.isoDictionary[langIso]):
              rAPItranslator2.isoDictionary[langIso].append(langIso)    
            if(not langIso in rAPItranslator2.nameDictionary):
              rAPItranslator2.nameDictionary[langIso] = []
            if(not langName in rAPItranslator2.nameDictionary[langIso]):
              rAPItranslator2.nameDictionary[langIso].append(langName) 
            if(not langIso in rAPItranslator2.sourceLanguages):
              rAPItranslator2.sourceLanguages.append(langIso)
            if(not langIso in rAPItranslator2.targetLanguages):
              rAPItranslator2.targetLanguages.append(langIso)
        print(rAPItranslator2.isoDictionary)



    def getServiceName(self):
        return 'rapiApi.'+rAPItranslator2.service

    def getRapid(self,endpoint='getLanguages', payload=None):
        apiKey = os.getenv('RAPIDAPI_KEY')
        rapidAPI = 'p.rapidapi.com'  
        headers = {
            'x-rapidapi-key': apiKey,
            'x-rapidapi-host': rAPItranslator2.service+"."+rapidAPI,
            'Content-Type': 'application/x-www-form-urlencoded'
            }
        url = "https://"+rAPItranslator2.service+"."+rapidAPI+"/"+endpoint
        ##response = requests.post(url, headers=headers, data=payload)
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        
        if((response.text) and (not response.status_code in [204, 500, 504])):
            ##results.append(":white_check_mark: Text-Translator-2 respone fine")
            text = response.text
            #print(text)
            if(not isinstance(text,str)):
                text = text.decode("utf-8")
            jsonData = json.loads(text)
            if('message' in jsonData):
              #print(jsonData['message'])
              if('You are not subscribed to this API.'==jsonData['message']):
                #results.append(":no_entry: **Not** subscribed to "+rAPItranslator2.service)
                #addSubscribeMessageToResults(results, service, "https://rapidapi.com/dickyagustin/api/text-translator2")
                return False
              if('Invalid API key. Go to https://docs.rapidapi.com/docs/keys for more info.'==jsonData['message']):
                return False
            return jsonData
        else:
          ##results.append(":no_entry: "+rAPItranslator2.service+" respone **failed**") 
          ##results.append("Maybe retry later...?") #?
          return False
        return False

    def postRapid(self,endpoint='translate', payload=None):
        apiKey = os.getenv('RAPIDAPI_KEY')
        rapidAPI = 'p.rapidapi.com'  
        headers = {
            'x-rapidapi-key': apiKey,
            'x-rapidapi-host': rAPItranslator2.service+"."+rapidAPI,
            'Content-Type': 'application/x-www-form-urlencoded'
            }
        url = "https://"+rAPItranslator2.service+"."+rapidAPI+"/"+endpoint
        response = requests.post(url, headers=headers, data=payload)
        response.encoding = response.apparent_encoding
        if((response.text) and (not response.status_code in [204, 500, 504])):
            ##results.append(":white_check_mark: Text-Translator-2 respone fine")
            text = response.text
            #print(text)
            if(not isinstance(text,str)):
                text = text.decode("utf-8")
            jsonData = json.loads(text)
            if('message' in jsonData):
              #print(jsonData['message'])
              if('You are not subscribed to this API.'==jsonData['message']):
                #results.append(":no_entry: **Not** subscribed to "+rAPItranslator2.service)
                #addSubscribeMessageToResults(results, service, "https://rapidapi.com/dickyagustin/api/text-translator2")
                return False
              if('Invalid API key. Go to https://docs.rapidapi.com/docs/keys for more info.'==jsonData['message']):
                return False
            return jsonData
        else:
          ##results.append(":no_entry: "+rAPItranslator2.service+" respone **failed**") 
          ##results.append("Maybe retry later...?") #?
          return False
        return False

    def languages(self):
        jsonData = self.getRapid(endpoint='getLanguages')
        if(jsonData):
          if('data' in jsonData):
            allLanguages = jsonData['data']
            if('languages' in allLanguages):
              return allLanguages['languages']
        return [] 
        #return None

    def translation(self, sourceText, sourceLanguage, targetLanguage):
        payload = {"text":sourceText,"source_language":sourceLanguage,"target_language":targetLanguage}
        jsonData = self.postRapid(endpoint='translate', payload=payload)
        if ('data' in jsonData):
          if ('translatedText' in jsonData['data']):
            return jsonData['data']['translatedText']  
        return None  

    def translate(self, sourceText, sourceLanguage, targetLanguage):
        rAPItranslator2.callCounter += 1
        rAPItranslator2.totalTextLength += len(sourceText)
        ##anySource = random.choice(googleTranslate.isoDictionary[sourceLanguage])
        ##anyTarget = random.choice(googleTranslate.isoDictionary[targetLanguage])  
        targetText = self.translation(sourceText, sourceLanguage, targetLanguage)
        return targetText




