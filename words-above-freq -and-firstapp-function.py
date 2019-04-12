from nltk.corpus import gutenberg

def freqandfirstapp(textfilefromgutenberg, fromfreq, fromfirstapp):
    """Adapted from an early assignment to print all words appearing more than 30 times past sentence 200 from a Carroll novel.
       Function prints words from any input text from the NLTK Gutenburg corpus and prints words above the input frequency
       and that appear after the input sentence number."""

    freq = dict()
    
    def frequency(sentence):
        """Updates dictionary of words and their corresponding frequencies in a sentence"""
        for word in sentence:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1

    text=gutenberg.sents(textfilefromgutenberg)

    firstapp = dict()

    for i in range(len(alice)): #run frequency function on each sentence
        frequency(alice[i])


    for n in range(len(alice)): #updates dictionary firstapp with words and the setence they first appear in
        for word in alice[n]:
            if word not in firstapp:
                firstapp[word] = n

    allwords = []

    for q in range(len(alice)): #creates a list of all words
        for word in alice[q]:
            if word not in allwords:
                allwords.append(word)

    allwords.sort()

    for word in allwords:       #iterates over each word and prints if its frequency and first appearence are higher than input values
       if freq[word] > fromfreq and firstapp[word] > fromfirstapp:
           print(word)

           
freqandfirstapp('carroll-alice.txt', 30, 200) #test
