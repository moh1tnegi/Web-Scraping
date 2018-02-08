import requests
from lxml import html
import learning_resources as lr
import specific_urls as su


if __name__ == '__main__':
	print('Please Wait...')
	link = 'https://www.codechef.com'
	pageLink = link + '/certification/prepare#foundation'

	sourceSoup = requests.get(pageLink) 
	sourceCode = sourceSoup.content
	htmlElements = html.fromstring(sourceCode)

	usrIn, selector = lr.learning_resources(htmlElements)
	su.specific_urls(htmlElements, usrIn, selector)

	while 1:
		try:
			again = input("Again?(y/n): ")
			if(again is 'y' or again is 'Y'):
				usrIn, selector = lr.learning_resources(htmlElements)
				su.specific_urls(htmlElements, usrIn, selector)
			else:
				break
		except NameError:
			break
