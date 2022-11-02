"""translator function """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

BASE_URL = 'https://api.us-south.language-translator.watson.cloud.ibm.com'
language_translator.set_service_url(BASE_URL)


def english_to_french(english_text):
    """englishToFrench function to translate english to french"""
    if not english_text:
        return None
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        #print(json.dumps(frenchText, indent=2, ensure_ascii=False))

    return french_text["translations"][0]['translation']

def french_to_english(french_text):
    """frenchToEnglish function to translate french to english"""
    #write the code here
    if not french_text:
        return None
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
#    print(english_text)
#    print(json.dumps(english_text, indent=2, ensure_ascii=False))
#    print(english_text["translations"][0]['translation'])
    return english_text["translations"][0]['translation']
