__author__ = 'mdenker'

import random
from Spotify import  vet_all_links
from Wiki import check_wiki
from Google import process_all
from Google import pick_artists

def main(init_artist):
    pick_artists(process_all (init_artist, vet_all_links(check_wiki(init_artist))))


print main(u"Kanye west")