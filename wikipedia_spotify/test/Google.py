#!/usr/bin/python
__author__ = 'mdenker'

import wikipedia
import sys
import spotipy
import math
import random
from bs4 import BeautifulSoup


import json
import urllib
import urllib2
import operator

# String -> Int
# returns the number of hits for a given search
def showsome(searchfor):

  query = urllib.urlencode({'q': unicode(searchfor).encode("utf-8")})
  print query
  opener = urllib2.build_opener()
  opener.addheaders = [("User-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) "
                                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                                    "Chrome/38.0.2125.111 Safari/537.36")]
  url = 'https://www.google.com/search?%s' % query
  search_response = opener.open(url)
  search_results = search_response.read()
  results = BeautifulSoup(search_results)

  # if no results found
  if not results.find(id="resultStats"):
      return 0

  result_text = results.find(id="resultStats").get_text()
  result_count = result_text.split()
  if result_count[0] == 'About':
      result_count = result_count[1]
  result_count = result_count[0]

  result_count = result_count.replace(',', '')

  return int(result_count)


#showsome('allintitle: foo fighters red hot chili peppers')

#output the dictionary of number of results matched with the artist from the list of artists
def process_all(init_artist, artists):

    if len(artists) > 20:
        artists = artists[0:20]

    artists_dic = dict()
    for first_artist in artists:
        variable = u''.join((u"allintitle: ", unicode(init_artist), u" ", unicode(first_artist)))
        print variable

        artists_dic[first_artist] = [showsome(variable)]

    return artists_dic

#Tests

arts1 = process_all("Mumford and Sons", ["Red Hot Chili Peppers", "linkin park", "bob dylan", "Taylor Swift"])

#pick three artists based on given dictionary
def pick_artists(artists):
    length = len(artists)

    if length <= 3:
        return artists.keys()

    else:
        third_len = int(math.floor(length / 3))
        sorted_artists = sorted(artists.items(), key=operator.itemgetter(1), reverse = True)
        list_of_thirds = [dict(sorted_artists[i:i+third_len]).keys() for i in range(0, third_len * 3, third_len)]

        base = 0;
        top_artist = list_of_thirds[0][random.randint(0, third_len - 1)]
        print top_artist
        mid_artist = list_of_thirds[1][random.randint(0, third_len - 1)]
        print mid_artist
        length_last = len(list_of_thirds[0]) - 1
        bot_artist = list_of_thirds[2][random.randint(0, length_last)]
        print bot_artist

        return [top_artist, mid_artist, bot_artist]


print pick_artists(arts1)


