import pronouncing

import string

import arpabetmodule #imported from costum module 'arpabetmodule.py', converts APRAbet to IPA

def ipa(text):
"""converts text input to IPA"""

    text = text.lower()
    textipa = ''
    
    for word in text.split():
        
        wordx = pronouncing.phones_for_word(word.rstrip(',.-/()!?¿¡$%&#@:;')) 
        
        if wordx == []:
            
            if textipa == '':
                textipa = textipa + (len(word)*'?')
                
            else:
                textipa = textipa + ' ' + (len(word)*'?')
                
        else:
            wordy = arpabetmodule.ipa_word(wordx[0])
            
            if textipa == '':
                textipa = textipa + wordy
                
            else:
                textipa = textipa + ' ' + wordy
    return textipa

def ipafile(filename):
"""outputs a file with text from input file converted to IPA"""

    with open('withipa_' + filename, 'w') as nf:
        
        with open(filename) as f:
            
            for line in f:
                
                print(ipa(line), file=nf)
