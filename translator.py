from translate import Translator

#From English to Spanish
translator= Translator(to_lang="Spanish")

translation = translator.translate("We are very happy!")

print(translation)

#from language to language
translator= Translator(from_lang="english",to_lang="chinese")
translation = translator.translate("We are happy!")

print(translation)



