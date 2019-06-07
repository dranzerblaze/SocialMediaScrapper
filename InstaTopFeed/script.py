from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import datetime
number = int(input("Enter the number of hashtags"))
taglist = []
for i in range(number):
	tag = input()
	taglist.append(tag)
tagdf = pd.DataFrame(columns = ['Hashtag','Number of posts','Posting Frequency'])
driver = webdriver.Chrome()
for tag in taglist:
	driver.get('https://www.instagram.com/explore/tags/'+str(tag))
	soup = BeautifulSoup(driver.page_source,"lxml")
	tagname = tag
	nposts = soup.find('span',{'class':'g47SY'}).text
	linklist = []
	for link in soup.find_all('a',href=True):
		linklist.append(a['href'])
	newlist = [x for x in linklist if x.startswith('p')]
	del newlist[:9]
	del newlist[9:]
	del newlist[1:8]
	timediff = []
	for j in range(len(newlist)):
		driver.get('https://www.instagram.com'+str(newlist[j]))
		soup = BeautifulSoup(driver.page_source,"lxml")
		for i in soup.findAll('time'):
			if i.has_attr('datetime'):
				timediff.append(i['datetime'])
	datetimeFormat = '%Y-%m-%dT%H:%M:%S.%fZ'
    diff = datetime.datetime.strptime(timediff[0], datetimeFormat)\
        - datetime.datetime.strptime(timediff[1], datetimeFormat)
    pfreq= int(diff.total_seconds()/(9))
    tagdf.loc[len(tagdf)] = [tagname, nposts, pfreq]
driver.quit()
tagdf.to_csv('hashtag.csv')

