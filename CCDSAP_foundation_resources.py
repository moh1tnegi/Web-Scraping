import requests
from lxml import html


def foundation_resources(link):
	'''This function collects all the learning material
		available for preparation for CCDSAP'''
	pageLink = link + '/certification/prepare#foundation'
	sourceSoup = requests.get(pageLink) 
	sourceCode = sourceSoup.content
	htmlElements = html.fromstring(sourceCode)
	
	print('1. Foundation.\n2. Advanced.\n3. Expert.')
	usrIn = int(input("Enter a choice: "))
	if usrIn is 1:
		selector = '2'
		print('\nFoundation:')
	elif usrIn is 2:
		selector = '4'
		print('\nAdvanced:')
	elif usrIn is 3:
		selector = '6'
		print('\nExpert:')
	else:
		print("Wrong Input!")
	data = htmlElements.xpath('//*[@id="node-9685883"]\
		/div[2]/div['+selector+']/ul[2]')  # selects user specified path
	#foundation, advanced or expert

	index = 0 #for numbering lists
	try: # dont know how many number of lists are there
		while data[0][index][0].text_content():
			print(str(index+1)+'. '+data[0][index][0].text_content())
			index += 1
	except IndexError: # if index goes beyond lists, will move to next step
		usrIn = int(input("Your call: ")) #user input according to lists above
		if usrIn<1 or usrIn>index-1:
			print("Wrong Selection!")
			usrIn = 1 # default selection

	print(data[0][usrIn-1].text_content()) # prints all content inside a list

	# TODO : print url to specific lists! 	~
	data = htmlElements.xpath('//*[@id="node-9685883"]\
		/div[2]/div['+selector+']/ul[2]/li[1]/ul/li[1]/ul/li[1]/a')
	# prints url of the very first list in Basic
	print(data[0].text_content()+ ': ' + (data[0].attrib)['href'] \
		+ '\n')


def main():
	link = 'https://www.codechef.com'
	foundation_resources(link)



if __name__ == '__main__':
	main()
