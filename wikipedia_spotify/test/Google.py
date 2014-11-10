#!/usr/bin/python
__author__ = 'mdenker'

import wikipedia
import sys
import spotipy
import math
import re
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

    if len(artists) > 5:
        artists = random_pick(artists, 5)

    artists_dic = dict()
    for first_artist in artists:
        variable = u''.join((u"allintitle: ", unicode(init_artist), u" ", unicode(first_artist)))
        print variable

        artists_dic[first_artist] = [showsome(variable)]

    return artists_dic

#Tests

#arts1 = process_all("Mumford and Sons", ["Red Hot Chili Peppers", "linkin park", "bob dylan", "Taylor Swift"])

# String Dictionary -> Dictionary
#pick three artists *outputted from most to least related*,
# based on given dictionary and returns them with a string value of how they're related
def pick_artists(init_artist, artists):
    length = len(artists)

    if length <= 3:
        return artists.keys()

    else:
        third_len = int(math.floor(length / 3))
        sorted_artists = sorted(artists.items(), key=operator.itemgetter(1), reverse = True)
        list_of_thirds = [dict(sorted_artists[i:i+third_len]).keys() for i in range(0, third_len * 3, third_len)]

        base = 0;
        top_artist = list_of_thirds[0][random.randint(0, third_len - 1)]
        mid_artist = list_of_thirds[1][random.randint(0, third_len - 1)]
        length_last = len(list_of_thirds[0]) - 1
        bot_artist = list_of_thirds[2][random.randint(0, length_last)]

        top_sentence = find_sentence(init_artist, top_artist)
        mid_sentence = find_sentence(init_artist, mid_artist)
        bot_sentence = find_sentence(init_artist, bot_artist)

        return {top_artist:top_sentence, mid_artist:mid_sentence,
                    bot_artist:bot_sentence}


def find_sentence(init_artist, one_artist):
    wiki_body = wikipedia.page(init_artist).content
    #next(right for right in link if right == init_artist)
    sentences = re.findall("([^.]*?" + re.escape(one_artist) + "[^.]*\.)", wiki_body)
    if not len(sentences):
        return "no info available"
    else:
        return sentences[0]

# list of artists -> shorter list of artists
def random_pick(artists, r):

    length = len(artists)
    new_list = list()
    for i in range(0,r):
        to_add = artists[random.randint(0, length-1)]
        if not (to_add in new_list):
            new_list.append(to_add)
    return new_list


print pick_artists("Foo Fighters", {"Nirvana":301, "Trent Reznor":21, "Red Hot Chili Peppers":1,
                                    "deadmau5":20})



