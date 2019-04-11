import os

import re

def tracklisting(folder):
    album = os.listdir(folder)
    album.sort()
    listing = []
    for song in album:
        track  = re.search(r'\d\d', song).group()
        songtitle = re.search(r'(.+)-(.+)', song)
        track = str(int(track))
        if len(track) == 1:
            track = ' ' + track
        listing.append(track + songtitle.group(2).split('.')[0])
    listing2 = "\n".join(listing)
    return listing2




