import json
import requests
from deep_translator import GoogleTranslator

# mengambl funfact
def get_fun_fact():
    # Clear the screen
    
    # URL from where we will fetch the data
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    # Use GET request
    response = requests.get(url)
    
    # Load the request in json file
    data = json.loads(response.text)
    
    # We will need 'text' from the data
    return data['text']

hasilku = get_fun_fact()
hasil = str(hasilku)
# translate funfact
translated = GoogleTranslator(source='auto', target='id').translate(hasil) 
print(translated)