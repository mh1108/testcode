#!/usr/bin/python
__author__ = 'mdenker'

import wikipedia
import sys
import spotipy
from bs4 import BeautifulSoup

import json
import urllib
import urllib2

    #init_artist = sys.argv[1]
    #artists = sys.argv[2]
    #artists_dic = dict[()]

def showsome(searchfor):

  query = urllib.urlencode({'q': searchfor})
  print query
  opener = urllib2.build_opener()
  opener.addheaders = [("User-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) "
                                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                                    "Chrome/38.0.2125.111 Safari/537.36")]
  url = 'https://www.google.com/search?%s' % query
  search_response = opener.open(url)
  search_results = search_response.read()
  results = BeautifulSoup(search_results)
  result_text = results.find(id="resultStats").get_text()
  result_count = result_text.split()
  if result_count[0] == 'About':
      result_count = result_count[1]
  result_count = result_count[0]

  result_count = result_count.replace(',', '')
  return int(result_count)

#showsome('allintitle: foo fighters red hot chili peppers')

#output the dictionary of number of results matched with the artist from the list of artists
def processAll(init_artist, artists):

    artists_dic = dict()
    for first_artist in artists:
        variable = "allintitle: " + init_artist + " " + first_artist
        print variable

        artists_dic[first_artist] = [showsome(variable)]

    return artists_dic

#Tests

print processAll("Mumford and Sons", ["Red Hot Chili Peppers", "linkin park", "bob dylan", "Taylor Swift"])

    return artists_dic

#Tests

print processAll("Mumford and Sons", ["Red Hot Chili Peppers", "linkin park", "bob dylan", "Taylor Swift"])



