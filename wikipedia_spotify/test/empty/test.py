import wikipedia
import sys
print sys.path


def t(name):
	test = wikipedia.page(name)
	print test.title
	link = test.links
	n = len(link)
	print len(link)
	print test.categories
	for i in range(n/2 , n/2+10):
		#print link[i]
		sys.stdout.write(link[i])
		sys.stdout.write("\n") 
	return link[0:n]

if __name__ == '__main__':
	name = sys.argv[1]	
	a = t(name)
	#sys.exit(a)
	
