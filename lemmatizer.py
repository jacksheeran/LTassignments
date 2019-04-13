import re, sys

"""From assignment to rewrite the code for a basic lemmatizer, adding functions for specific words types that can cope with irregular 
endings and compound words like 'aren't' and 'don't', and returns them in dictionary form, achieving above 98% accurracy on test texts."""

def noun_lemma(word):
    if word.endswith("s"):
        if word.endswith("ss"):
            return word.lower()
        elif  word.endswith("ies"):
            return word[:-3].lower() + ("y")
        else:
            return word[:-1].lower()
    if word.endswith("men"):
        return word[:-2].lower() + ("an")
    else:
        return word.lower()

def verb_lemma(word):
    if word.endswith("ed"):
        if word[:-2].endswith("v"):
            return word[:-2].lower() + "e"
        elif word[:-2].endswith("at"):
            return word[:-2].lower() + "e"
        elif word[:-2].endswith("it"):
            return word[:-2].lower() + "e"
        elif word[:-2].endswith("et"):
            return word[:-2].lower() + "e"
        elif word[:-2].endswith("ut"):
            return word[:-2].lower() + "e"
        elif word[:-2].endswith("ac"):
            return word[:-2].lower() + "e"
        elif word[:-2].endswith("i"):
            return word[:-3].lower() + "y"
        elif word[:-2].endswith("ir"):
            return word[:-2].lower() + "e"
        elif word[:-2].endswith("ag"):
            return word[:-2].lower() + "e"
        elif word[:-2].endswith("nc"):
            return word[:-2].lower() + "e"
        elif word[:-2].endswith("nu"):
            return word[:-2].lower() + "e"
        else:
            return word[:-2].lower()    
    elif word.endswith("ing"):
        if word[:-3].endswith("v"):
            return word[:-3].lower() + "e"
        elif word[:-3].endswith("at"):
            return word[:-3].lower() + "e"
        elif word[:-3].endswith("it"):
            return word[:-3].lower() + "e"
        elif word[:-3].endswith("et"):
            return word[:-3].lower() + "e"
        elif word[:-3].endswith("ut"):
            return word[:-3].lower() + "e"
        elif word[:-3].endswith("ac"):
            return word[:-3].lower() + "e"
        elif word[:-3].endswith("i"):
            return word[:-4].lower() + "y"
        elif word[:-3].endswith("ir"):
            return word[:-3].lower() + "e"
        elif word[:-3].endswith("ag"):
            return word[:-3].lower() + "e"
        elif word[:-3].endswith("nc"):
            return word[:-3].lower() + "e"
        elif word[:-3].endswith("nu"):
            return word[:-3].lower() + "e"
        else:
            return word[:-3].lower()
    elif re.match(r"(does|did|done)", word):
        return ("do")
    elif re.match(r"(is|are|am|was|will|were|been)", word):
        return ("be")
    elif word == ("'s"):
        return ("be")
    elif re.match(r"(had|has|'ve)", word):
        return ("have")
    else:
        return word.lower()
    

def adj_lemma(word):
    if word.endswith("er"):
        return word[:-2].lower()
    elif word != ("best") and word.endswith("est"):
        return word[:-3].lower()
    else:
        return word.lower()

def aux_lemma(word):
    if re.match(r"(does|did|doing)", word):
        return ("do")
    elif re.match(r"(had|has|'ve|having)", word):
        return ("have")
    elif re.match(r"(is|are|am|was|were|been|'s|being)", word):
        return ("be")
    elif word == ("'d"):
        return ("would")
    else:
        return word.lower()

def part_lemma(word):
    if word == ("n't"):
        return ("not")
    else:
        return word.lower()

def pron_lemma(word):
    if re.match(r"(their|theirs|them|themselves)", word):
        return ("they")
    elif re.match(r"(his|him|himself)", word):
        return ("he")
    elif re.match(r"(her|hers|herself)", word):
        return ("she")
    elif re.match(r"(its|itself)", word):
        return ("it")
    elif re.match(r"(your|yours|yourself)", word):
        return ("you")
    elif re.match(r"(our|us|ours)", word):
        return ("we")
    elif re.match(r"(me|mine|my|myself)", word):
        return ("I")
    elif word == ("I"):
        return word
    else:
        return word.lower()

def det_lemma(word):
    if word == ("an"):
        return ("a")
    else:
        return word.lower()
        

for line in sys.stdin:
    if line.strip():
        (word, tag) = line.strip().split("\t")
        lemma = word
        if tag == "NOUN":
            lemma = noun_lemma(word)
        elif tag == "VERB":
            lemma = verb_lemma(word)
        elif tag == "ADJ":
            lemma = adj_lemma(word)
        elif tag == "AUX":
            lemma = aux_lemma(word)
        elif tag == "PROPN":
            lemma = word
        elif tag == "PART":
            lemma = part_lemma(word)
        elif tag == "PRON":
            lemma = pron_lemma(word)
        else: 
            lemma = word.lower()
        print("{0}\t{1}\t{2}".format(word, tag, lemma))
    else:
        print()
