def learning_resources(htmlElements):
	
	'''This function collects all the learning material
		available for preparation for CCDSAP'''	
	print('1. Foundation.\n2. Advanced.\n3. Expert.')
	usrIn = int(input("Enter a choice: "))
	
	if usrIn is 1:
		selector = '2' # for specific child
		print('\nFoundation:')
	elif usrIn is 2:
		selector = '4'
		print('\nAdvanced:')
	elif usrIn is 3:
		selector = '6'
		print('\nExpert:')
	else:
		print("\nWrong Input!")
	
	data = htmlElements.xpath('//*[@id="node-9685883"]\
		/div[2]/div['+selector+']/ul[2]')  # selects user specified path
	#foundation, advanced or expert

	index = 0 #for numbering lists
	try: # dont know how many number of lists are there
		while data[0][index][0].text_content():
			print(str(index+1)+'. '+data[0][index][0].text_content())
			index += 1
	except IndexError: # if index goes beyond lists, will move to next step
		usrIn = int(input("\nYour call: ")) #user input according to lists above
		if usrIn<1 or usrIn>index:
			print("\nWrong Selection!")
			usrIn = 1 # default selection

	yield usrIn
	yield selector
