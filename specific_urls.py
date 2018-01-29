def specific_urls(htmlElements, usrIn, selector):
	
	# condition for expert as expert list don't have same structure as others
	if selector is '6':
		data = htmlElements.xpath('//*[@id="node-9685883"]/div[2]/div[6]/ul[2]/li/a')
		print(data[0].text_content()+': '+(data[0].attrib)['href']+'\n')
	if selector is '4' and usrIn is 20: # advanced->general category don't have third list
		data = htmlElements.xpath('//*[@id="node-9685883"]/div[2]/div[4]/ul[2]/li[20]/ul/li[1]/a')
		print(data[0].text_content(), ': ', (data[0].attrib)['href'], '\n')


	# data for traversing way down to all the lists
	data = lambda x, y, z: htmlElements.xpath('//*[@id="node-9685883"]\
		/div[2]/div['+selector+']/ul[2]/li['+str(x)+']/ul/li['+str(y)\
		+']/ul/li['+str(z)+']/a')

	# jData for second lists, that are: basic, resources and practice etc
	jData = lambda x, y: htmlElements.xpath('//*[@id="node-9685883"]\
		/div[2]/div['+selector+']/ul[2]/li['+str(x)+']/ul/li['+str(y)+']/text()') 

	i = usrIn
	for j in range(1, 5):
		try: # as number of lists are distinct, exception will be caught
			k = 0 # k represents the lists of links 'real links' ;P
			print((jData(i, j))[0]) 
			while 1:
				try:
					k += 1 # list children incrementing from 1
					# printing content and its url
					print(str(k)+'. '+(data(i, j, k))[0].text_content()+ ': ' \
						+ (((data(i, j, k))[0]).attrib)['href']+'\n')
				except IndexError:
					break
			_ = data(i, j, k) # ignore lvalue, its only for catching exception for outer loop
		except IndexError:
			return

		
