from asyncore import write
import string
madlibFile = open('madlib.txt', 'r')
split_text = (madlibFile.read()).split()

for text in split_text:
    split_text_nu = text#.translate(str.maketrans('','',string.punctuation))
    if split_text_nu.isupper() and 'ADJECTIVE' in split_text_nu:
        words = split_text_nu.split('ADJECTIVE')
        txt = input(f"Enter an {split_text_nu.lower()}:\n")
        words[0] = txt
        words = "".join(words)
        split_text[split_text.index(text)] = words
    if split_text_nu.isupper() and 'NOUN' in split_text_nu:
        words = split_text_nu.split("NOUN")
        txt1 = input(f"Enter a {split_text_nu.lower()}:\n")
        words[0] = txt1
        words = ''.join(words)
        split_text[split_text.index(text)] = words
    if split_text_nu.isupper() and 'ADVERB' in split_text_nu:
        words = split_text_nu.split("ADVERB")
        txt2 = input(f"Enter an {split_text_nu.lower()}:\n")
        words[0] = txt2
        words = "".join(words)
        split_text[split_text.index(text)] = words
    if split_text_nu.isupper() and "VERB" in split_text_nu:
        words = split_text_nu.split("VERB")
        txt3 = input(f"Enter a {split_text_nu.lower()}:\n")
        words[0] = txt3
        words = "".join(words)
        split_text[split_text.index(text)] = words

madlibFile.close()

madlibEditted = open('madlibEditted.txt','w')        
madlibEditted.write(' '.join(split_text))
madlibEditted.close()

#if split_text_nu.upper() and split_text_nu.find('VERB') == 0: