from  textblob import TextBlob
text = input (str("ingrese un palabra a traducir :\n"))

blob1 = TextBlob(text)

blob1.tags
blob1.noun_phrases

print ("----- TRADUCCION ----")

print (blob1.translate (to = "en")) ##"en" en esta parte se pone el idionma al que se quiere traducir
for sentence in blob1.sentences:
	print(sentence.sentiment.polarity)
	
def creartxt():
	archi=open('trad','w')
	archi.close()

def grabartxt():
	archi=open('trad','a')
	archi.write(text)
	archi.close()

creartxt()
grabartxt()
