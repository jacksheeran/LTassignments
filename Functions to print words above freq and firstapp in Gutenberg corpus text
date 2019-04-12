from nltk.corpus import gutenberg

def frequency(sentence):
    freq = dict()
    for word in sentence:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    return(freq)

def freqandfirstapp(textfilefromgutenberg, fromfreq, fromfirstapp):

    text=gutenberg.sents(textfilefromgutenberg)

    firstapp = dict()

    for i in range(len(alice)):
        frequency(alice[i])


    for n in range(len(alice)):
        for word in alice[n]:
            if word not in firstapp:
                firstapp[word] = n

    allwords = []

    for q in range(len(alice)):
        for word in alice[q]:
            if word not in allwords:
                allwords.append(word)

    allwords.sort()

    for word in allwords:
       if freq[word] > fromfreq and firstapp[word] > fromfirstapp:
           print(word)

           
freqandfirstapp('carroll-alice.txt', 30, 200) #test
