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
    isWorking = True

    maxTextLength = 5000
    service = 'text-translator2'  # news-api14.p.rapidapi.com

    frozenLanguages = {"data": {"languages": [
      { "code":"af", "name":"Afrikaans" },
      { "code":"sq", "name":"Albanian" },
      { "code":"am", "name":"Amharic" },
      { "code":"ar", "name":"Arabic" },
      { "code":"hy", "name":"Armenian" },
      { "code":"az", "name":"Azerbaijani" },
      { "code":"eu", "name":"Basque" },
      { "code":"be", "name":"Belarusian" },
      { "code":"bn", "name":"Bengali" },
      { "code":"bs", "name":"Bosnian" },
      { "code":"bg", "name":"Bulgarian" },
      { "code":"ca", "name":"Catalan" },
      { "code":"ceb", "name":"Cebuano" },
      { "code":"ny", "name":"Chichewa" },
      { "code":"zh-CN", "name":"Chinese (Simplified)" },
      { "code":"zh-TW", "name":"Chinese (Traditional)" },
      { "code":"co", "name":"Corsican" },
      { "code":"hr", "name":"Croatian" },
      { "code":"cs", "name":"Czech" },
      { "code":"da", "name":"Danish" },
      { "code":"nl", "name":"Dutch" },
      { "code":"en", "name":"English" },
      { "code":"eo", "name":"Esperanto" },
      { "code":"et", "name":"Estonian" },
      { "code":"tl", "name":"Filipino" },
      { "code":"fi", "name":"Finnish" },
      { "code":"fr", "name":"French" },
      { "code":"fy", "name":"Frisian" },
      { "code":"gl", "name":"Galician" },
      { "code":"ka", "name":"Georgian" },
      { "code":"de", "name":"German" },
      { "code":"el", "name":"Greek" },
      { "code":"gu", "name":"Gujarati" },
      { "code":"ht", "name":"Haitian Creole" },
      { "code":"ha", "name":"Hausa" },
      { "code":"haw", "name":"Hawaiian" },
      { "code":"iw", "name":"Hebrew" },
      { "code":"hi", "name":"Hindi" },
      { "code":"hmn", "name":"Hmong" },
      { "code":"hu", "name":"Hungarian" },
      { "code":"is", "name":"Icelandic" },
      { "code":"ig", "name":"Igbo" },
      { "code":"id", "name":"Indonesian" },
      { "code":"ga", "name":"Irish" },
      { "code":"it", "name":"Italian" },
      { "code":"ja", "name":"Japanese" },
      { "code":"jw", "name":"Javanese" },
      { "code":"kn", "name":"Kannada" },
      { "code":"kk", "name":"Kazakh" },
      { "code":"km", "name":"Khmer" },
      { "code":"rw", "name":"Kinyarwanda" },
      { "code":"ko", "name":"Korean" },
      { "code":"ku", "name":"Kurdish (Kurmanji)" },
      { "code":"ky", "name":"Kyrgyz" },
      { "code":"lo", "name":"Lao" },
      { "code":"la", "name":"Latin" },
      { "code":"lv", "name":"Latvian" },
      { "code":"lt", "name":"Lithuanian" },
      { "code":"lb", "name":"Luxembourgish" },
      { "code":"mk", "name":"Macedonian" },
      { "code":"mg", "name":"Malagasy" },
      { "code":"ms", "name":"Malay" },
      { "code":"ml", "name":"Malayalam" },
      { "code":"mt", "name":"Maltese" },
      { "code":"mi", "name":"Maori" },
      { "code":"mr", "name":"Marathi" },
      { "code":"mn", "name":"Mongolian" },
      { "code":"my", "name":"Myanmar (Burmese)" },
      { "code":"ne", "name":"Nepali" },
      { "code":"no", "name":"Norwegian" },
      { "code":"or", "name":"Odia (Oriya)" },
      { "code":"ps", "name":"Pashto" },
      { "code":"fa", "name":"Persian" },
      { "code":"pl", "name":"Polish" },
      { "code":"pt", "name":"Portuguese" },
      { "code":"pa", "name":"Punjabi" },
      { "code":"ro", "name":"Romanian" },
      { "code":"ru", "name":"Russian" },
      { "code":"sm", "name":"Samoan" },
      { "code":"gd", "name":"Scots Gaelic" },
      { "code":"sr", "name":"Serbian" },
      { "code":"st", "name":"Sesotho" },
      { "code":"sn", "name":"Shona" },
      { "code":"sd", "name":"Sindhi" },
      { "code":"si", "name":"Sinhala" },
      { "code":"sk", "name":"Slovak" },
      { "code":"sl", "name":"Slovenian" },
      { "code":"so", "name":"Somali" },
      { "code":"es", "name":"Spanish" },
      { "code":"su", "name":"Sundanese" },
      { "code":"sw", "name":"Swahili" },
      { "code":"sv", "name":"Swedish" },
      { "code":"tg", "name":"Tajik" },
      { "code":"ta", "name":"Tamil" },
      { "code":"tt", "name":"Tatar" },
      { "code":"te", "name":"Telugu" },
      { "code":"th", "name":"Thai" },
      { "code":"tr", "name":"Turkish" },
      { "code":"tk", "name":"Turkmen" },
      { "code":"uk", "name":"Ukrainian" },
      { "code":"ur", "name":"Urdu" },
      { "code":"ug", "name":"Uyghur" },
      { "code":"uz", "name":"Uzbek" },
      { "code":"vi", "name":"Vietnamese" },
      { "code":"cy", "name":"Welsh" },
      { "code":"xh", "name":"Xhosa" },
      { "code":"yi", "name":"Yiddish" },
      { "code":"yo", "name":"Yoruba" },
      { "code":"zu", "name":"Zulu" },
      { "code":"he", "name":"Hebrew" },
      { "code":"zh", "name":"Chinese (Simplified)"
      }
    ]}}

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
        print(response.headers)
        # 'x-ratelimit-characters-limit' 'x-ratelimit-characters-remaining' 'x-ratelimit-characters-reset' 
        # 'x-ratelimit-rapid-free-plans-hard-limit-limit' 'x-ratelimit-rapid-free-plans-hard-limit-remaining' 'x-ratelimit-rapid-free-plans-hard-limit-reset' 
        #'x-ratelimit-requests-limit' 'x-ratelimit-requests-remaining' x-ratelimit-requests-reset'
        
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
                rAPItranslator2.isWorking = False
                return False
              if('Invalid API key. Go to https://docs.rapidapi.com/docs/keys for more info.'==jsonData['message']):
                rAPItranslator2.isWorking = False
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
        print(response.text)
        print(response.headers)
        # 'x-ratelimit-characters-limit' 'x-ratelimit-characters-remaining' 'x-ratelimit-characters-reset' 
        # 'x-ratelimit-rapid-free-plans-hard-limit-limit' 'x-ratelimit-rapid-free-plans-hard-limit-remaining' 'x-ratelimit-rapid-free-plans-hard-limit-reset' 
        #'x-ratelimit-requests-limit' 'x-ratelimit-requests-remaining' x-ratelimit-requests-reset'
        if((response.text) and (not response.status_code in [204, 500, 504])):
            ##results.append(":white_check_mark: Text-Translator-2 respone fine")
            text = response.text
            if(not isinstance(text,str)):
                text = text.decode("utf-8")
            try:
              jsonData = json.loads(text)
            except Exception as X:
              #results.append(":no_entry: Text-Translator-2 results **not** JSON")
              #results.append("Maybe retry later...?") #?
              rAPItranslator2.isWorking = False 
              print('-+'*25)
              print(text)
              print('-+'*25)
              return False
            else:



             if('message' in jsonData):
              #print(jsonData['message'])
              if('You are not subscribed to this API.'==jsonData['message']):
                #results.append(":no_entry: **Not** subscribed to "+rAPItranslator2.service)
                #addSubscribeMessageToResults(results, service, "https://rapidapi.com/dickyagustin/api/text-translator2")
                rAPItranslator2.isWorking = False
                return False
              if('Invalid API key. Go to https://docs.rapidapi.com/docs/keys for more info.'==jsonData['message']):
                rAPItranslator2.isWorking = False 
                return False
            return jsonData
        else:
          ##results.append(":no_entry: "+rAPItranslator2.service+" respone **failed**") 
          ##results.append("Maybe retry later...?") #?
          rAPItranslator2.isWorking = False
          return False
        return False




    def languages(self):
        #jsonData = self.getRapid(endpoint='getLanguages')  # save calls for now - later may store in csv
        jsonData = rAPItranslator2.frozenLanguages
        if(jsonData):
          if('message' in jsonData):
            #print(jsonData['message'])
            if('Too many requests' == jsonData['message']):
              rAPItranslator2.isWorking = False
              print('FAIL: Too many requests @ rAPItranslator2')
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




