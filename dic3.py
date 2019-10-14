sample_text= "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his brown belly"
words_dict = {}
sample_text = sample_text.lower()
sample_text = sample_text.replace(',', "")
sample_text = sample_text.replace(".", "")
sample_text = sample_text.split(" ")
for word in sample_text:
	if word in words_dict.keys():
		words_dict[word] +=1
	else: 
		words_dict[word] = 1


for (word, amount) in words_dict.items():
	if amount > 2:
	 print(word, ":", amount)