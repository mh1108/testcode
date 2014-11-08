import spotipy
import sys

def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None


if __name__ == '__main__':
    sp = spotipy.Spotify()
    
    
    name = sys.argv[1]
    artist = get_artist(name)
    
    uri = artist['uri']
    response = sp.artist_top_tracks(uri)
    for track in response['tracks']:
    	#print track['name']
    	sys.stdout.write(track['name'])
    	sys.stdout.write("\n") 