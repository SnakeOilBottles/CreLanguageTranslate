from CreLanguageTranslate.TranslateBase import TranslateBase

import os
import requests
import json
import random


#https://rapidapi.com/sibaridev/api/rapid-translate-multi-traduction/pricing  -> plan!
#https://rapidapi.com/developer/billing/subscriptions-and-usage usage/quota
"""
curl 'https://rapidapi.com/gateway/graphql' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/json;charset=utf-8' -H 'x-entity-id: 5658635' -H 'rapid-client: developers-dashboard-service' -H 'csrf-token: b1DD1CKK-GM-VSAQkCXk5gZhqtmXzmvWAxfA' -H 'Origin: https://rapidapi.com' -H 'Connection: keep-alive' -H 'Referer: https://rapidapi.com/_developer/billing/subscriptions-and-usage?pub_hub=true' -H 'Cookie: __cflb=02DiuHPSNb326nZUQB6NoY4qqsJaLefLR532tkUd8EMJc; cf_clearance=.SeoPBlEJ3n_8HMjHlrkfkE23Uxt37Mu_pXsUbryidk-1777714719-1.2.1.1-e4TOjJpfpgSgG9jua8K1MoEFZW7CgmAkImUYRPmdJRiD3NIdVr5ZL.0lr.qFgtBwtlFfU_RjKDiNXr2TT2cAuXmJ4ItwvzOdyifsq5IpGzqK.vinNiMoOYvsz0gIBIhRTdl8MGkjcTnphfB69XtUF1F5cylcCXhSA7Bni.FBQHSKtbF6xSfPNPu3srMP7bO0jfWMpT_4dGxwWJOWx7F_PEsjA6gW2IRIc5v20pjzoAWwbR5qy5RBZDKQ3EnXiWcPR3jf6qXa4CggaHLxgJZh7Dr40N0m5cqwLWBC9lJlcyRi8XQTxlZGeGEPqFZqL2jHnRhwXEB2vZCgorOpNBLNoA; g_state={"i_l":1,"i_ll":1777634575354,"i_b":"1gN23Eb6c/fHN0mwrSt3DTKaZSd1kwX4MK5CYAzaFbs","i_e":{"enable_itp_optimization":0},"i_et":1777634575354,"i_p":1777641778538}; ajs_user_id=614f60227cfdab214f2e38e2; ajs_anonymous_id=15A3C463-86B2-4F67-AF6A-EAF51C441C1B; _gcl_au=1.1.1000590644.1777634576; OptanonConsent=isGpcEnabled=0&datestamp=Sat+May+02+2026+11%3A40%3A41+GMT%2B0200+(Central+European+Summer+Time)&version=202510.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=2ae88436-b060-48b8-9f9d-cf03da5d27fd&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0004%3A1%2CC0002%3A1%2CC0001%3A1&AwaitingReconsent=false&intType=1&geolocation=DE%3BBW; _ga=GA1.2.504686110.1777634577; _gid=GA1.2.1085338877.1777634577; __stripe_mid=a5046676-68d2-4e19-b005-171de4b5b19854034c; jwt_auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NTY1ODYzNSwibWFzaGFwZUlkIjoiNjE0ZjYwMjI3Y2ZkYWIyMTRmMmUzOGUyIiwib3JpZ2luX3NpdGUiOiJyYXBpZGFwaSIsImVtYWlsIjoibWljaGFlbC5rYWhsZUB5YWhvby5kZSIsImlzTmV3VXNlciI6ZmFsc2UsImlzQXV0aGVudGljYXRlZEJ5U1NPIjpmYWxzZSwidHdvRmFjdG9yQXV0aG9yaXplZCI6ZmFsc2UsInR3b0ZhY3RvclByZWZlcnJlZE1ldGhvZCI6ZmFsc2UsInR3b0ZhY3RvckVuYWJsZWQiOmZhbHNlLCJ3YXNTZXNzaW9uSXNzdWVkIjp0cnVlLCJpYXQiOjE3Nzc2MzQ2MTgsImV4cCI6MTc4NTQxMDYxOH0.HJT6rc2VIWka2YQMID-MiogOvsTRn3x5kPuTwvsH00Q; connect.sid=s%3AjPTY1tjN0aknIS6LHbeTb-ZzJN68AnpI.e4sbALg%2ButG6lvWrCMFAn8I4dHlnd78E1crNmB6pgaw; OptanonAlertBoxClosed=2026-05-01T11:23:56.309Z; __cf_bm=sXYOonRS4NueyfLSeoUFGH_xrEPtBnGPUDN1MFBkAOo-1777714719.3267896-1.0.1.1-UgWQE9lDRJbZaNf_v_xPvAehL.K9NCsjompAxddb6FTKuJwcQFD1ggoIbZrB1BEhK23gRrJwHK1Xj0Q4h7J0gj6vtdeVrzlP6lApWg4wQaUkTvIEI8DCTVhKjO9Dl9w2; AMP_TOKEN=%24NOT_FOUND; __stripe_sid=928bf2a2-caa9-4a9b-aa77-77922ba5465c6ccb29; _ga_KK5QQ6G7DK=GS2.1.s1777712244$o1$g1$t1777712584$j60$l0$h0; _csrf=Wuso3R2QwquMfUxg5PeaFSaz; rapidapi-context-id=5658635; __variation__FFNewModalExperiment=0.3; __variation__FFPostSignupModalMarketplace=0.85; __variation__FFNewHero=0.65; __variation__FFNewOrgCreatePage=0.79; __variation__FFAskCompanyInfo=0.89; __variation__FFEmbedTeamsVideo=0.77; __variation__FFTeamsLandingPageOrgButtonText=0.05; __variation__FFOrgCreationWithUsersInvitaions=0.04; __variation__FFApiPlaygroundABTest=0.73; __variation__FF_SearchInput_PlaceHolder=0.01; __variation__FFSubscribeModalDirectNavToPricing=0.9; __variation__FFNewPricingPage=0.41; __variation__FFPricingPaymentsAdminsInvite=0.04; __variation__FFPricingPersonalNoOrg=0.22; __variation__FFTryItFreeBottomMPTeamsPage=0.71; __variation__FFFastSubscribeToFreePlanOnMarketplace=0.01; __variation__FFNewPaymentPage=0.81; __variation__FFNewMarketplaceHomepageContent=0.06; __variation__FFAPILimitModalExperiment=0.03; theme=light; _gat=1' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-origin' -H 'TE: trailers' --data-raw '{"operationName":"getSubscriptions","query":"\n  query getSubscriptions {\n    activeEntity {\n      id\n      subscriptions(getAllSubscriptions: true, statuses: [\"ACTIVE\", \"BLOCKED\", \"PENDING_DELETION\"]) {\n        id\n        status\n        billingPlanVersion {\n          id\n          name\n          current\n          status\n          period\n          price\n          pricing\n          billinglimits {\n            item\n            period\n            amount\n            limitType\n            unlimited\n            billingitem {\n              name\n            }\n          }\n          billingPlan {\n            name\n            id\n          }\n        }\n        usages {\n          mostUsagePercentage\n          topPercentageLimitedUsage\n          pricing\n          usageByBillingItem {\n            id\n            name\n            quota\n            usage\n            period\n            usagePercentages\n            billingCycleStart\n          }\n        }\n        userId\n        parentId\n        stripeId\n        isInternal\n        billingPlanVersionId\n        apiId\n        apiVersionId\n        createdAt\n        api {\n          title\n          name\n          owner {\n            id\n            slugifiedName\n          }\n          slugifiedName\n        }\n        apiVersion {\n          name\n          thumbnail\n        }\n        additionalSubscriptionData {\n          latestInvoiceId\n        }\n        relatedActiveSubscriptions {\n          id\n        }\n      }\n    }\n  }\n"}'
"""


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
    isWorking = True

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
                rAPImultiTraductionisWorking = False
                return False
              if('Invalid API key' in jsonData['message']):
                rAPImultiTraductionisWorking = False
                return False
              if('Too many requests'==jsonData['message']):
                rAPImultiTraductionisWorking = False
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
        print('*#-'*15)
        print(jsonData) 
        if hasattr(jsonData, "__len__"):
          if (len(jsonData)>0):
            return jsonData[0]
        else:
            rAPImultiTraduction.isWorking = False
        return None  

    def translate(self, sourceText, sourceLanguage, targetLanguage):
        rAPImultiTraduction.callCounter += 1
        rAPImultiTraduction.totalTextLength += len(sourceText)
        ##anySource = random.choice(googleTranslate.isoDictionary[sourceLanguage])
        ##anyTarget = random.choice(googleTranslate.isoDictionary[targetLanguage])  
        targetText = self.translation(sourceText, sourceLanguage, targetLanguage)
        return targetText




