__author__ = 'misaki'




#!/usr/bin/python
import json
import urllib
import urllib2

def showsome(searchfor):
  query = urllib.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.urlopen(url)
  search_results = search_response.read()
  results = json.loads(search_results)
  data = results['responseData']
  print 'Total results: %s' % data['cursor']['estimatedResultCount']
  hits = data['results']
  print 'Top %d hits:' % len(hits)
  for h in hits: print ' ', h['url']
  print 'For more results, see %s' % data['cursor']['moreResultsUrl']

showsome('katy perry')

#output the dictionary of number of results matched with the artist from the list of artists
def processAll(init_artist, artists):

    artists_dic = dict()
    for first_artist in artists:
        query = urllib.urlencode({'q': "allintitle: " + init_artist + first_artist})
        url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
        search_response = urllib.urlopen(url)
        search_results = search_response.read()
        #results = json.loads(search_results)
        #data = results['responseData']
        #length = 'Total results: %s' % data['cursor']['estimatedResultCount']
        #hits = data['results']
        artists_dic[first_artist] = len(search_results)
    return artists_dic


