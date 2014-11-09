# -*- coding: utf-8 -*-
__author__ = 'mdenker'

import wikipedia

import sys

from Google import random_pick

# Name-> List-of Links
def check_wiki(name):
	test = wikipedia.page(name)
	link = test.links
	n = len(link)
	#print test.categories
	#for i in range(n/2 , n/2+10):
		#print link[i]
		#sys.stdout.write(link[i])
		#sys.stdout.write("\n")
	return random_pick(link, 20)


#if __name__ == '__main__':
#	name = sys.argv[1]
#	a = t(name)

#print vet_all_links(check_wiki("Kanye West"))