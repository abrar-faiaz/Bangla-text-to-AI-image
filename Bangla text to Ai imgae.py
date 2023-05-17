import openai
from translate import Translator  # import the modules
translator = Translator(from_lang="bn", to_lang="en")   # creates an object

bangla_text = input("আপনি যে চিত্রটি তৈরি করতে চান সে সম্পর্কে বলুন: ")  # gets the bangla input

english_text = translator.translate(bangla_text)
openai.api_key=open("api.txt", "rt").read()   # reads the text file in which the api key is stored.You can directly put your key in the " " .
img=openai.Image.create(
 prompt=english_text,
 n=1,
 size="1024x1024"
)
img_url=img['data'][0]['url']
print(img_url)