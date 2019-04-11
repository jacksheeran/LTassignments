# IPA correspondences according to
# https://en.wikipedia.org/wiki/ARPABET
# for the phonemes used by CMUdict according to
# http://www.speech.cs.cmu.edu/cgi-bin/cmudict .
ipadict = {
    'AA':'ɑ',                   # AA	odd     AA D
    'AE':'æ',                   # AE	at	AE T
    'AH':'ʌ',                   # AH	hut	HH AH T
    'AO':'ɔ',                   # AO	ought	AO T
    'AW':'aʊ',                  # AW	cow	K AW
    'AY':'aɪ',                  # AY	hide	HH AY D
    'B':'b',                    # B 	be	B IY
    'CH':'tʃ',                  # CH	cheese	CH IY Z
    'D':'d',                    # D 	dee	D IY
    'DH':'ð',                   # DH	thee	DH IY
    'EH':'ɛ',                   # EH	Ed	EH D
    'ER':'ɝ',                   # ER	hurt	HH ER T
    'EY':'eɪ',                  # EY	ate	EY T
    'F':'f',                    # F 	fee	F IY
    'G':'ɡ',                    # G 	green	G R IY N
    'HH':'h',                   # HH	he	HH IY
    'IH':'ɪ',                   # IH	it	IH T
    'IY':'i',                   # IY	eat	IY T
    'JH':'dʒ',                  # JH	gee	JH IY
    'K':'k',                    # K 	key	K IY
    'L':'l',                    # L 	lee	L IY
    'M':'m',                    # M 	me	M IY
    'N':'n',                    # N 	knee	N IY
    'NG':'ŋ',                   # NG	ping	P IH NG
    'OW':'oʊ',                  # OW	oat	OW T
    'OY':'ɔɪ',                  # OY	toy	T OY
    'P':'p',                    # P 	pee	P IY
    'R':'ɹ',                    # R 	read	R IY D
    'S':'s',                    # S 	sea	S IY
    'SH':'ʃ',                   # SH	she	SH IY
    'T':'t',                    # T 	tea	T IY
    'TH':'θ',                   # TH	theta	TH EY T AH
    'UH':'ʊ',                   # UH	hood	HH UH D
    'UW':'u',                   # UW	two	T UW
    'V':'v',                    # V 	vee	V IY
    'W':'w',                    # W 	we	W IY
    'Y':'j',                    # Y 	yield	Y IY L D
    'Z':'z',                    # Z 	zee	Z IY
    'ZH':'ʒ',                   # ZH	seizure	S IY ZH ER
}

import pronouncing

import string

def ipa_word(s):
    """convers APRAbet to IPA"""
    inipa = ''
    for x in s.split():
        x = x.rstrip(string.digits)
        inipa = inipa + ipadict[x]
    return inipa

        
    
