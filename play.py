import deep_translator
from deep_translator import (GoogleTranslator,
                             ChatGptTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             LibreTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,   #not existing
                             single_detection,
                             batch_detection)


#https://github.com/terryyin/translate-python
#pip3 install translate
from translate import Translator



text = 'happy coding makes fun'

#translated = GoogleTranslator(source='auto', target='de').translate(text=text) #fail
#translated = MyMemoryTranslator(source='en-GB', target='de-DE').translate(text=text) #wrong
#translated = DeeplTranslator(source='en-GB', target='de-DE', use_free_api=True, api_key='123').translate(text=text) #onetime credit 1E6 chars
#translated = LingueeTranslator(source='english', target='german').translate(word=text) #words only
#translated = PonsTranslator(source='en', target='de').translate(word=text) #words only/not working
#translated = YandexTranslator('your_api_key').translate(source="auto", target="en", text='Hallo, Welt') #Costs
#translated = LibreTranslator(source='auto', target='en').translate(text=text) #costs

#translated = MicrosoftTranslator(api_key='some-key', target='de').translate(text=text) #needs API key: 2 million chars/month free
#translated = ChatGptTranslator(api_key='your_key', target='german').translate(text=text) #?

#translated = TencentTranslator(secret_id="your-secret_id", secret_key="your-secret_key" source="en", target="de").translate(text) #?

'''
    'mymemory': MyMemoryProvider,
    'microsoft': MicrosoftProvider,
    'deepl': DeeplProvider,   10000000 chars
    'libre': LibreProvider,   $29/month
    'yandex': YandexProvider
'''

translator = Translator(from_lang='en',to_lang="de")
translator = Translator(provider='microsoft', from_lang='en',to_lang="de")
translated = translator.translate(text)  

#https://translate-python.readthedocs.io/en/latest/providers.html  #MyMemory


print(translated)

