import requests
from lxml import html

#user input
handle = input("Enter handle : ")

#valid username url
url = 'https://www.codechef.com/users/' + handle

page = requests.get(url)

tree = html.fromstring(page.content)

#Storing the text of the first 'main' tag's child 'aside' tag's child tag 'div'
data = tree.xpath("//main[1]/aside/div/text()")

if len(data) == 0:
	print("Invalid handle")

else:
	print("Valid handle")
