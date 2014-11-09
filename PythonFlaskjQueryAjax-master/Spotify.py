import spotipy
import sys
from simplejson.scanner import JSONDecodeError

def get_artist(name):
    sp = spotipy.Spotify()
    results = sp.search(q=u''.join((u'artist:', unicode(name))), type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None


#if __name__ == '__main__':

    
    
   # name = sys.argv[1]
    artist = get_artist(name)
    
    uri = artist['uri']
    response = sp.artist_top_tracks(uri)
    for track in response['tracks']:
    	#print track['name']
    	sys.stdout.write(track['name'])
    	sys.stdout.write("\n")

# List-of links -> List-of Artists (Strings)
# Checks against spotify database to return only valid artists
def vet_all_links(links):
    sp = spotipy.Spotify()
    artists = list()
    for link in links:
        try:
            results = sp.search(q=u''.join((u'artist:', unicode(link))), type='artist')
            items = results['artists']['items']
            if len(items) > 0 and items[0]['name'] == link:
                artists.append(link)
        except JSONDecodeError:
            pass
    return artists
