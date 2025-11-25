from CreLanguageTranslate.TranslateBase import TranslateBase

import os
import requests
import json
import random


def inqRapidMultiTraductionTranslate(results=[]):
    gitOrg = os.getenv('GITHUB_OWNER')
    apiKey = os.getenv('RAPIDAPI_KEY')
    results.append("### RapidAPI: Multi-Traduction-Translate")
    url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"
    payload = {"q":"Klimawandel","from":"de","to":"en"}
    headers = {
        'x-rapidapi-key': apiKey,
        'x-rapidapi-host': "rapid-translate-multi-traduction.p.rapidapi.com",
        'Content-Type': 'application/json'
        }
    response = requests.post(url, headers=headers, json=payload)
    #response = requests.request('POST', url, headers=headers, json=payload)
    response.encoding = response.apparent_encoding
    #print(response.text)
    print(['Multi-Traduction-Translate', response.status_code])     #200
    #504 : The request to the API has timed out
    if((response.text) and (not response.status_code in [204, 500, 504])):
        results.append(":white_check_mark: Multi-Traduction-Translate respone fine")
        text = response.text
        if(not isinstance(text,str)):
            text = text.decode("utf-8")
        jsonData = json.loads(text)
        if('message' in jsonData):
          if('You are not subscribed to this API.'==jsonData['message']):
            results.append(":no_entry: **Not** subscribed to Multi-Traduction-Translate")
            addSubscribeMessageToResults(results, "Multi-Traduction-Translate", "https://rapidapi.com/sibaridev/api/rapid-translate-multi-traduction")
            return False
        if (len(jsonData)>0):
          results.append(":white_check_mark: Multi-Traduction-Translate status fine")
          if (jsonData[0]):
            results.append(":white_check_mark: Multi-Traduction-Translate results found")
            return True
          else: 
            results.append(":no_entry: Multi-Traduction-Translate results **not** found")
            results.append("Maybe retry later...?") #?
            return False
        else:
          results.append(":no_entry: Multi-Traduction-Translate status **failed**:")
          addSubscribeMessageToResults(results, "Multi-Traduction-Translate", "https://rapidapi.com/sibaridev/api/rapid-translate-multi-traduction")
          return False
    else:
      results.append(":no_entry: Multi-Traduction-Translate respone **failed**") 
      results.append("Maybe retry later...?") #?
      return False
    return False


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
class rAPImultiTraduction(TranslateBase):

    ## https://stackoverflow.com/questions/9056957/correct-way-to-define-class-variables-in-python
    ## class variable vs instance variable

    sourceLanguages = []
    targetLanguages = []
    callCounter = 0
    totalTextLength = 0 
    isoDictionary = {}
    nameDictionary = {}

    maxTextLength = 5000
    service = 'rapid-translate-multi-traduction'

    def __init__(self):
        allLanguages = self.languages()
        for language in allLanguages:
            langIso = language
            langName = language
            if(not langIso in rAPImultiTraduction.isoDictionary):
              rAPImultiTraduction.isoDictionary[langIso] = []
            if(not langIso in rAPImultiTraduction.isoDictionary[langIso]):
              rAPImultiTraduction.isoDictionary[langIso].append(langIso) 
            if(not langIso in rAPImultiTraduction.nameDictionary):
              rAPImultiTraduction.nameDictionary[langIso] = []
            if(not langName in rAPImultiTraduction.nameDictionary[langIso]):
              rAPImultiTraduction.nameDictionary[langIso].append(langName)   
            if(not langIso in rAPImultiTraduction.sourceLanguages):
              rAPImultiTraduction.sourceLanguages.append(langIso)
            if(not langIso in rAPImultiTraduction.targetLanguages):
              rAPImultiTraduction.targetLanguages.append(langIso)
        print(rAPImultiTraduction.isoDictionary)



    def getServiceName(self):
        return 'rapiApi.'+rAPImultiTraduction.service

    #not needed
    def getRapid(self,endpoint='getLanguages', payload=None):
        apiKey = os.getenv('RAPIDAPI_KEY')
        rapidAPI = 'p.rapidapi.com'  
        headers = {
            'x-rapidapi-key': apiKey,
            'x-rapidapi-host': rAPImultiTraduction.service+"."+rapidAPI,
            'Content-Type': 'application/json'
            }
        url = "https://"+rAPImultiTraduction.service+"."+rapidAPI+"/"+endpoint
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

    def postRapid(self,endpoint='t', payload=None):
        apiKey = os.getenv('RAPIDAPI_KEY')
        rapidAPI = 'p.rapidapi.com'  
        headers = {
            'x-rapidapi-key': apiKey,
            'x-rapidapi-host': rAPImultiTraduction.service+"."+rapidAPI,
            'Content-Type': 'application/json'
            }
        url = "https://"+rAPImultiTraduction.service+"."+rapidAPI+"/"+endpoint
        response = requests.post(url, headers=headers, json=payload)                     #JSON vs DATA!
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
        #jsonData = self.getRapid(endpoint='getLanguages')
        #if('data' in jsonData):
        #   allLanguages = jsonData['data']
        #   if('languages' in allLanguages):
        #      return allLanguages['languages']
        return ['de','en']    #many more, but no API inq
        #return None

    def translation(self, sourceText, sourceLanguage, targetLanguage):
        payload = {"q":sourceText,"from":sourceLanguage,"to":targetLanguage}
        jsonData = self.postRapid(endpoint='t', payload=payload)
        if (len(jsonData)>0):
            return jsonData[0]
        return None  

    def translate(self, sourceText, sourceLanguage, targetLanguage):
        rAPImultiTraduction.callCounter += 1
        rAPImultiTraduction.totalTextLength += len(sourceText)
        ##anySource = random.choice(googleTranslate.isoDictionary[sourceLanguage])
        ##anyTarget = random.choice(googleTranslate.isoDictionary[targetLanguage])  
        targetText = self.translation(sourceText, sourceLanguage, targetLanguage)
        return targetText




