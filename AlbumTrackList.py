import os

import re

"""Takes an album folder and returns a readable listing of track numbers and song titles."""

def tracklisting(folder):
    
    
    album = os.listdir(folder) #creates a list of tracks' file names
    
    album.sort()
    
    listing = []
    
    for song in album:
        track  = re.search(r'\d\d', song).group() #finds track number
        
        songtitle = re.search(r'(.+)-(.+)', song) #finds song title
        
        track = str(int(track)) #convers track number to string to be joined to title
        
        if len(track) == 1:
            track = ' ' + track #ensures all tracks numbers are at least two characters long
            
        listing.append(track + songtitle.group(2).split('.')[0]) #adds each joined track number and song title  into a single printable string
        
    listingjoined = "\n".join(listing) #creates a string with each listing on a separate line
    
    return listingjoined




