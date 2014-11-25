__author__ = 'misaki'
import wikipedia
import spotipy
import json


class SearchCode(object):
	sp = None
	def __init__(self):
		self.sp = spotipy.Spotify()

	def get_links(self, name):
		originalname = name
		try:
			wikiinfo = wikipedia.page(originalname)
		except:
			try:
				originalname = originalname + "(singer)"
				wikiinfo = wikipedia.page(originalname)
			except:
				wikiinfo = None

		if wikiinfo is None:
			return None
		else:
			return wikiinfo.links

	def findinspotify(self, links):
		if links is None:
			return  None
		names = []
		i = 0
		while len(names) < 3 and i < len(links):
			tmpresults = self.sp.search(q='artist:' + links[i], type='artist')
			tmpitems = tmpresults['artists']['items']
			i = i+ 1
			if len(tmpitems) > 0:
				tmpart = tmpitems[0]
				if tmpart not in names:
					names.append(tmpart)
			else:
				continue
		return names

	def getSongs(self, names):
		total = {}
		if names is None:
			total['message'] = False
			return json.dumps(total)
		if names == []:
			total['message'] = False
			return json.dumps(total)

		total['message'] = True
		m = 0

		for artist in names:
			arturi = artist['uri']
			artname = artist['name']
			images = artist['images']
			if len(images)>0:
				image = images[0]
				imageurl = image['url']
			else:
				imageurl = "https://spotifypresscom.files.wordpress.com/2013/01/spotify-logo-primary-vertical-dark-background-rgb.jpg"
			response = self.sp.artist_top_tracks(arturi)
			tmpd = []
			d = {}
			for track in response['tracks']:
				trackuri = track['uri']
				tmpd.append(trackuri)
			d["name"] = artname
			d["imageurl"] = imageurl
			d["tracks"] = tmpd
			tmpnum = "artist" + str(m)
			total[tmpnum] = d
			m = m + 1
		return json.dumps(total)

	def startsearchrelated(self, name):
		links = self.get_links(name)
		names = self.findinspotify(links)
		tracks = self.getSongs(names)
		return tracks

	def startonesearch(self,name):
		names = self.findinspotify(name)
		tracks = self.getSongs(names)
		return tracks




# if __name__ == '__main__':
# 	sc = SerchCode()
#
# 	songs = sc.startonesearch("sam smith")
# 	print(songs)
