import os
from flask import Flask,render_template, request,json
from Spotify import  vet_all_links
from Wiki import check_wiki
from Google import process_all
from Google import pick_artists

import spotipy
import wikipedia

app = Flask(__name__)



@app.route('/')
def hello():
    return 'Welcome to Python Flask!'

@app.route('/signUp')
def signUp():
    return render_template('test.html')

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
	artistname =  request.form['artist']
	sp = spotipy.Spotify()
	name = artistname
	total = {}


	results = sp.search(q='artist:' + name, type='artist')
	items = results['artists']['items']
	if len(items) > 0:
		artist=items[0]
	else:
		total = {'message':'no results'}
		return json.dumps(total)

	originalname = artist['name']
	wikiinfo = wikipedia.page(originalname)
	t = wikiinfo.title
	if (t.lower() != originalname.lower()):
		originalname = originalname + "(singer)"
		wikiinfo = wikipedia.page(originalname)

	link = wikiinfo.links
	names = []
	i = 0
	while len(names) < 3 and i < len(link):
		tmpresults = sp.search(q='artist:' + link[i], type='artist')
		tmpitems = tmpresults['artists']['items']
		i = i+ 1
		if len(tmpitems) > 0:
			tmpart = tmpitems[0]
		else:
			tmpart = None

		if tmpart == None:
			continue
		else:
			if tmpart not in names:
				names.append(tmpart)



	artists = names

	m = 0
	for artist in artists:

		arturi = artist['uri']
		artname = artist['name']
		images = artist['images']
		if len(images)>0:
			image = images[0]
			imageurl = image['url']
		else:
			imageurl = "https://spotifypresscom.files.wordpress.com/2013/01/spotify-logo-primary-vertical-dark-background-rgb.jpg"
		response = sp.artist_top_tracks(arturi)
		tmpd = []
		d = {}
		for track in response['tracks']:

			trackname = track['name']
			trackuri = track['uri']
			tmpd.append(trackuri)

		d["name"] = artname
		d["imageurl"] = imageurl
		d["tracks"] = tmpd
		tmpnum = "artist" + str(m)
		total[tmpnum] = d
		m = m + 1
	return json.dumps(total)
        
    

if __name__=="__main__":
    app.run()
